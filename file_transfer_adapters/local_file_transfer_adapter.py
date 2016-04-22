"""
A simple adapter which takes the source file and puts it in another location on the drive
"""
import logging
from abc import abstractmethod
from file_name_parsers.file_description import FileDescription
from abstract_file_transfer_adapter import AbstractFileTransferAdapter
log = logging.getLogger(__name__)

class LocalFileTransferAdapter(AbstractFileTransferAdapter):
    def _get_config_file_name(self):
        return "local_file_transfer_adapter.cfg"

    def get_file(self, file_description):
        pass

    def put_file(self, file_description):
        pass

