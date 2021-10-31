from django.conf import settings
import configparser


class PropertyReader:
    config = configparser.ConfigParser()
    config.read(settings.PROPS_FILE_PATH)

    @staticmethod
    def read_string(section, key):
        print(PropertyReader.config.sections())