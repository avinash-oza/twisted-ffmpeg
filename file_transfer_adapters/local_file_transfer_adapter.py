"""
A simple adapter which takes the source file and puts it in another location on the drive
"""
import logging
import os
from abc import abstractmethod
from file_name_parsers.file_description import FileDescription
from file_transfer_adapters.abstract_file_transfer_adapter import AbstractFileTransferAdapter
log = logging.getLogger(__name__)
logging.basicConfig(format= '%(asctime)s ' + "Encoder " +  '%(message)s', level=logging.DEBUG)

class LocalFileTransferAdapter(AbstractFileTransferAdapter):
    def get_file(self, file_description):
        log.info("Calling get_file")
        pass

    def put_file(self, file_description):
        log.info("Calling put_file")
        pass

    def _clean_up(self, file_description):
        log.info("Calling _clean_up")
        pass

    def get_file_paths(self):
        final_file_paths = []
        file_root = self._get_config_option('get_file_directory')
        for dir_path, _, filenames in os.walk(file_root):
            for filename in filenames:
                #TODO: Make this configurable
                if filename.endswith('.avi'):
                    final_file_paths.append(os.path.join(dir_path, filename))

        return final_file_paths
