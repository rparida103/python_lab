import re

"""Splitting Strings on Any of Multiple Delimiters"""
line = 'asdf fjdk; afed, fjek,asdf,      foo'
s = re.split(r'[;,\s]\s*', line)
print(s)

"""Matching Text at the Start or End of a String"""
lines = ["Log: this ia log line", "The process is completed."]

for line in lines:
    if line.startswith("Log:"):
        print(f"This is a log line: {line}")
    if line.endswith("completed."):
        print(f"Completed line: {line}")
    if re.match('Log:', line):
        print(f"Found a match: {line}")

"""Matching and Searching for Text Patterns"""
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.find('no'))

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

datepat = re.compile(r'\d+/\d+/\d+')


if datepat.match(text2):
    print("yes")
else:
    print("NO")


text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

m = datepat.match('11/27/2012')
print(m.group(0))

for m in datepat.finditer(text):
    print(m.groups())

"""Searching and Replacing Text"""
text = 'yeah, but no, but yeah, but no, but yeah'
new_text = text.replace('yeah', 'yep')
print(new_text)

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
#Backslashed digits such as \3 refer to capture group numbers in the pattern.
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(n)

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))