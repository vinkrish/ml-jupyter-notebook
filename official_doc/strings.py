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

capitalized_word = text.capitalize()
print(capitalized_word)

capitalized_word = text.title()
print(capitalized_word)

#index
word = 'Python'
print(word[0])

#lower
print(word.lower())

#upper
print(word.upper())

#strip
hello_world = ' Hello World! '
print(hello_world.lstrip())
print(hello_world.strip())
print(hello_world.rstrip())

text = "***Hello, World!***"
result = text.strip("*")
print(result)  # Output: "Hello, World!"


#isalpha, isdigit, isspace
alphanumeric = 'a0 b1'
print(alphanumeric[0].isalpha())
print(alphanumeric[1].isdigit())
print(alphanumeric[2].isspace())

#startswith
print(hello_world.startswith(' Hello'))

#endswith
print(hello_world.endswith('World!'))

#find
print(hello_world.find('World'))

#replace
print(hello_world.replace('World', 'Python'))

#split
split_word = hello_world.split(' ')
print(split_word)
split_word = hello_world.split()
print(split_word)

#join
join_word = '-'.join(split_word)
print(join_word)

#slicing
print(word[0:2])
print(word[:2])

print(word[4:])
print(word[-2:])

#length
print(len(word))

# f-Strings (Formatted String Literals) — Python 3.6+
name = "Alice"
age = 30
greeting = f"Hello, {name}! You are {age} years old."
print(greeting)

# str.format() Method
name = "Alice"
age = 30
greeting = "Hello, {}! You are {} years old.".format(name, age)
print(greeting)

# Percent % Formatting (Older Style)
name = "Alice"
age = 30
greeting = "Hello, %s! You are %d years old." % (name, age)
print(greeting)
