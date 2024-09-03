#https://www.pylenin.com/blogs/python-logging-guide/

import logging

logger = logging.getLogger(__name__)

logger.debug("Trying to run this")
logger.warning("I am a separate Logger")
