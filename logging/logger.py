import logging
import logging.config
from pathlib import Path
import appdirs

# -----------------------------------------------
# Defaults
# This is the only section that needs adjusting.
# -----------------------------------------------
# Set app name here or import it from a config file
DIR_LOGS: Path = Path(appdirs.user_log_dir("App Name", False))

# 'DEBUG', 'INFO', ('WARNING', 'ERROR', 'CRITICAL')
LOG_CONSOLE_LEVEL: str = 'INFO'

# 'concise', 'standard', 'complete'
LOG_CONSOLE_FORMAT: str = 'standard' 

# 'concise', 'standard', 'complete'
LOG_FILE_FORMAT: str = 'standard' 

# -----------------------------------------------
# Files
# -----------------------------------------------
LOG_INFO: Path  = DIR_LOGS / 'info.log'
LOG_DEBUG: Path = DIR_LOGS / 'debug.log'
LOG_WARN: Path  = DIR_LOGS / 'warning.log'
LOG_ERROR: Path = DIR_LOGS / 'error.log'
LOG_CRIT: Path  = DIR_LOGS / 'critical.log'

# -----------------------------------------------
# Formatters + Handlers
# -----------------------------------------------
FORMAT_DT: str = '%Y-%m-%d %H:%M:%S'
FORMAT_CONCISE: str  = '%(levelname)s : %(message)s'
FORMAT_STANDARD: str = '%(asctime)s : %(levelname)s : %(name)s : %(message)s'
FORMAT_COMPLETE: str = '%(asctime)s : %(threadName)s : %(levelname)s : %(name)s : %(funcName)s : %(message)s'
FILE_HANDLER: str = 'logging.handlers.RotatingFileHandler'
LOGGER_HANDLERS: list = ['console_handler', 'file_handler_info', 'file_handler_debug', 'file_handler_warn', 'file_handler_error', 'file_handler_crit']

# -----------------------------------------------
# Logging config dictionary
# -----------------------------------------------
LOGGING_CONFIG: dict = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
    'concise': {
      'format': FORMAT_CONCISE,
      'datefmt': FORMAT_DT},
    'standard': {
      'format': FORMAT_STANDARD,
      'datefmt': FORMAT_DT},
    'complete': {
      'format': FORMAT_COMPLETE,
      'datefmt': FORMAT_DT},
  },  # end formatters
  'handlers': {
    'console_handler': {
      'class': 'logging.StreamHandler',
      'level': LOG_CONSOLE_LEVEL,
      'formatter': LOG_CONSOLE_FORMAT,
      'stream': 'ext://sys.stdout'},
    'file_handler_info': {
      'class': FILE_HANDLER,
      'level': 'INFO',
      'formatter': LOG_FILE_FORMAT,
      'filename': LOG_INFO,
      'maxBytes': 10485760,  # 10MB
      'backupCount': 3,
      'encoding': 'utf8',
      'delay': True},
    'file_handler_debug': {
      'class': FILE_HANDLER,
      'level': 'DEBUG',
      'formatter': LOG_FILE_FORMAT,
      'filename': LOG_DEBUG,
      'maxBytes': 10485760,  # 10MB
      'backupCount': 3,
      'encoding': 'utf8',
      'delay': True},
    'file_handler_warn': {
      'class': FILE_HANDLER,
      'level': 'WARNING',
      'formatter': LOG_FILE_FORMAT,
      'filename': LOG_WARN,
      'maxBytes': 10485760,  # 10MB
      'backupCount': 3,
      'encoding': 'utf8',
      'delay': True},
    'file_handler_error': {
      'class': FILE_HANDLER,
      'level': 'ERROR',
      'formatter': LOG_FILE_FORMAT,
      'filename': LOG_ERROR,
      'maxBytes': 10485760,  # 10MB
      'backupCount': 3,
      'encoding': 'utf8',
      'delay': True},
    'file_handler_crit': {
      'class': FILE_HANDLER,
      'level': 'CRITICAL',
      'formatter': LOG_FILE_FORMAT,
      'filename': LOG_CRIT,
      'maxBytes': 10485760,  # 10MB
      'backupCount': 3,
      'encoding': 'utf8',
      'delay': True}
  },  # end handlers
  'loggers': {
    '<Module>': {
      'level': 'DEBUG',
      'handlers': LOGGER_HANDLERS,
      'propagate': False},
    '<Module.x>': {
      'level': 'DEBUG',
      'handlers': LOGGER_HANDLERS,
      'propagate': True},
  },  # end loggers
  'root': {
    'level': 'NOTSET',
    # Must attach all file handlers or files will be created but not written.
    'handlers': LOGGER_HANDLERS,
    'propagate': True  # always True
  },  # end root
}

# -----------------------------------------------
# Run this one time in main()
# -----------------------------------------------
def setup_logging():
  '''Sets up logging using the LOGGING_CONFIG dictionary.
  '''
  # Create save directory.
  try:
    Path(DIR_LOGS).mkdir(parents=True, exist_ok=True)

  except Exception as e:
    use_logging_baseconfig()
    logging.error('ERROR prepping logs directory. Console only - no log files will be written.')
    logging.exception(e)            
    return

  # Configure logging.
  try:
    logging.config.dictConfig(LOGGING_CONFIG)
    logging.debug(f'Logs directory: {DIR_LOGS}')
    logging.debug(f'Log file: {LOG_INFO}') 
    logging.debug(f'Log file: {LOG_DEBUG}') 
    logging.debug(f'Log file: {LOG_WARN}') 
    logging.debug(f'Log file: {LOG_ERROR}')
    logging.debug(f'Log file: {LOG_CRIT}')
    
  except Exception as e:
    use_logging_baseconfig()
    logging.error('ERROR in LOGGING_CONFIG. Console only - no log files will be written.')
    logging.exception(e)

# -----------------------------------------------
# Fallback configuration
# -----------------------------------------------
def use_logging_baseconfig():
  '''If any part of logging configuration fails, use these settings instead.
  '''
  logging.basicConfig(level = LOG_CONSOLE_LEVEL, format = FORMAT_STANDARD, datefmt = FORMAT_DT)

# -----------------------------------------------
# Test
# -----------------------------------------------
if __name__ == "__main__": 

  setup_logging()

  logging.debug('Test debug')
  logging.info('Test info')
  logging.warning('Test warn')
  logging.error('Test error')
  logging.critical('Test critical')

