from lib import csvIO
from lib.objectFactory import ObjectFactory

class BasicTransform:

    entities=[]
    links=[]
    objectFactory=None

    inputFiles = None
    outputFile = None
    transformConfig = None

    def __init__(self,inputFiles,outputFile,transformConfig):
        print('[*] Initializing Transform')
        self.inputFiles = inputFiles
        self.outputFile = outputFile
        self.transformConfig = transformConfig
        print('[*] Transform Initialized')
        print('[*] Loading Entities')
        for file in self.inputFiles:
            self.entities+= csvIO.readEntityFromCSV(file)
        self.objectFactory = ObjectFactory(self.entities)
        print('[+] Entities Loaded')
        
    def output(self):
        print('[*] Exporting Data')
        csvIO.writeEntitiesToCSV(self.outputFile,self.entities)
        csvIO.writeLinksToCSV(self.outputFile,self.links)
        print('[+] Export Finished')