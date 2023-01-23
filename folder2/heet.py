import os
print('ddd')
print(__name__)
def fil():
    print("hhhh")
    dir_path = os.getcwd()
    new_file_path = str(os.path.join(dir_path, 'heet.txt'))
    print(new_file_path)
    a=open(new_file_path, "w") 
    print(a,'heet ')
    print("heet shah")


    for i in range(5):
        a.write("my name is heet \n")
    a.close()

if __name__=='__main__':
    fil()    