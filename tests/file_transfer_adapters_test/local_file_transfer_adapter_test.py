import unittest
import datetime
from dingus import Dingus
from file_transfer_adapters.local_file_transfer_adapter import LocalFileTransferAdapter

class LocalFileTransferAdapterTestCase(unittest.TestCase):
    def test__init(self):
        test_class = LocalFileTransferAdapter()

