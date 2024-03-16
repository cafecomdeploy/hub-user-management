import logging

from utils.log import Config

class Log():
    CONFIG_KEY = 'log'

    @staticmethod
    def get_level():
        return Config.read(Log.CONFIG_KEY, 'level')

    @staticmethod
    def get_filename():
        return Config.read(Log.CONFIG_KEY, 'filename')

    @staticmethod
    def get_format():
        return Config.read(Log.CONFIG_KEY, 'format')

    @staticmethod
    def get_date_format():
        return Config.read(Log.CONFIG_KEY, 'dateformat')

    @staticmethod
    def get_logger(name):
        logger = logging.getLogger(name)
        logger.setLevel(Log.get_level())

        formatter = logging.Formatter(
            Log.get_format(),
            Log.get_date_format())

        file_hdlr = logging.FileHandler(Log.get_filename())
        file_hdlr.setFormatter(formatter)
        logger.addHandler(hdlr=file_hdlr)

        return logger