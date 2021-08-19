from config.config import *
import csv

def generateFiledName(data):
    solvedType = []
    fieldName = []
    # 生成键表
    for item in data:#遍历数组
        if not item['EntityType'] in solvedType: # 优化-同类型不再多次遍历
            solvedType.append(item['EntityType'])
            for key,values in  item.items():
                if not key in fieldName:
                    fieldName.append(key)
    return fieldName

def readEntityFromCSV(filename):
    with open(filename,"r") as readFrom:
        csvReader = csv.DictReader(readFrom)
        data = []
        for row in csvReader:
            data.append(row)
        return data

def writeEntitiesToCSV(filename,data):
    with open(filename + '.csv','w') as writeTo:
        csvWriter = csv.DictWriter(writeTo,generateFiledName(data))
        csvWriter.writeheader()
        for item in data:
            csvWriter.writerow(item)

def writeLinksToCSV(filename,data):
    with open(filename + '_links.csv','w') as writeTo:
        csvWriter = csv.DictWriter(writeTo,
        ['LinkID','SourceEntityID','TargetEntityID','maltego.link.label','maltego.link.show-label','maltego.link.color','maltego.link.style','maltego.link.thickness',
        'maltego.link.transform.name','maltego.link.transform.display-name','maltego.link.transform.version','maltego.link.transform.run-date'])
        csvWriter.writeheader()
        for item in data:
            csvWriter.writerow(item)