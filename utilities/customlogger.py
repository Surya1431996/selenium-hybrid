import logging
import inspect

class LogGen:
    def Loggen(logLevel=logging.DEBUG):
        logger_name= inspect.stack()[1] [3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        fh = logging.FileHandler("automation3.log")
        logger.addHandler(fh)
        return logger


    #@staticmethod
   # def loggen():
     #   logging.basicConfig(level=logging.DEBUG, filename="C://Users//assha//PycharmProjects//selenium hybrid//Logs//automation.log", filemode="a")
     ##   logger.setLevel(logging.INFO)
       # return logger
