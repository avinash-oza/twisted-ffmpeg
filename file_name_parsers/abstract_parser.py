import os
import datetime
from abc import ABCMeta, abstractmethod
from file_description import FileDescription

class AbstractParser(object):
    __metaclass__ = ABCMeta

    def parse_path(self, file_path_string):
        """Entry method. This will call the parsing functions in a sequence which will extract what we need"""
        file_name = self._extract_file_name(file_path_string)
        channel = self._extract_channel_name(file_path_string)
        segment_date = self._extract_file_date(file_path_string)
        time_period_start = self._extract_time_period_start(file_path_string)
        time_period_end = self._extract_time_period_end(file_path_string)
        ip_address = self._extract_ip_address(file_path_string)
        return FileDescription(file_name=file_name,
                               channel = channel,
                               time_period_start=time_period_start,
                               time_period_end=time_period_end,
                               segment_date=segment_date,
                               ip_address=ip_address)

    @abstractmethod
    def _extract_file_name(self, file_path_string):
        pass

    @abstractmethod
    def _extract_channel_name(self, file_path_string):
        pass

    @abstractmethod
    def _extract_file_date(self, file_path_string):
        pass

    @abstractmethod
    def _extract_time_period_start(self, file_path_string):
        pass

    @abstractmethod
    def _extract_time_period_end(self, file_path_string):
        pass

    @abstractmethod
    def _extract_ip_address(self, file_path_string):
        pass

