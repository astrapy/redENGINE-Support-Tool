import logging
import os

DEBUG_MODE = False
LOG_FILE = 'log/redengine.log'

def init_logging():
    # Ensure the log directory exists
    log_dir = os.path.dirname(LOG_FILE)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    logging.basicConfig(
        filename=LOG_FILE if not DEBUG_MODE else None,
        level=logging.DEBUG if DEBUG_MODE else logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def get_logger(name='RedEngineSupportTool'):
    return logging.getLogger(name)


def get_log_file_path():
    return LOG_FILE if not DEBUG_MODE else None