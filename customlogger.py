import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename= ".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S.%f')


        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


  