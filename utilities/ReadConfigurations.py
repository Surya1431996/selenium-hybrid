import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class read_configuration:
    @staticmethod
    def geturl():
        url=config.get('basic info','url')
        return url
