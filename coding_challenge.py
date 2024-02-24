import re

# extract_phone_numbers(string)
 
string = "Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333"

pattern=r"(\d{3})\s\d{3}-\d{4}"

result=re.search(pattern,string)

print (result)


# extract_email_addresses(string)

pattern1=r"\w+@+\w+.+\w"

result=re.search(pattern1,string)
print (result)

# replace_email_addresses(string, replacement)

result=pattern1.sub('REPLACED',string)

print (result)


