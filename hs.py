import os

print(os.listdir(),os.getcwd())

def fil():
    myfile=open('heet.txt',"w+")


    for i in range(5):
        myfile.write("my name is heet \n")
    myfile.close()

if __name__=='main':
    fil()        