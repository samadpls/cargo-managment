import sqlite3
import pywhatkit
import datetime
class Sender:
  def __init__(self,sName,sPhone,sAddress):
    self.sName=sName
    self.sAddress=sAddress
    self.sPhone=sPhone

class Recevier:
  def __init__(self,rName,rPhone,rAddress):
    self.rName=rName
    self.rAddress=rAddress
    self.rPhone=rPhone   

class Item:
  def __init__(self,item,Weight):
    self.item=item
    self.Weight=int(Weight)
    self.Price=self.Check()
  def   Check(self):
    if self.Weight<150:
      self.Price=2000
    elif self.Weight>150:
     self.Price=2000
    else:
      print("cant ship")
class CargoCompany:
  def __init__(self,sName,sPhone,sAddress,item,weight,rName,rPhone,rAddress):
    self.s=Sender(sName,sPhone,sAddress) 
    self.i=Item(item,weight)
    self.r=Recevier(rName,rPhone,rAddress)
    self.Detail()

  # def Detail(self):
  #     return f'''sender name={self.s.sName} \nrecevier name={self.r.rName}  \nitem={self.i.item}'''
  #detail will send to the customer
  def Detail(self):
    now = datetime.datetime.now()
    hour=now.hour
    mint=now.minute
    message=f''''Dear {self.r.rName}!\n
    {self.s.sName} has sent you {self.i.item}\n
    It will reach you in 14 bussines days
    '''
    pywhatkit.sendwhatmsg(f'+92{self.r.rPhone}',message,hour,mint+1)
    self.Data()
  def Data(self):
    with sqlite3.connect('database.db') as db:
      cursor= db.cursor()
      sql=f'''insert into stock (sender,"s num","s address",item,weight,recevier,"r num","r address") 
      values('{self.s.sName}','{self.s.sAddress}','{self.s.sPhone}','{self.i.item}','{self.i.Weight}','{self.r.rName}','{self.r.rAddress}','{self.r.rPhone}',)
      '''
    cursor.execute(sql) 
    db.commit()
    cursor.close()
#driver's code
sname=input("Enter Sender Name==> ")      
sphone=input("Enter Sender phone==> ") 
saddress=input("Enter Sender Address==> ") 
item=input("Enter Item==> ") 
weight=input("Enter Weight==> ") 
rname=input("Enter Recevier Name==> ") 
rphone=input("Enter Recevier Phone==> ") 
raddress=input("Enter Recevier Address==> ") 
p1=CargoCompany(sname,sphone,saddress,item,weight,rname,rphone,raddress)

  
    

