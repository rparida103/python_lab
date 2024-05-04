import re

line = 'asdf fjdk; afed, fjek,asdf,      foo'
after_split = re.split(r'[;,\s]\s*', line)
print(after_split)

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.startswith('yeah'))
print(text.endswith('no'))

# Search for the location of the first occurrence
print(text.find('no'))

text1 = '11/27/2012'
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

# match() always tries to find the match at the start of a string.
# If you want to search text for all occurrences of a pattern, use the findall() method instead.

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))


