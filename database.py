# create csv based database for small data handling.

import os
class juan_db:
    def __init__(self,db_name):
        self.name=db_name
        self.tables=[]
        a=os.listdir()
        if db_name not in a:
            os.mkdir(db_name)
            file=open(db_name+'/index.csv','w+')
            file.close()
        else:
            file=open(db_name+'/index.csv','r')
            for i in file:
                temp=i.split(',')
                self.tables.append(temp)
            file.close()

    def create_table(self,tb_name,col):
        # name of table, [number of col, type of col]
        if tb_name in self.tables:
            print("similar DB already present give another name")
            return
        file=open(self.name+'/index.csv','a')
        file.write('\n')
        file.write("%s,%s"%(tb_name,col))
        file.close()
        file=open(self.name+'/'+tb_name+'.csv','w+')
        file.close()
        self.tables.append(tb_name)
        print("table created with name %s"%(tb_name))

    def add(self,tb_name,val):
        # validate name, val
        for i in self.tables:
            if i[0]==tb_name:
                temp=i[1:]
                break
        if len(val)==len(temp):
            file=open(self.name+'/'+tb_name+'.csv','a')
            file.write('\n')
            for i in range(len(val)):
                file.write(str(val[i]))
                if i!=len(val)-1:
                    file.write(',')
            file.close()
        pass
    
    def fetch(self,tb_name):
        file=open(self.name+'/'+tb_name+'.csv','r')
        for i in file:
            print(i)
        file.close()



a=juan_db('felix')
# a.create_table('ok',[str,int])
# a.fetch('index')
a.add('income',['job',10000])
print(a.tables)