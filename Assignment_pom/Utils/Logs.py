import logging

# Configure logging
logging.basicConfig(filename='example2.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Log some messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')