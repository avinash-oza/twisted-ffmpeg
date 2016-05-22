"""
An adapter which uses the http protocol to get and delete files. No putting of files is supported
"""
import logging
import os
import shutil
import yaml
import urllib
import urlparse
from abc import abstractmethod
from file_name_parsers.file_description import FileDescription
from file_transfer_adapters.abstract_file_transfer_adapter import AbstractFileTransferAdapter
log = logging.getLogger(__name__)

class HTTPFileTransferAdapter(AbstractFileTransferAdapter):
    def __init__(self):
        super(HTTPFileTransferAdapter, self).__init__()
        self.host_url = self._get_config_option('host_root_url')

    def get_file(self, file_description, staging_directory):
        log.info("Calling get_file")
        # We need to download the file to the staging area
        log.info("The file name is {0}".format(self._construct_file_description_url(file_description)))
        pass

    def put_file(self, file_description):
        # This is not implemented for an HTTP server
        raise NotImplementedError

    def _clean_up(self, file_description):
        pass

    def _construct_file_description_url(self, file_description):
        """Constructs a url using the file_description given"""
        segment_date = file_description.segment_date.strftime("%Y%M%d")
        file_name = "{0}-{1}.avi".format(file_description.time_period_start.strftime("%H%M%S"), file_description.time_period_end.strftime("%H%M%S"))
        return '/'.join([file_description.ip_address, file_description.channel, file_description.segment_date.strftime('%Y%m%d'),file_name]) 

    def get_file_paths(self):
        final_file_paths_url = urlparse.urljoin(self.host_url, 'get_file_list')
        log.info("The host url is {0}".format(self.host_url))
        try:
            result = urllib.urlopen(final_file_paths_url)
            # Make the result into a string
            result_str = ''.join(result.readlines())
            result_dict = yaml.load(result_str)

            logging.info("{0} entries returned in file".format(result_dict['number_of_entries']))
        except Exception as e:
            log.exception(e)
        
        else:
            return result_dict['file_paths']
    
