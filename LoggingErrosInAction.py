import logging
logging.basicConfig(filename='myfile.log',level=logging.DEBUG)
try:

logging.critical('critical error')

logging.error('second above all errors')
logging.warning('warning error')
logging.info('information')
logging.debug("debug info")
