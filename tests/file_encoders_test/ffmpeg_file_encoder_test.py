import unittest
import datetime
import logging
from dingus import Dingus
from file_encoders.ffmpeg_file_encoder import FFmpegFileEncoder
log = logging.getLogger(__name__)

class FFmpegFileEncoderTestCase(unittest.TestCase):
    def setUp(self):
        self.test_class = FFmpegFileEncoder()

    def test___init__(self):
        assert True

    def test_encode_video(self):
        self.test_class.encode_video(Dingus("FileDescription"))
        

