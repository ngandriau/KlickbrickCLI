from klickbrickcli import __version__
from unittest import TestCase

class TestKlick(TestCase):

    def test_dummyTest(self):
        self.assertTrue(1 + 1 == 2)

    def test_version(self):
        self.assertTrue(__version__ == '0.1.0')
