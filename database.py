# create csv based database for small data handling.

import os
class juan_db:
    def __init__(self,db_name):
        self.name=db_name
        self.tables={}
        a=os.listdir()
        if db_name not in a:
            os.mkdir(db_name)
            file=open(db_name+'/index.csv','w+')
            file.close()
        else:
            file=open(db_name+'/index.csv','r')
            for i in file:
                temp=i.split(':')
                self.tables[temp[0]]=temp[1]
            file.close()

    def create_table(self,tb_name,col):
        # name of table, [number of col, type of col]
        if tb_name in self.tables:
            print("similar DB already present give another name")
            return
        file=open(self.name+'/index.csv','a')
        file.write("%s:%s"%(tb_name,col))
        file.write('\n')
        file.close()
        file=open(self.name+'/'+tb_name+'.csv','w+')
        file.close()
        self.tables[tb_name]=col
        print("table created with name %s"%(tb_name))

    def add(self,tb_name,val):
        # validate name, val
        temp=self.tables[tb_name]
        temp=temp[1:-2]
        temp=temp.split(',')
        for i in range(1,len(temp)):
            temp[i]=temp[i][1:]
        print(temp)
        if len(val)==len(temp):
            flag=True
            for i in range(len(val)):
                if str(type(val[i]))!=str(temp[i]):
                    print(len(str(type(val[i]))),len(str(temp[i])))
                    flag=False
            if flag:
                file=open(self.name+'/'+tb_name+'.csv','a')
                file.write('\n')
                for i in range(len(val)):
                    file.write(str(val[i]))
                    if i!=len(val)-1:
                        file.write(',')
                file.close()
            else:
                print("given incorrect format")
        else:
            print("length incorrect")
        pass
    
    def fetch(self,tb_name):
        file=open(self.name+'/'+tb_name+'.csv','r')
        for i in file:
            print(i)
        file.close()



a=juan_db('felix')
a.create_table('ok',[str,int,int,str])
# a.fetch('index')
a.add('ok',['food',1000,10,"new"])
# print(a.tables)