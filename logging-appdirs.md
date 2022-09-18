# Logging + `appdirs`

How to write a Python app's logs to an OS-appropriate directory.

## Install

```
py -m pip install appdirs
```

## appdirs Paths

```
appname = "SuperApp"
appauthor = "Acme"

user_data_dir(appname, appauthor)
# Mac OS X:   /Users/trentm/Library/Application Support/SuperApp 
# Windows 7:  C:\Users\trentm\AppData\Local\Acme\SuperApp
# Windows 11: C:\Users\trentm\AppData\Local\Acme\SuperApp     
# Linux:      /home/trentm/.local/share/SuperApp

site_data_dir(appname, appauthor)
# Mac OS X:   /Library/Application Support/SuperApp
# Windows 7:  C:\Users\trentm\AppData\Roaming\Acme\SuperApp
# Windows 11: C:\ProgramData\Acme\SuperApp     
# Linux:      /usr/local/share/SuperApp

user_cache_dir(appname, appauthor)
# Mac OS X:   /Users/trentm/Library/Caches/SuperApp
# Windows 7:  C:\Users\trentm\AppData\Local\Acme\SuperApp\Cache
# Windows 11: C:\Users\trentm\AppData\Local\Acme\SuperApp\Cache     
# Linux:     /home/trentm/.cache/SuperApp

user_log_dir(appname, appauthor)
# Mac OS X:   /Users/trentm/Library/Logs/SuperApp
# Windows 7:  C:\Users\trentm\AppData\Local\Acme\SuperApp\Logs
# Windows 11: C:\Users\trentm\AppData\Local\Acme\SuperApp\Logs    
# Linux:      /home/trentm/.cache/SuperApp/log
```

## Using appdirs

I do this in `configure.py`

```
import appdirs
from pathlib import Path

#
# Project root
DIR_PROJ = Path(__file__).parent
DIR_PACK  = Path(__file__).parent.parent
DIR_USER_HOME = 

#
# App info
APP_NAME = 'SuperApp'
APP_DESC = 'Command line Twitter scraping tools geared towards OSINT'
APP_VS = '0.0.1'
APP_REPO = 'https://github.com/Acme'
APP_AUTHOR = 'Acme' 

#
# appdirs
DIR_USER_DATA  = appdirs.user_data_dir(APP_NAME, APP_AUTHOR)
DIR_SITE_DATA  = appdirs.site_data_dir(APP_NAME, APP_AUTHOR)
DIR_USER_CACHE = appdirs.user_cache_dir(APP_NAME, APP_AUTHOR)
DIR_USER_LOG   = appdirs.user_log_dir(APP_NAME, APP_AUTHOR)

# 
# Log files
LOG_DIR = Path(appdirs.user_log_dir(APP_NAME, False))
LOG_PATH_INFO = Path(LOG_DIR / 'info.log') 
LOG_PATH_DEBUG = Path(LOG_DIR / 'debug.log') 
LOG_PATH_WARN = Path(LOG_DIR / 'warning.log)
LOG_PATH_ERROR = Path(LOG_DIR / 'error.log)
LOG_PATH_CRIT = Path(LOG_DIR / 'critical.log')
 ```
