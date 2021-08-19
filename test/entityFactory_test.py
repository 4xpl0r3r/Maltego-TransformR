import unittest
from lib.objectFactory import *
from lib import csvIO

class Test_entityFactory(unittest.TestCase):
    def test_init(self):
        res = csvIO.readEntityFromCSV("output/export.csv")
        entityFactory = ObjectFactory(res)
        test = entityFactory.generateEntity("maltego.DNSName")
        pass