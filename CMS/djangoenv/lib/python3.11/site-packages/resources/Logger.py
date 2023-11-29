""" sample docstring

$DESCRIPTION

$AUTHOR

"""

import logging
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.handlers.RotatingFileHandler("log.log", maxBytes=2000, backupCount=10)
handler.setLevel(logging.DEBUG)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)
