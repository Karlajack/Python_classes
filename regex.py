import re

#pattern=re.compile('^Hello')

#result=pattern.finditer('Hello world,Hello,Kenya')
#result=pattern.search('Hello world')

#for match in result:
 #   print (match)

#print(result)


#text="This is my phone number 111-111-1111"

#pattern=r"\d{3}-\d{3}-\d{4}"
#result=re.search(pattern,text)


# define regex pattern  for phone number +254-234-098-134

text="This is my phone number +254-234-098-134"

pattern= r"\+\d{3}-\d{3}-\d{3}-\d{3}"

result=re.search(pattern,text)

print(result)