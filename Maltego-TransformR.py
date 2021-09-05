import argparse
import importlib

def main(args):
    transModule = importlib.import_module('transform.'+args.transform+'.'+args.transform)
    mainTransform = transModule.MainTransform(args.inputFiles,args.outputFile,args.configFile)
    mainTransform.doTransform()
    mainTransform.output()

if(__name__=='__main__'):
    parser = argparse.ArgumentParser(description='A Transform to find out subdomains. Input Type: maltego.Domain Output Type: maltego.DNSName')
    parser.add_argument('-i','--inputFiles',nargs='+',help='the files that contains the exported maltego entities to perform transform')
    parser.add_argument('-o','--outputFile',help='where to store the generated data ( NO .csv suffix needed )')
    parser.add_argument('-c','--configFile',help='the file that contains configuration information for transform(Optional)')
    parser.add_argument('transform',help='the transform you want to use')
    main(parser.parse_args())