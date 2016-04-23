from dingus import Dingus
import unittest
from celery_task import CeleryEncoder
from file_name_parsers.file_description import FileDescription


class CeleryEncoderTestCase(unittest.TestCase):
    #TODO: Extend these tests
    def setUp(self):
        self.file_encoder = Dingus('file_encoder')
        self.file_get_adapter = Dingus('file_get_adapter')
        self.file_push_adapter = Dingus('file_push_adapter')

    def test_celery_encoder_init(self):
        test_class = CeleryEncoder(self.file_encoder, self.file_get_adapter, self.file_push_adapter)

    def test_celery_encoder_calls(self):
        test_class = CeleryEncoder(self.file_encoder, self.file_get_adapter, self.file_push_adapter)
        file_description = FileDescription(full_source_path='aaa',
                               file_name='file_name',
                               channel = '1',
                               time_period_start=Dingus('time_period_start'),
                               time_period_end=Dingus('time_period_end'),
                               segment_date=Dingus('segment_date'),
                               ip_address=Dingus('ip_address')
                               )
        test_class.encode_video(file_description)


