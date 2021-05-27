import os
import sys
from datetime import datetime

def saveBdd(dataBaseName, date):
    os.system(f"ssh hugo@52.169.79.53 sudo mysqldump -u root {dataBaseName} > {dataBaseName}-{date}.sql")


if __name__=="__main__":

    saveBdd(sys.argv[1], str(datetime.timestamp(datetime.now())))

