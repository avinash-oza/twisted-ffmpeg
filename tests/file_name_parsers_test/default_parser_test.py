import unittest
import datetime
from dingus import Dingus
from file_name_parsers.default_parser import DefaultParser

class DefaultParserTestCase(unittest.TestCase):
    def setUp(self): 
        self.test_path = '/mnt/raid0/DVR/172.16.1.46/CH1/20160415/023547-030548.avi'
        self.parser = DefaultParser()

    def test__extract_file_name(self):
        self.assertEqual(self.parser._extract_file_name(self.test_path), '023547-030548.avi')

    def test__extract_channel_name(self):
        self.assertEqual(self.parser._extract_channel_name(self.test_path), 'CH1')

    def test__extract_file_date(self):
        self.assertEqual(self.parser._extract_file_date(self.test_path), datetime.date(2016, 4, 15))

    def test__extract_time_period_start(self):
        #Arbitrary date chosen for the date time
        expected_date = datetime.datetime(1900,1,1,02,35,47)
        self.assertEqual(self.parser._extract_time_period_start(self.test_path), expected_date.time())

    def test__extract_time_period_end(self):
        expected_date = datetime.datetime(1900,1,1,03,05,48)
        self.assertEqual(self.parser._extract_time_period_end(self.test_path), expected_date.time())

    def test__extract_ip_address(self):
        self.assertEqual(self.parser._extract_ip_address(self.test_path), '172.16.1.46')

    def test__extract_file_source_path(self):
        self.assertEqual(self.parser._extract_file_source_path(self.test_path), '/mnt/raid0/DVR/172.16.1.46/CH1/20160415')

if __name__ == '__main__':
    unittest.main()

