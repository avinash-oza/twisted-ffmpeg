"""
Defines the basic interface an adapter for a protocol should implement
"""
from collections import namedtuple
FileDescription = namedtuple('FileDescription', 'file_name', 'channel', 'time_period_start', 'time_period_end', 'ip_address')

class AbstractFileTransferAdapter(object):
    def get_file(self, file_destination, file_description=None, file_path=None):
        """TBD: Given a FileDescription or file_path, this retrieves the file and gives a return code"""
            raise NotImplementedError

    def put_file(self, full_source_path, file_description):
        """TBD: Given the full_source_path, this will transfer the file using the description of the file"""
            raise NotImplementedError
