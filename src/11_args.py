# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

# YOUR CODE HERE
def f1(i1, i2):
    return i1 + i2

print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and prints the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"
"""
*args : special syntax in function definitions // used to pass a variable number of arguments to a function
"""

# YOUR CODE HERE
def f2(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

"""
def f2(*argv)
    print(argv) # if you print, you will get a tuple containing all of arguments
    return sum(argv)
"""

print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = [7, 6, 5, 4]

# How do you have to modify the f2 call below to make this work?
print(f2(*a))    # Should print 22

"""
unpacking operators (* & **) : unpack the values from iterable objects 
    - * single asterisk : can be used on any iterable
    - ** double asterisk : can only be used on dictionaries
"""

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.

"""
default argument : use assignment (=) operator of the form `keywordname=value`
"""

# YOUR CODE HERE
def f3(num1, num2=1):
    return num1+num2

print(f3(1, 2))  # Should print 3
print(f3(8))     # Should print 9


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".
"""
keyword arguemnt **kways : used to pass a keyworded, variable-length argument list
    can think of the `kwargs` as being a dictionary that maps each keywords to the value that we pass alongside it
    doesn't have an order in which they weere printed out when we iterate over the `kwargs`
When we use keyword arguments
    1. we can often leave out argumetns that have default values
    2. we can rearrange arguments in a way that makes them most readable
    3. we call arguments by their names to make it more clear what they represent
"""
"""
D = {} # dictionary
D.items() -> a set-like object providing a view on D's items
"""
# YOUR CODE HERE
def f4(**kwargs):
    for key, value in kwargs.items():
        print("key: %s, value: %s" %(key, value))
    # print(kwargs) # will print a dictionary {"a": 12, "b": 30}
    # for key in kwargs:
        # print(f"key: {key}, value: {kwargs[key]})

# Should print
# key: a, value: 12
# key: b, value: 30
f4(a=12, b=30)

# Shouldprint
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
f4(city="Berkeley", population=121240, founded="March 23, 1868")

d = {
    "monster": "goblin",
    "hp": 3
}

# How do you have to modify the f4 call below to make this work?
f4(**d)

# print
# key: monster, value: goblin
# key: hp, value: 3