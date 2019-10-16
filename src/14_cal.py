"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
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
"""

import sys
import calendar
from datetime import datetime

today = datetime.now()
today_year = today.year
today_month = today.month

def view_calender(_, month = today_month, year = today_year):
  try:
    month = int(month)
    year = int(year)
    if month in range(1, 13):
      return calendar.month(year, month)
    return 'Invalid Input. Expected -> filename.py month(1-12) year'
  except ValueError as e:
    return 'Please Check input: filename(string) month(int) year(int)'

if __name__ == "__main__":
  arguments = sys.argv
  print(view_calender(*arguments))
