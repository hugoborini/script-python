import csv
import os
import re


def getStatIp():
    data = {}
    tab = []

    final = {}

    testsite_array = []
    with open('data/acess.log') as my_file:
        testsite_array = my_file.readlines()
    

    for log in testsite_array:
        date = re.search(r"(\b\d{1,2}\D{0,3})?\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(Nov|Dec)(?:ember)?)\D?(\d{1,2}\D?)?\D?((19[7-9]\d|20\d{2})|\d{2})", log).group()
        ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', log).group()

        
        if date in data:
            newObject = {**data[date], ip: 1}
            data[date] = newObject
        else:
            object = {
                ip: 1,
            }
            data[date] = object

        
    for cle,valeur in data.items():
        final[cle] = len(valeur.keys())

    print(final)



if __name__=="__main__":
    getStatIp()