# PS4_db_rebuilder

Ps4 built-in database rebuilder has the tendency to remove fpkg from the database. This will repopulate the database with them!

## Requirement

- Python (preferably 3.0+)


## Instructions

**NOTE**: Sony seems to have modified the PS4 DB from 5.05 to the 6.72 system version. Taking this into account, follow the 3) step accordingly to your system. Versions after 5.05 may have to follow the step accordingly to the 6.72 system version.

1) Recurively clone this repo or download a [Release](https://github.com/Zer0xFF/PS4_db_rebuilder/releases)

2) Start FTP server on the PS4

3) Run the python script through terminal/cmdline:
	| Version | Command |
	|--|--|
	| 5.05 | `python3 fix_db.py [PS4_IP] --fw 5.05` |
	| 6.72 | `python3 fix_db.py [PS4_IP]` |

4) Wait for the script to finish, then logout of the PS4 user without closing the browser

5) Log back in and all your games should be there again