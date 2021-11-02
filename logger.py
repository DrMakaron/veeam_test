import logging


logger = logging.getLogger('logger')
logger.setLevel('INFO')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%d/%m/%Y %H:%M:%S')
stream = logging.StreamHandler()
stream.setFormatter(formatter)
logger.addHandler(stream)
