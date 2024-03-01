import math
#pip REPL(read-evaluate-print-loop)
# string data type

# literal assignment

first = "navya"
last = "sree"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))


# constructor function

# donut = str("glazed")

# print(type(donut))
# print(type(donut) == str)
# print(isinstance(donut, str))


# concatenation

fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)


# casting a number to a string
century = str(1999)
print(type(century))
print(century)

statement = "I was born in " + century + "."
print(statement)


# multiple lines
multiline = '''
Hey, Hi!     

I am in Office.
                       How's your day?

'''
print(multiline)

# Escaping special characs

sentence = 'I\'m back to work!\t!\n\nWhere\'s this at\\located?'
print(sentence)


# string Methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("day", "ok"))
print(multiline)


print(len(multiline))
multiline += "             "
multiline = "              " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# Build a menu

title = "menu".upper()
print(title.center(20, "="))
print("coffee".ljust(16, ".") + "$2".rjust(5))
print("Muffin".ljust(16, ".") + "$3".rjust(5))
print("cupcake".ljust(16, ".") + "$4".rjust(5))


# string index value
print(first[1])
print(first[1:4])

# methods returning boolean value/data
# .startswith
# .endswith

# boolean data type
myvalue = False
x = bool(True)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data types
# int, float

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)


# built-in functions for numbers
gpa = 3.8
print(abs(gpa))
print(round(gpa))
print(round(gpa, 1))

print(math.pi)
print(math.sqrt(36))
print(math.ceil(gpa))
print(math.floor(gpa))


#casting a string to number
zip = "60007"
zipvalue = int(zip)
print(type(zipvalue))

#error if you attempt to cast icorrect data
zipvalue = int("newyork")
