#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from ftplib import FTP
import sqlite3
import appinfo
import io
import os
from sfo.sfo import SfoFile as SfoFile
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("PS4_IP", help="PS4 ftp ip address")
args = parser.parse_args()
app_db = "tmp/app.db"
PS4_IP = args.PS4_IP

if not os.path.exists('tmp'):
	os.makedirs('tmp')

class CUSA :
	sfo = None
	size = 10000000
	is_usable = False

info = {}
files = []

def sort_files(file) :
	if("CUSA" in file) :
		files.append("'%s'" % file[-9:])

def get_game_info_by_id(GameID) :
	if(GameID not in info) :
		info[GameID] = CUSA()

		buffer = io.BytesIO()
		ftp.cwd('/system_data/priv/appmeta/%s/' % GameID)
		ftp.retrbinary("RETR param.sfo" , buffer.write)
		buffer.seek(0)
		sfo = SfoFile.from_reader(buffer)
		info[GameID].sfo = sfo
		info[GameID].size = ftp.size("/user/app/%s/app.pkg" % GameID)
		info[GameID].is_usable = True

	return info[GameID]


ftp = FTP()
ftp.connect(PS4_IP, 1337, timeout=30)
ftp.login(user='username', passwd = 'password')
if(len(files) == 0) :
	ftp.cwd('/user/app/')
	ftp.dir(sort_files)
	print(files)


ftp.cwd('/system_data/priv/mms/')
lf = open(app_db, "wb")
ftp.retrbinary("RETR app.db" , lf.write)
lf.close()

conn = sqlite3.connect(app_db)

cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'tbl_appbrowse_%%';")
tables = cursor.fetchall()

files_joined = "SELECT %s AS titleid " % ' AS titleid UNION SELECT '.join(files)
tbl_appbrowse = []
for tbl in tables :
	tbl_appbrowse.append(tbl[0])
	print("Processing table: %s" % tbl[0])
	cursor.execute("SELECT T.titleid FROM (%s) T WHERE T.titleid NOT IN (SELECT titleid FROM %s);" % (files_joined, tbl[0]))
	list_id = cursor.fetchall()
	sql_list = []
	for tmp_GameID in list_id :
		GameID = tmp_GameID[0].replace("'", "")
		print("	Processing GameID: %s... " % GameID, end='')
		cusa = get_game_info_by_id(GameID)
		if(cusa.is_usable == True) :
			sql_list.append("""("%s", "%s", "%s", "/user/appmeta/%s", "2018-07-27 15:06:46.822", "0", "0", "5", "1", "100", "0", "151", "5", "1", "gd", "0", "0", "0", "0", NULL, NULL, NULL, "%d", "2018-07-27 15:06:46.802", "0", "game", NULL, "0", "0", NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, "0", NULL, NULL, NULL, NULL, NULL, "0", "0", NULL, "2018-07-27 15:06:46.757")"""
				% (cusa.sfo['TITLE_ID'], cusa.sfo['CONTENT_ID'], cusa.sfo['TITLE'], cusa.sfo['TITLE_ID'], cusa.size))
			print("Completed %d" % cusa.size)
		else :
			print("Skipped")

	if(len(sql_list) > 0) :
		cursor.execute("INSERT INTO %s VALUES %s;" % (tbl[0], ', '.join(sql_list)))

print('')
print('')
print('')

print("Processing table: tbl_appinfo")

cursor.execute("SELECT DISTINCT T.titleid FROM (SELECT titleid FROM %s) T WHERE T.titleid LIKE 'CUSA%%' AND T.titleid NOT IN (SELECT DISTINCT titleid FROM tbl_appinfo);" % (" UNION SELECT titleid FROM ".join(tbl_appbrowse)))
missing_appinfo_cusa_id = cursor.fetchall()
for tmp_cusa_id in missing_appinfo_cusa_id :
	game_id = tmp_cusa_id[0]
	print("	Processing GameID: %s... " % game_id, end='')
	cusa = get_game_info_by_id(game_id)
	if(cusa.is_usable == True) :
		sql_items = appinfo.get_pseudo_appinfo(cusa.sfo, cusa.size)
		for key, value in sql_items.items():
			cursor.execute("INSERT INTO tbl_appinfo (titleid, key, val) VALUES (?, ?, ?);", [game_id, key, value])
		print("Completed")
	else :
		print("Skipped")

conn.commit()

conn.close()

ftp.cwd('/system_data/priv/mms/')
file = open(app_db,'rb')
ftp.storbinary('STOR app.db', file)
file.close()
