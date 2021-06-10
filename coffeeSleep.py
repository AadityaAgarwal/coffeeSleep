import pandas as pd
import plotly_express as px
import csv
import numpy as np

def getData(path):
    coffee=[]
    sleep=[]

    with open(path) as f:
        read=csv.DictReader(f)
        fileData=list(read) #.pop(0)

        for i in fileData:
            coffee.append(float(i['Coffee in ml']))
            sleep.append(float(i['sleep in hours']))
    return(coffee,sleep)


def findCorrelation(dataSrc):
    correlation=np.corrcoef(dataSrc[0],dataSrc[1])
    print("correlation: ",correlation)

def setup():
    path='coffeSleep.csv'
    dataSrc=getData(path)

    findCorrelation(dataSrc)

setup()
