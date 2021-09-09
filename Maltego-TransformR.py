import argparse
import json
import importlib

def main(args):
    transModule = importlib.import_module('transform.'+args.transform+'.'+args.transform)
    transformConfig = None
    configPath = 'config.json'
    if(args.configFile):
        configPath = args.configFile
    with open(configPath) as f:
        transformConfig = json.loads(f.read())[args.transform]
    mainTransform = transModule.MainTransform(args.inputFiles,args.outputFile,transformConfig)
    mainTransform.doTransform()
    mainTransform.output()

if(__name__=='__main__'):
    parser = argparse.ArgumentParser(description='A Transform to find out subdomains. Input Type: maltego.Domain Output Type: maltego.DNSName')
    parser.add_argument('-i','--inputFiles',nargs='*s',help='the files that contains the exported maltego entities to perform transform')
    parser.add_argument('-o','--outputFile',help='where to store the generated data ( NO .csv suffix needed )')
    parser.add_argument('-c','--configFile',help='the config file that used to replace default config file (Optional)')
    parser.add_argument('transform',help='the transform you want to use')
    main(parser.parse_args())