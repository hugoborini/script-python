import os
import sys
from datetime import datetime

def saveBdd(dataBaseName, date):
    os.system(f"ssh hugo@52.169.79.53 sudo mysqldump -u root {dataBaseName} > {dataBaseName}_{date}.sql")


if __name__=="__main__":
    date = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    saveBdd(sys.argv[1], date)
