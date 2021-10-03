import csv 
import numpy as np
def GetdataSource(datapath):
    sleep = []
    coffee = []
    with open(datapath) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sleep.append(float(row["sleep in hours"]))
            coffee.append(float(row["Coffee in ml"]))
    return {"x": sleep, "y": coffee}
def findCorrelation(datasource):
    cr = np.corrcoef(datasource["x"], datasource["y"])
    print ("correlation is ", cr[0,1])
def setup():
    datapath = "data.csv"
    datasource = GetdataSource(datapath)
    findCorrelation(datasource)
setup() 