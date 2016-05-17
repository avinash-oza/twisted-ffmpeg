"""
Defines concrete class FFMPEG file encoder for using the ffmpeg file encoder
"""
import os
import logging
import sys
from abc import ABCMeta, abstractmethod
from collections import namedtuple
from ConfigParser import RawConfigParser, NoOptionError
from file_name_parsers.file_description import FileDescription
from application_config import ApplicationConfig
from abstract_file_encoder import AbstractFileEncoder
log = logging.getLogger(__name__)


class FFmpegFileEncoder(AbstractFileEncoder):
    def encode_video(self, file_description):
        log.info("Called encode_video")

    
