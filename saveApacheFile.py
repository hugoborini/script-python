import os
import sys
from datetime import datetime

def saveApacheFile(date):

    os.system(f"scp -r hugo@52.169.79.53:/etc/apache2 saveApacheFile/apache2-{date}")

if __name__=="__main__":
    date = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    saveApacheFile(date)