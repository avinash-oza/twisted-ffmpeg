from ConfigParser import RawConfigParser, NoOptionError
import os
import logging
log=logging.getLogger(__name__)

class ApplicationConfig(object):
    def __init__(self, config_file_name='twisted-ffmpeg.cfg'):
        self.config = self._load_config(config_file_name)

    def _load_config(self, config_file_name):
        config = RawConfigParser(allow_no_value=True)
        with open(config_file_name, 'rb') as config_file:
            config.readfp(config_file)

        return config

    def get_config_option(self, section, option):
        ret = ""
        try:
            ret = self.config.get(section,option)
        except NoOptionError:
            #value does not exist
            log.warning("Value does not exist for section {0} and option {1}".format(section, option))
        return ret
