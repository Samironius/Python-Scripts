import  re
s = "python for devops"
m = re.match(r'(.*) (.*?) (.*)', s)
print(m.group())