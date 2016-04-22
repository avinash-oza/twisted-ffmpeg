"""
Defines the basic interface an adapter for a protocol should implement.
Configurations for any of the adapters should be stored in configs/ with the same name as the adapter file
"""
import os
import logging
from abc import ABCMeta, abstractmethod
from collections import namedtuple
from ConfigParser import RawConfigParser, NoOptionError
from file_name_parsers.file_description import FileDescription

log=logging.getLogger(__name__)

class AbstractFileTransferAdapter(object):
    __metaclass__ = ABCMeta

    def __init__(self):
       self.config = RawConfigParser(allow_no_value=True)
       self._load_configuration_file()

    @abstractmethod
    def get_file(self, file_description):
        """TBD: Given a FileDescription, this figures out which file to obtain"""

    @abstractmethod
    def put_file(self, file_description):
        """TBD: Give the file description and the original source path, this method will transfer the file remotely"""
    
    @abstractmethod
    def _get_config_file_name(self):
        """Returns the name of the config file to look for in configs/"""

    def _load_configuration_file(self):
        current_working_directory = os.getcwd()
        full_path = os.path.join(current_working_directory, "file_transfer_adapters", 'configs')
        config_file_path = os.path.join(full_path, self._get_config_file_name())

        log.info("Opening configuration at {0}".format(config_file_path))
        with open(config_file_path, 'rb') as config_file:
            self.config.readfp(config_file)

    def _get_config_option(self, section, field):
        ret = ""
        try:
            ret = config.get(section,option)
        except NoOptionError:
            #value does not exist
            log.warning("Value does not exist for section {0} and option {1}".format(section, option))
        return ret

