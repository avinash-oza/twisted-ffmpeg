"""
Defines the basic interface an adapter for a protocol should implement
"""
from abc import abstractmethod
from collections import namedtuple
from file_description import FileDescription

class AbstractFileTransferAdapter(object):
    @abstractmethod
    def get_file(self, file_description):
        """TBD: Given a FileDescription, this figures out which file to obtain"""
        pass

    @abstractmethod
    def put_file(self, file_description):
        """TBD: Give the file description and the original source path, this method will transfer the file remotely"""
        pass
