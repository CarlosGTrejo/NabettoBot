import csv
from glob import glob as isfile
from time import time
from models.Fetch import fetchSettings

def nGen() -> str(int):
    "number generator"
    i=1
    while True:
        yield str(i)
        i += 1

#===========Creates Bets_n.csv files=============
def currentFile()-> 'Name of Current File':
    header = "time,team,amount\n"

    if not isfile("Bets_?.csv"):
        with open('Bets_0.csv', 'w') as f:
            f.write(header)
        return 'Bets_0.csv'

    else:
        for n in nGen():
            fileName = "Bets_"+n+".csv"
            if not isfile(fileName):
                with open(fileName, 'w') as f:
                    f.write(header)
                return fileName
    
#================================================
fileName = currentFile()
fieldNames = ('time', 'team', 'amount')
#================================================
def timer(start:"Timestamp of the beginning"=None)->"timestamp":
    if start:
        return float('%.3f'%(time())) - start
    else:
        return float('%.3f'%(time()))

def gatherData(msg,timestamp):
    entry = msg.split('-').pop()
    line: "Holds the data that will be written to the csv file" = {"time":None, "team":None, "amount":None}
    line["team"]   = "BLUE" if "BLUE" in entry else "RED"
    line["amount"] = int(entry.split('.').pop(0).split(', ')[1]) # <- This probably won't make sense in the future, but this separates the bet amount and the 'Bet complete for ...' message (ex: [' Bet complete for BLUE', '500'])
    line["time"]   = timestamp
    
    with open(fileName, 'a') as f:
        db = csv.DictWriter(f, fieldnames=fieldNames)
        db.writerow(line)
    
    return line





