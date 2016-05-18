"""
Defines the interface that an encoder needs to follow
"""
import os
import logging
import sys
from abc import ABCMeta, abstractmethod
from collections import namedtuple
from ConfigParser import RawConfigParser, NoOptionError
from file_name_parsers.file_description import FileDescription
from application_config import ApplicationConfig

log=logging.getLogger(__name__)

class EncoderException(Exception):
    pass

class AbstractFileEncoder(object):
    __metaclass__ = ABCMeta

    def __init__(self):
       self.config = ApplicationConfig()

    @abstractmethod
    def encode_video(self, file_description, staging_directory):
        """Encodes a file given a FileDescription tuple. Should return the full path of the encoded file"""

    def _get_config_file_section(self):
        """Returns the name of the section of the configuration for parameters"""
        return self.__class__.__name__

    def _get_config_option(self, field):
        return self.config.get_config_option(self._get_config_file_section(), field)

