from lib import csvIO
from lib.objectFactory import ObjectFactory

class basicTransform:

    entities=None
    links=[]
    objectFactory=None

    def __init__(self,filenmae):
        print('[*] Loading Entities')
        self.entities= csvIO.readEntityFromCSV(filenmae)
        self.objectFactory = ObjectFactory(self.entities)
        print('[+] Entities Loaded')
        
    def output(self,filename):
        print('[*] Exporting Data')
        csvIO.writeEntitiesToCSV(filename,self.entities)
        csvIO.writeLinksToCSV(filename,self.links)
        print('[+] Export finished')