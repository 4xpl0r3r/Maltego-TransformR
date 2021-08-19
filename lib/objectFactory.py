from config.config import *
from itertools import islice
import csv
import numpy
import functools
import random

int36 = functools.partial(int, base=36)


def str36(number):
    return numpy.base_repr(number, base=36).lower()


class ObjectFactory:
    entityPrototypes = {}
    objectIDGenerator = None

    class ObjectIDGenerator:
        baseID = int36('2000000000000')
        nextID = 0

        def __init__(self, data):  # 使用所有数据进行初始化
            randomRange = int36("i00000000000")
            checkFlag = True
            while checkFlag:
                self.baseID = self.baseID + random.randint(0, randomRange)
                checkFlag = False
                for item in data:
                    if abs(int36(item['EntityID']) - self.baseID) < 100000:
                        checkFlag = True
            self.nextID = self.baseID

        def getNextID(self):
            self.nextID += 1
            return str36(self.nextID-1)

    def __init__(self,data):
        self.objectIDGenerator = self.ObjectIDGenerator(data)
        with open(ENTITYDB, "r") as dbfile:
            csvReader = csv.reader(dbfile)
            for line in csvReader:
                self.entityPrototypes[line[0]] = {}
                self.entityPrototypes[line[0]]['EntityID'] = None
                self.entityPrototypes[line[0]]['EntityType'] = line[0]
                for key in islice(line, 1, None):
                    self.entityPrototypes[line[0]][key] = None

    def generateEntity(self, type):
        if type in self.entityPrototypes.keys():
            newEntity = self.entityPrototypes[type].copy()
            newEntity['EntityID'] = self.objectIDGenerator.getNextID()
            return newEntity
        else:
            raise Exception("Can't find type: "+type)

    def generateLink(self, SourceEntityID, TargetEntityID,
                     maltego_link_label=None,
                     maltego_link_show_label=0,
                     maltego_link_color=None,
                     maltego_link_style=None,
                     maltego_link_thickness=-1,
                     maltego_link_transform_name=None,
                     maltego_link_transform_display_name=None,
                     maltego_link_transform_version=0,
                     maltego_link_transform_run_date=0):
        return {
            'LinkID': self.objectIDGenerator.getNextID(),
            'SourceEntityID': SourceEntityID,
            'TargetEntityID': TargetEntityID,
            'maltego.link.label': maltego_link_label,
            'maltego.link.show-label': maltego_link_show_label,
            'maltego.link.color': maltego_link_color,
            'maltego.link.style': maltego_link_style,
            'maltego.link.thickness': maltego_link_thickness,
            'maltego.link.transform.name': maltego_link_transform_name,
            'maltego.link.transform.display-name': maltego_link_transform_display_name,
            'maltego.link.transform.version': maltego_link_transform_version,
            'maltego.link.transform.run-date': maltego_link_transform_run_date
        }
