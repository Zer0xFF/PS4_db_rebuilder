_appinfo = {}

_appinfo["#_access_index"] = "67"
_appinfo["#_last_access_time"] = "2018-07-27 15:04:39.822"
_appinfo["#_contents_status"] = "0"
_appinfo["#_mtime"] = "2018-07-27 15:04:40.635"
_appinfo["#_update_index"] = "74"
_appinfo["#exit_type"] = "0"
_appinfo["ATTRIBUTE_INTERNAL"] = "0"
_appinfo["DISP_LOCATION_1"] = "0"
_appinfo["DISP_LOCATION_2"] = "0"
_appinfo["DOWNLOAD_DATA_SIZE"] = "0"
_appinfo["FORMAT"] = "obs"
_appinfo["PARENTAL_LEVEL"] = "1"
_appinfo["SERVICE_ID_ADDCONT_ADD_1"] = "0"
_appinfo["SERVICE_ID_ADDCONT_ADD_2"] = "0"
_appinfo["SERVICE_ID_ADDCONT_ADD_3"] = "0"
_appinfo["SERVICE_ID_ADDCONT_ADD_4"] = "0"
_appinfo["SERVICE_ID_ADDCONT_ADD_5"] = "0"
_appinfo["SERVICE_ID_ADDCONT_ADD_6"] = "0"
_appinfo["SERVICE_ID_ADDCONT_ADD_7"] = "0"
_appinfo["SYSTEM_VER"] = "33751040"
_appinfo["USER_DEFINED_PARAM_1"] = "0"
_appinfo["USER_DEFINED_PARAM_2"] = "0"
_appinfo["USER_DEFINED_PARAM_3"] = "0"
_appinfo["USER_DEFINED_PARAM_4"] = "0"
_appinfo["_contents_ext_type"] = "0"
_appinfo["_contents_location"] = "0"
_appinfo["_current_slot"] = "0"
_appinfo["_disable_live_detail"] = "0"
_appinfo["_hdd_location"] = "0"
_appinfo["_path_info"] = "3113537756987392"
_appinfo["_path_info_2"] = "0"
_appinfo["_size_other_hdd"] = "0"
_appinfo["_sort_priority"] = "100"
_appinfo["_uninstallable"] = "1"
_appinfo["_view_category"] = "0"
_appinfo["_working_status"] = "0"

def get_pseudo_appinfo(sfo, size) :
	copy__appinfo = _appinfo

	copy__appinfo["#_size"] = "%d" % size
	copy__appinfo["_org_path"] = "/user/app/%s" % sfo["TITLE_ID"]
	copy__appinfo["_metadata_path"] = "/user/appmeta/%s" % sfo["TITLE_ID"]

	copy__appinfo["APP_TYPE"] = sfo["APP_TYPE"]
	copy__appinfo["APP_VER"] = sfo["APP_VER"]
	copy__appinfo["ATTRIBUTE"] = sfo["ATTRIBUTE"]
	copy__appinfo["CATEGORY"] = sfo["CATEGORY"]
	copy__appinfo["CONTENT_ID"] = sfo["CONTENT_ID"]
	copy__appinfo["TITLE"] = sfo["TITLE"]
	copy__appinfo["TITLE_ID"] = sfo["TITLE_ID"]
	copy__appinfo["VERSION"] = sfo["VERSION"]

	if(False) :
		print("		%s" % copy__appinfo["APP_TYPE"])
		print("		%s" % copy__appinfo["APP_VER"])
		print("		%s" % copy__appinfo["ATTRIBUTE"])
		print("		%s" % copy__appinfo["CATEGORY"])
		print("		%s" % copy__appinfo["CONTENT_ID"])
		print("		%s" % copy__appinfo["TITLE"])
		print("		%s" % copy__appinfo["TITLE_ID"])
		print("		%s" % copy__appinfo["VERSION"])

	return copy__appinfo