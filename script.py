"""
Different examples of string formatting, including:
dicts, lists, numbers, and dates.
"""
# String formatting using f-strings
import datetime
person = {'name': 'Jenn', 'age': 23}

sentence = f'My name is {person["name"]} and I am {person["age"]} years old.'

# using format() and **
sentence = "My name is {name} and I am {age} years old.".format(**person)
print(sentence)

print(sentence)

# class instance


class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Jack', '33')

sentence = f"My name is {p1.name} and I am {p1.age} old."
print(sentence)

# for loop and printing single digits with a zero

for i in range(1, 11):
    sentence = 'The value is {:02}'.format(i)
    print(sentence)

# using decimal places
pi = 3.14159265
sentence = 'The value is {:.2f}'.format(pi)
print(sentence)

# make a large number more readable as a comma-separated value
sentence = '1 MB is equal to {:,} bytes'.format(1000**2)
print(sentence)

# printing dates

my_date = datetime.datetime(2025, 6, 17, 12, 30, 45)
print(my_date)  # prints 2025-06-17 12:30:45

# print "June 17, 2025"
sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

# use format "March 01, 2016 fell on a Tuesday and that was the 061 day of the year"
sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(
    my_date)
print(sentence)
