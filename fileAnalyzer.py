# defining fuction to file analyzer
def fileanalyzer(filename,openmode):
    num_lines=0
    num_words=0
    num_char=0
    total_words_length=0
    with open("test.txt",'r') as file:

# counting the number of lines
        for line in file:
            num_lines +=1

# counting the number of words
            word='T'
            for letter in line:
                if (letter !=' ' and word=='T'):
                    num_words +=1

# counting the number of characters                  
                for i in letter:
                    num_char=num_char+1

# caculating the average lengh of the wordss
            for letter in line:
                total_words_length= total_words_length +len(letter)
            av_word_length=total_words_length/len(filename)
   # Printing the results       
    print (f"num_words: {num_words}")
    print(f"num_lines: {num_lines}")
    print(f" num_char: { num_char}")
    print(f" Av_word_length: { av_word_length}")

            

       
filename=input("Enter filename or path: ")
openmode=input("open mode? [w,r]: ")

fileanalyzer(filename,openmode)