# PS4_db_rebuilder - Updated to 6.72
ps4 built in database rebuilder has the tendency to remove fpkg from the database, this will repopulate the database with them

## requirement
- Python (preferably 3.0+)

## how-to-use
1) recurively clone this repo or download a [Release](https://github.com/Zer0xFF/PS4_db_rebuilder/releases)
2) start FTP server on the PS4
3) run the python script though terminal/cmdline `python3 fix_db.py PS4_IP`
4) wait for the script to finish, then logout of the PS4 user without closing the browser
5) log back in and all your games should be there again

## Changelog
- Fixed error "table tbl_appbrowse_XXXXXXX has 53 columns but 47 values were supplied"
- Support to FW 6.72
