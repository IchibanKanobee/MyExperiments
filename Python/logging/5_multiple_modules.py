#https://www.pylenin.com/blogs/python-logging-guide/

# logging_guide.py
import logging

from modules import helper

log_format = "%(asctime)s::%(levelname)s::%(name)s::"\
             "%(filename)s::%(lineno)d::%(message)s"
             
logging.basicConfig(filename='mylogs_multiple_modules.log', filemode='w', level='DEBUG', format=log_format)

logging.debug("This is a debug message")
logging.info("This is an informational message")
logging.warning("Careful! Something does not look right")
logging.error("You have encountered an error")
logging.critical("You are in trouble")
