"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# input --> 4 2015 ==> will print out a calendar for April in 2015
# input --> 4 ==> print out April in 2020 (current year)
# input --> none ==> print out April in 2020 (current year, current month)

# in case you don't ask input, just use `sys.argv`
args = sys.argv # it will give a list
# print(args) # will print out like python3 14_cal.py 4 2020 ==> ['14_cal.py', '10', '2020']

inputCal = input('which month and year?: ') # make default current year and current month
print('You typed :', inputCal)

today = datetime.today()
curMon = today.month
curYear = today.year
# print(curMon, curYear)

# if input is empty, use current Mon, Year variable
if len(inputCal) == 0:
    print(calendar.month(curYear, curMon))
# if only 1 input which is month, use currentYear variable
elif len(inputCal) == 1 or len(inputCal) == 2:
    print(calendar.month(curYear, int(inputCal)))
    # REFLECT : add input month is 10, 11, 12
else:
    splited = inputCal.split()
    print(calendar.month(int(splited[1]), int(splited[0])))
    # REFLECT : for 10 2010 ==> slice where the space is

# maybe add error message if a user types somthing else