import datetime
import time
def Caltime(date1,date2):  
    date1=str(date1)
    date2=str(date2)
    date1=time.strptime(date1,"%Y-%m-%d")  
    date2=time.strptime(date2,"%Y-%m-%d")  
    date1=datetime.datetime(date1[0],date1[1],date1[2])  
    date2=datetime.datetime(date2[0],date2[1],date2[2])  
    return (date2-date1).days
if __name__ == '__main__':
  Caltime('2019-04-23', '2019-05-01')
