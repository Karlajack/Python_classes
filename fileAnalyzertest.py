
def fileopener(filename,openmode):
       with open(filename,openmode) as file:
        for line in file:
            number_lines+= 1
            print(number_lines)
            
number_lines=0          
filename=input("Enter filename or path: ")
openmode=input("open mode? [w,r]: ")

fileopener(filename,openmode)