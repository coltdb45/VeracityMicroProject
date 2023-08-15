import csv
import time 
from datetime import datetime, timezone

def sum1forline(filename):
    with open(filename) as f:
        return sum(1 for line in f)

def filterData(path, information):
    with open(path, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            print(row[information])



def main():
    length = sum1forline()
    while True:
        #st_iso = datetime.now(timezone.utc).isoformat() Gets System time UTC in ISO format
        
        dataTime = filterData('/home/colt/Documents/ScienceProject/RxStudio_NavData_PosEcefSAMPLE.xls - RxStudio_NavData_PosEcefSAMPLE.xls.csv','SystemTime (UTC)' )
        

        time.sleep(1)
    
    
    






if __name__ == "__main__":
    main()