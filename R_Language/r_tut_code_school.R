## 1 -- to repeat a value 3 times, 
##	  you would call the rep function and provide its times argument:

rep("Yo ho ho!", times = 3)

##2 -- help(functionname) brings up help for the given function. 
##	 Try displaying help for the sum function:

#help(sum)

##3 -- example(functionname) brings up examples of usage for 
## 	 the given function. Try displaying examples for the min function:

#example(min)

##4 -- You can list the files in the current directory from within R, 
##  	 by calling the list.files function. Try it now:

list.files()

##5 -- To run a script, pass a string with its name to the source function.
source("example.R")

## ---------------------------------------------------------------------- ##

## Vectors ##
##1 A vector's values can be numbers, strings, logical values, or any other type,
##  as long as they're all the same type.
##  The c function (c is short for Combine) creates a new vector by -
##  combining a list of values.
## Vectors cannot hold values with different modes (types).
c(4,7,8)

##2 Sequence Vector ##
##  If you need a vector with a sequence of numbers you can create it with 
##  start:end notation. Let's make a vector with values from 5 through 9:
5:9

seq(5,9)

## seq also allows you to use increments other than 1. 
seq(5, 9, 0.5)

## Reverse order
seq(9,5)

##3 Vector Access
##1 You can retrieve an individual value within a vector by providing 
## its numeric index in square brackets.
sentence <- c("walk", "the", "plank")
sentence[3]

##2 You can assign new values within an existing vector.
sentence[3] <- "dog"

##3 Add new values onto the end, the vector will grow to accommodate them.
sentence[4] <- "to"

##4 You can use a vector within the square brackets to access multiple values. 
##  Try getting the first and third words:
sentence[c(1,3)]

##5 This means you can retrieve ranges of values too.
sentence[2:4]

##6 You can also set ranges of values; 
##  just provide the values in a vector. Add words 5 through 7:
sentence[5:7] <- c('the', 'pop', 'culture')

##7 You can assign names to a vector's elements by passing a second vector 
##  filled with names to the names assignment function, like this:
ranks <- 1:3
names(ranks) <- c("first", "second", "third")

##8 You can also use the names to access the vector's values.
ranks
ranks["first"]

##9 Now set the current value for the "third" rank to 
#   a different value using the name rather than the position.

ranks["third"] <- 4
ranks

#### 4  Plotting One Vector ###
##1 The barplot function draws a bar chart with a vector's values. 
##  We'll make a new vector for you, and store it in the vesselsSunk variable.

vesselsSunk <- c(4, 5, 1)
barplot(vesselsSunk)

##2 If you assign names to the vector's values, R will use those 
#   names as labels on the bar plot.

names(vesselsSunk) <- c("English", "Spanish", "Hindi")
barplot(vesselsSunk)

##3 Now, try calling barplot on a vector of integers ranging from 1 through 20:
barplot(1:20)

#### 5 Vector Math ###
##1 If you add a scalar (a single value) to a vector, the scalar will be added 
    to each value in the vector, returning a new vector with the results.
a <- c(1,2,3)
a
a + 10

