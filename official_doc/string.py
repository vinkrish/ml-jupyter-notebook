#new line
str = 'First line.\nSecond line.' 
print(str)

#raw string
print(r'C:\some\name')

#multiple string
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

#concat
text = ('Put several strings within parentheses '
            'to have them joined together.')
print(text)

#index
word = 'Python'
print(word[0])

#slicing
print(word[0:2])
print(word[:2])

print(word[4:])
print(word[-2:])

#length
print(len(word))
