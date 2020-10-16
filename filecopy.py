import numpy as np
import pandas as pd   
from glob import glob
import sys
import os
from time import ctime
import time
from datetime import datetime
from shutil import copy2

from setup_logger import logger
import yaml


class FileCopyObj(object):

    def __init__(self):
        logger.info('File')

        self.yml = None
        self.targetDirectory = None
        self.sourceDirectory = None



    def readYAML(self,filename="test.yaml"):

        try: 
            with open(filename) as file:
                yml = yaml.load(file)
                print(yml)
                self.yml = yml
        except Exception as e:
            logger.error("Exception Occured while loading YAML...", file=sys.stderr)
            logger.error(e)
            sys.exit(1)


    def setDirectoryParam(self):

        for k, v in self.yml.items():

            if k == "SourceDirectory":
                self.sourceDirectory = v
            if k == "TargetDirectory":
                self.targetDirectory = v

    def readDirectory(self):

        files_grabbed = []
        
        types = ('*.JPG', '*.jpg','*.png','*.PNG')
        files = os.listdir(self.sourceDirectory)

        for current, dirs, files in os.walk(self.sourceDirectory):
            if dirs:
                self.sourceDirs=dirs
            #print("files (walking)",files)
        
        logger.info("SourceDirectory : %s " % self.sourceDirs)

        for t in types:

            for d in self.sourceDirs:
                files = os.path.join(self.sourceDirectory,d , t)
                files_grabbed.extend( glob(files) )

        filesDict = {}
        for f in files_grabbed:

            str1 = time.ctime(os.path.getmtime(f)) # Fri Jun 07 16:54:31 2013
            datetime_object = datetime.strptime(str1, '%a %b %d %H:%M:%S %Y')
            dtfmt = datetime_object.strftime("%Y%m%d") # 06/07/2013
            #print(f,dtfmt)

            filesDict[f] = dtfmt

        for k,v in filesDict.items():
            logger.info("file --> %s, dir --> %s" % (k, v) )


            base = os.path.basename(k)
            mydir = os.path.join(self.targetDirectory,v)


            try:
                if not os.path.exists(os.path.dirname(mydir)):
                    os.makedirs(os.path.dirname(mydir))
                    logger.info("[** CREATED DIRECTORY **] %s" % mydir)
            except OSError as err:
                print(err)

            targetFile = os.path.join(mydir, base)

            copy2(k, targetFile)
            logger.info("file copied to --> %s" % targetFile )
            logger.info("")

        #print(files_grabbed)



        

        


