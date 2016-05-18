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
from application_config import ApplicationConfig

log=logging.getLogger(__name__)

class AbstractFileTransferAdapter(object):
    __metaclass__ = ABCMeta

    def __init__(self):
       self.config = ApplicationConfig()

    @abstractmethod
    def get_file(self, file_description):
        """TBD: Given a FileDescription, this figures out which file to obtain"""

    @abstractmethod
    def put_file(self, file_description):
        """TBD: Give the file description and the original source path, this method will transfer the file remotely"""

    @abstractmethod
    def get_file_paths(self):
        """This method should return a list of full paths to files that should be encoded"""

    def clean_up(self, file_description):
        try:
            self._clean_up(file_description)
        except Exception as e:
            log.error("Hit exception while trying to clean up file {0}: {1}".format(file_description.file_name, e))

    @abstractmethod
    def _clean_up(self, file_description):
        """Given a file description, this cleans up the file from the location"""
        
    
    def _get_config_file_section(self):
        """Returns the name of the section of the configuration for parameters"""
        return self.__class__.__name__

    def _get_config_option(self, field):
        return self.config.get_config_option(self._get_config_file_section(), field)

