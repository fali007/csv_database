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
            file.close
        else:
            file=open(db_name+'/index.csv','r')
            for i in file:
                temp=i.split(',')
                self.tables.append(temp[0])

    def create_table(self,tb_name,col):
        if tb_name in self.tables:
            print("similar DB already present give another")
            return

        file=open(self.name+'/index.csv','a')
        file.write("%s,%s"%(tb_name,col))
        file.close()

        file=open(self.name+'/'+tb_name+'.csv','w+')
        file.close

        self.tables.append(tb_name)
        print("table created with name %s"%(tb_name))

a=juan_db('felix')
a.create_table('expense',[2,str,int])
print(a.tables)
print(a.name)