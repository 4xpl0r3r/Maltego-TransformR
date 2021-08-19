import unittest
from lib import csvIO

class Test_csvIO(unittest.TestCase):
    def test_outputSingle(self):
        # self.assertEqual(csvOutputer.a(), 2)
        data=[
            ['maltego.Person','Text','maltego.IPv4Address','maltego.Port'],
            ['UserName','Password','IP Addr','port'],
            ['Mike','hfdawdhiuaw','1.2.3.4',11],
            ['John','fawifuwiagf','2.2.3.4',22],
            ['Steve','AWDWJ89d','3.2.3.4',33],
        ]
        # csvOutputer.outputToCSV('testCSV',data)
    def test_readFromCSV(self):
        res = csvIO.readFromCSV("output/export.csv")
        csvIO.writeToCSV('test',res)
    def test_generateFiledName(self):
        res = csvIO.readEntityFromCSV("output/export.csv")
        print(csvIO.generateFiledName(res))


if __name__ == '__main__':
    unittest.main()