import pandas as pd
import plotly_express as px
import csv
import numpy as np

def getData(path):
    temp=[]
    ice=[]

    with open(path) as f:
        read=csv.DictReader(f)
        fileData=list(read) #.pop(0)

        for i in fileData:
            temp.append(float(i['Marks In Percentage']))
            ice.append(float(i['Days Present']))
    return(temp,ice)


def findCorrelation(dataSrc):
    correlation=np.corrcoef(dataSrc[0],dataSrc[1])
    print("correlation: ",correlation)

def setup():
    path='marks.csv'
    dataSrc=getData(path)

    findCorrelation(dataSrc)

setup()