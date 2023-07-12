import logging
# custom logging
"""
    1. import logging
"""

# logger = logging.getLogger(__name__) #create logger with the filename as I have name the file
# logger.propagate = False
# logger.info('Hello from custom')

"""
    Lock handler.
    => Handler objects are responsible for dispatching the appropriate lock message to the handlers specific destination, for example you can use lock handler to send log messages to this standard output stream to files vis HTTPL or via via email
"""
# set up 
logger = logging.getLogger(__name__)

# create handler

stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# Set the level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)


logger.warning('This is a Warning')
logger.error('This is an error')
