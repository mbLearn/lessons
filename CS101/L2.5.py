### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextday(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    
    if day < 30:
        return year, month, day + 1
    elif day == 30 and month < 12:
        return year, month + 1, 1    # day = 1
    else:
        return year + 1, 1, 1        # month = 1 & day = 1

print nextDay(1999, 12, 30)
print nextDay(2013, 1, 30)
print nextDay(2012, 12, 30)


## ======================== Alternative =============================
def nextDay1(year, month, day):
  day = day + 1
  if day>30 and month == 12:
         day = day-30
         month = month -11  
         year = year + 1

  if day > 30 and month < 12:
                day = day-30
                month = month+1
  return year, month, day

print nextDay1(1999, 12, 30)
print nextDay1(2013, 1, 30)
print nextDay1(2012, 12, 30)

# ================== Problem 2 =============================================

        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    days=0
    while (year1, month1, day1) != (year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days= days+1
       # year1=new[0]
       # month1=new[1]
       # day1= new[2]
    return days
    


print daysBetweenDates(2012,9,30,2012,10,30)
print daysBetweenDates(2012,1,1,2013,1,1)
print daysBetweenDates(2012,9,1,2012,9,4)
