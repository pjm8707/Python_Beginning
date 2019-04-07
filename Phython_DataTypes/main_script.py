import sys

print("\npython data types -Numeric")
#create a variable with integer value
a=100
print("The type of variable having value", a, "is", type(a))

print("The maximum interger value", sys.maxsize)
print("The minimum interger value", -sys.maxsize-1)

#create a variable with float value
b=10.2345
print("The type of variable having value", b, "is", type(b))

#create a variable with complex value
c=100+3j
print("The type of variable having value", c, "is", type(c))


print("\npython data type - String")
d="string in a double quote"
e='string in a single quote'
print("The type of variable having value", d, "is", type(d))
print("The type of variable having value", e, "is", type(e))

#using ',' to concatenate the two or several strings
print(d, "concatenated with", e)
print(d+" concatenated with "+e)

print("\npython data typed - List")
#list of having only integer
f=[1,2,3,4,5]
print("list f is:",f)

#list of having only strings
g=["hey", "you", 1,2,3, "go"]
print("list g is:",g)

#index are 0 based. this will prnt a single character
print(g[1]) # this will print "you" in list g

print("\npython data type - Tuple")
#Tuple is another data type which is a sequence of data similar to list. But it is immutable.
#That means data in a tuple is write protected.
#Data in a tuple is wrriten using parenthesis and commas.

#tuple having only integer type of data
h=(1,2,3,4)
print("tuple h is:", h)

#tuple having multiple type of data
i=("hello", 1, 2, 3, "go")
print("tuple i is :", i)

#index of tuples are also 0 based
print("i[4] is ", i[4], "in tuple i")

print("\npython data type - Dictionary")
#Python Dictionary is an unordered sequence of data of key-value pair form.
#It is similar to the hash table type. Dictionaries are written within curly braces in the form key:vale.
#It is very useful to retrive data in an optimized way among large amount of data.

#a sample dictionary variable
j={1:"first name", 2:"second name", "age":3}
print(j[1])
print(j[2])
print(j["age"])











