import os
import sys
from datetime import datetime

def saveDb(dataBaseName, date):
    os.system(f"ssh hugo@52.169.79.53 sudo mysqldump -u root {dataBaseName} > saveDb/{dataBaseName}_{date}.sql")


if __name__=="__main__":
    dbName = ""
    date = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

    if len(sys.argv) == 1 :
        dbName = input("veuillez rentrer le nom de la table : ")
        saveDb(dbName, date)
    else:
        saveDb(sys.argv[1], date)

