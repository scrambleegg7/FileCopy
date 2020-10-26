from filemove import FileCopyObj 

import numpy as np   
import pandas as pd   




def main():

    print(" main routine.")
    flObj = FileCopyObj()

    flObj.readYAML("nec.yaml")
    flObj.setDirectoryParam()
    flObj.readDirectory()



if __name__ == "__main__":
    main()