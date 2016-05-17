import unittest
import datetime
import logging
from dingus import Dingus
from file_name_parsers.file_description import FileDescription
from file_encoders.ffmpeg_file_encoder import FFmpegFileEncoder
log = logging.getLogger(__name__)

class FFmpegFileEncoderTestCase(unittest.TestCase):
    def setUp(self):
        self.test_class = FFmpegFileEncoder()
        self.file_description = FileDescription(full_source_path='aaa',
                               file_name='file_name',
                               channel = '1',
                               time_period_start=datetime.datetime(2015, 10, 10, 12, 30, 50),
                               time_period_end=datetime.datetime(2015, 10, 10, 2, 25, 30),
                               segment_date=datetime.date(2015, 10, 10),
                               ip_address='1.2.3.4'
                               )

    def test___init__(self):
        assert True

    def test_encode_video(self):
        self.test_class.encode_video(self.file_description)
        

