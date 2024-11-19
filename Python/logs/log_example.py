import __main__ as main
import os
import logging


ROOT_DIR = "log"

def get_logger(main_name):
    base_name = os.path.basename(main_name)
    name = os.path.splitext(base_name)[0]
    log_name = name + ".log"

    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logger = logging.getLogger(__name__)

    # To override the default severity of logging
    logger.setLevel('DEBUG')

    # Use FileHandler() to log to a file
    file_handler = logging.FileHandler(log_name)
    formatter = logging.Formatter(log_format)
    file_handler.setFormatter(formatter)

    # Don't forget to add the file handler
    logger.addHandler(file_handler)
    return logger


logger = get_logger(main.__file__)
logger.info("Log message")
