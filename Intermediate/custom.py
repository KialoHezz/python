import logging
# custom logging
"""
    1. import logging
"""

logger = logging.getLogger(__name__) #create logger with the filename as I have name the file
logger.info('Hello from custom')