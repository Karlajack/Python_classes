
def fileopener(filename,openmode):
    with open("test.txt",'r') as file:
            number_of_lines=len(file.readlines())
            print (f"number of lines: {number_of_lines}")


       
filename=input("Enter filename or path: ")
openmode=input("open mode? [w,r]: ")

fileopener(filename,openmode)