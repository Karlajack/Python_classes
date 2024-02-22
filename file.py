#file =open('test.txt','r')

#content=file.read()


#print(content)
#file.close()

#with open("test.txt",'r') as file:
 #for item in file:
    #print(item)

def fileopener(filename,openmode):
     with open(filename,openmode) as file:
        for line in file:
            print(line.strip())

filename=input("Enter filename or path: ")
openmode=input("open mode? [w,r]: ")

fileopener(filename,openmode)

