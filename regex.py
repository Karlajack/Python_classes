import re

#pattern=re.compile('^Hello')


#result=pattern.finditer('Hello world,Hello,Kenya')
#result=pattern.search('Hello world')
#result=pattern.search.sub()

#result=pattern.finditer('Hello world,Hello,Kenya')

#for match in result:
 #   print (match)

#print(result)

#"result=pattern.search.sub('Hi','Hello world,Hello,Kenya')

#print(result)


#Phone number regex pattern: "(?\d{3})?[-.\s]?\d{3}[-.\s]?\d{4}"

#\d=0-9
#\w=0-9 a-z,A-Z,_
\S=whitespace characters
#[]=match grouped character
#()=grouping
#*=zero or more occurence
#?=zero or more ocurence for previous character








Email address regex pattern: "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}"









#text="This is my phone number 111-111-1111"

#pattern=r"\d{3}-\d{3}-\d{4}"
#result=re.search(pattern,text)


# define regex pattern  for phone number +254-234-098-134

text="This is my phone number +254-234-098-134"

pattern= r"\+\d{3}-\d{3}-\d{3}-\d{3}"

result=re.search(pattern,text)

print(result)