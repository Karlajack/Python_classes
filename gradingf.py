# This assign grading to the student's score
def grading(score):
    if (score<1 or score>100):  # check score validity
        print("Enter valid student score!")
    elif (score>=80 and score<=100): # A grading score range
        print("A Grade")
    elif (score>=70 and score<80): # B grading score range
        print("B Grade")
    elif (score>=60 and score<70): # C grading score range
        print("C Grade")
    elif (score>=50 and score<60): # D grading score range
        print("D Grade")
    else:
        print("E Grade") 

    score=int(input("Enter student score= "))

    grading(score)               
