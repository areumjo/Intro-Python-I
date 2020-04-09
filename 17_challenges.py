"""
Exercise 1 : calculation
"""

# 1. How many seconds are there in 21 minutes and 15 seconds?
one = 21 * 60 + 15
print(f"1: {one} seconds")

# 2. How many miles are there in 5 kilometers? # 0.62137119223733 miles in 1 kilometer
two = 0.62 * 5
print(f"2: {two} miles")

# 3. If you run a 5 kilometer race in 21 minutes and 15 seconds, what is your average pace (time per mile in minutes and seconds)?
three = one / two
print(f"3: {three} sec/mile")

# 4. What is your average speed in miles per hour?
# 60 * 60 sec == 1 hour
four = two / (one/3600)
print(f"4: {four} m/h")

# 5. Suppose the cover price of a book is $19.95, but bookstores get a 25% discount. Shipping costs $2.50 for the first copy and $1 for each additional copy. What is the total wholesale cost for 75 copies?
def costCal(numOfBook):
    price = 19.95
    total_price_book = price * numOfBook
    discounted = total_price_book * 0.75
    shipping = 2.50 + (numOfBook - 1) * 1
    return discounted + shipping
    
print(f"5: ${costCal(75)}")


"""
Exercise 2 : function object
"""
def do_twice(arg1, arg2):
    arg1(arg2)
    arg1(arg2)

# def print_spam():
#     print('spam')

def print_twice(arg1):
    print(arg1)
    print(arg1)

# do_twice(print_spam)
# do_twice(print_twice, 'spam')

def do_four(arg1, arg2, arg3):
    arg1(arg2, arg3)

do_four(do_twice, print_twice, 'spam')


"""
Exercise 3 : Fermat’s Last Theorem
a**n + b**n == c**n
"""

def check_fermat(a,b,c,n):
    if n > 2 and (a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

check_fermat(3,4,5,3)

print("Let's check Fermat's theorem : aⁿ + bⁿ = cⁿ")
a = input("Enter a:")
b = input("Enter b:")
c = input("Enter c:")
n = input("Enter n (greater than 2):")

check_fermat(int(a), int(b), int(c), int(n))
