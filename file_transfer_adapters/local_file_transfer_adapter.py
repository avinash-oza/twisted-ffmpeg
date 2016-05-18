"""
A simple adapter which takes the source file and puts it in another location on the drive
"""
import logging
import os
import shutil
from abc import abstractmethod
from file_name_parsers.file_description import FileDescription
from file_transfer_adapters.abstract_file_transfer_adapter import AbstractFileTransferAdapter
log = logging.getLogger(__name__)

class LocalFileTransferAdapter(AbstractFileTransferAdapter):
    def get_file(self, file_description, staging_directory):
        log.info("Calling get_file")
        pass

    def put_file(self, file_description):
        put_file_directory = self._get_config_option('put_file_directory')
        full_output_file_path = os.path.join(file_description.full_source_path, file_description.output_file_name)
        #TODO: Maybe refactor this out
        if not os.path.isdir(put_file_directory):
            log.warning("Directory {0} does not exist. Attempting to create".format(put_file_directory))
            os.mkdir(put_file_directory)
        try:
            shutil.copy(full_output_file_path, put_file_directory)
        except Exception as e:
            log.exception(e)

    def _clean_up(self, file_description):
        full_input_file_path = os.path.join(file_description.full_source_path, file_description.file_name)
        full_output_file_path = os.path.join(file_description.full_source_path, file_description.output_file_name)

        try:
            os.remove(full_input_file_path)
            os.remove(full_output_file_path)
        except OSError as e:
            log.exception(e)


    def get_file_paths(self):
        final_file_paths = []
        file_root = self._get_config_option('get_file_directory')
        for dir_path, _, filenames in os.walk(file_root):
            for filename in filenames:
                #TODO: Make this configurable
                if filename.endswith('.avi'):
                    final_file_paths.append(os.path.join(dir_path, filename))

        return final_file_paths
