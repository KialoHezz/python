"""
    Logging : 
    Python comes with in-build module, therefore, you can add logging to your application by simply saying import logging.

    Import logging    

    You can use logging.
        1. Different Block levels, 
        2. Configurations option, 
        3. How to lock in different modules,
        4. How to use different lock handlers,
        5. Capture stack traces in your  log
        6. How to use rotating file handler
"""

import logging

# Lock to five different log levels
# Levels are:-
    #1 debug
    #2 info
    #3 warning
    #4 error
    #5 critical

#  they indicate the severity of the events
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

import custom



