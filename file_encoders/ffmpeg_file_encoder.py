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
from abstract_file_encoder import AbstractFileEncoder, EncoderException
log = logging.getLogger(__name__)


class FFmpegFileEncoder(AbstractFileEncoder):
    def encode_video(self, file_description):
        ffmpeg_command = self._get_config_option("ffmpeg_bin")
        ffmpeg_options = self._get_config_option("ffmpeg_options")


        input_file_full_path = os.path.join(file_description.full_source_path, file_description.file_name)

        output_file_name = self._get_output_file_name(file_description)
        file_description = self._add_output_file_name_to_file_description(file_description, output_file_name)

        output_file_full_path = os.path.join(file_description.full_source_path, file_description.output_file_name)

        ffmpeg_options = ffmpeg_options.format(input_file_name=input_file_full_path,
                                               output_file_name=output_file_full_path
                                               )
        command_to_run = "{0} {1}".format(ffmpeg_command, ffmpeg_options)
        log.info("Command to be invoked to run encoding: {0}".format(command_to_run))
        #TODO: Maybe subproc this or redirect log
        try:
            os.system(command_to_run)
        except Exception as e:
            log.exception(e)
            raise EncoderException("Hit exception in encoder")
        else:
            return file_description



    def _get_output_file_name(self, file_description):
        """Given a file description, this constructs the file name to be written to after encoding"""
        file_name_format_string="{channel_name}_{ip_address}_{segment_date}_{start_time}_{end_time}.avi" 
        segment_date = file_description.segment_date.strftime("%Y-%m-%d")
        start_time = file_description.time_period_start.strftime("%H%M%S")
        end_time = file_description.time_period_end.strftime("%H%M%S")
        return file_name_format_string.format(channel_name=file_description.channel,
                                              ip_address=file_description.ip_address,
                                              segment_date=segment_date,
                                              start_time=start_time,
                                              end_time=end_time)

    def _add_output_file_name_to_file_description(self, file_description, output_file_name):
        return file_description._replace(output_file_name=output_file_name)

    
