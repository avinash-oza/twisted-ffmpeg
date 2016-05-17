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
        ffmpeg_command = self._get_config_option("ffmpeg_bin")
        ffmpeg_options = self._get_config_option("ffmpeg_options")
        command_to_run = "{0} {1}".format(ffmpeg_command, ffmpeg_options)
        log.info("Command to be invoked to run encoding: {0}".format(command_to_run))
        #TODO: Maybe subproc this or redirect log
        ret_value = os.system(command_to_run)
    
