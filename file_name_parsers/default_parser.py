import os
import datetime
from file_description import FileDescription
from abstract_parser import AbstractParser

class DefaultParser(AbstractParser):
    def __init__(self):
        pass

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

    def _extract_file_name(self, file_path_string):
        head, file_name = os.path.split(file_path_string)
        return file_name

    def _extract_channel_name(self, file_path_string):
        head, file_name = os.path.split(file_path_string)
        head, file_date = os.path.split(head)
        head, channel_number = os.path.split(head)
        return channel_number

    def _extract_file_date(self, file_path_string):
        head, file_name = os.path.split(file_path_string)
        head, file_date = os.path.split(head)
        return datetime.datetime.strptime(file_date, '%Y%m%d').date()

    def _extract_time_period_start(self, file_path_string):
        start_time_str, _  = self._get_start_and_end_time_str(file_path_string)
        return datetime.datetime.strptime(start_time_str, '%H%M%S').time()

    def _extract_time_period_end(self, file_path_string):
        _ , end_time_str =  self._get_start_and_end_time_str(file_path_string)
        return datetime.datetime.strptime(end_time_str, '%H%M%S').time()

    def _extract_ip_address(self, file_path_string):
        head, file_name = os.path.split(file_path_string)
        head, file_date = os.path.split(head)
        head, channel = os.path.split(head)
        head, ip_address = os.path.split(head)
        return ip_address


    def _get_start_and_end_time_str(self, file_path_string):
        """Helper method to extract out the start and end times"""
        head, file_name = os.path.split(file_path_string)
        time_str, ext = os.path.splitext(file_name)
        start_time_str, end_time_str = time_str.split('-')
        return start_time_str, end_time_str
        
