import re

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))


text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
#Backslashed digits such as \3 refer to capture group numbers in the pattern.
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))

