## ======================== problem 1 ========================================
# Write a procedure, count_words, which takes as input a string
# and returns the number of words in the string. You may consider words
# as strings of characters separated by spaces.

def count_words(s):
    slst = s.split()
    return len(slst) 


passage =("The number of orderings of the 52 cards in a deck of cards "
"is so great that if every one of the almost 7 billion people alive "
"today dealt one ordering of the cards per second, it would take "
"2.5 * 10**40 times the age of the universe to order the cards in every "
"possible way.")
print count_words(passage)


## ===================== Problem 2 ==========================================
print "\n"
# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should 
# return the speed the data travels as a decimal fraction of the speed of
# light.

speed_of_light = 300000. # km per second

def speed_fraction(tracert, distance):
    return  (2.0 * distance / tracert * 1000) / (speed_of_light)



print speed_fraction(50,5000)

print speed_fraction(50,10000)

print speed_fraction(16,20)

## ======================= Problem 3 ======================================
print "\n"
# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(sec):
    
    hours = int(sec) // (60 * 60)
    minutes = (int(sec) - hours * 3600) // 60
    seconds = (sec - hours * 3600) - (minutes * 60)
    
    hours_str = (" hours, ", " hour, ")[hours == 1]
    minutes_str = (" minutes, ", " minute, ")[minutes == 1]
    seconds_str = (" seconds", " second")[seconds == 1]
    return str(hours) + hours_str + str(minutes) + minutes_str + \
           str(seconds) + seconds_str

    
print convert_seconds(3661)

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds

## ===================== explanation =======================================
# (use_when_false, use_when_true)[use_bool_expression_as_index_on_tuple]
# When the variable hours is one, hours==1 is True (but can also be used as
# an integer 1) and "hour, " is printed. If hours==1 is False (bool, but
# also integer 0) then hours, is printed instead.

## ======================= Alternative ==================================
def output(x, name):
    return "%s %s%s" % (str(x), name, "s" if x != 1 else "")

def convert_seconds1(n):
    h, rest = divmod(int(n), 3600)
    m = rest / 60
    return "%s, %s, %s" % (output(h, "hour"), output(m, "minute"), \
                            output(n - (3600 * h + 60 * m), "second"))

## ==================== Problem 4 ======================================
print "\n"
# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def download_time(fileSize, unit1, bandWidth, unit2):
    bits = [["kb", 2 ** 10],["kB", 2 ** 10 * 8],["Mb", 2 ** 20],["MB", 2 ** 20 * 8],["Gb", 2 ** 30],
            ["GB", 2 ** 30 * 8],["Tb", 2 ** 40],["TB", 2 ** 40 * 8]]
    for bit in bits:
        if bit[0] == unit1: fileSize = fileSize * bit[1]
        if bit[0] == unit2: bandWidth = bandWidth * bit[1]
    time = float(fileSize) / bandWidth
    
    return convert_seconds(time)

print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable
