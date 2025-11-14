tuple1 = ("green", "red", "blue") # Create a tuple
print(tuple1)

tuple2 = tuple([7, 1, 2, 23, 4, 5]) # Create a tuple from a list
print(tuple2)

print("length is", len(tuple2)) # Use function len
print("max is", max(tuple2)) # Use max
print("min is", min(tuple2)) # Use min
print("sum is", sum(tuple2)) # Use sum

print("The first element is", tuple2[0]) # Use indexer

tuple3 = tuple1 + tuple2 # Combine 2 tuples
print(tuple3)

tuple3 = 2 * tuple1 # Multiple a tuple
print(tuple3)

print(tuple2[2 : 4]) # Slicing operator exclusief 4 dus 2 en 3
print(tuple1[-1]) #negatieve index => vanachter beginnen tellen 

print(2 in tuple2) # in operator , checkt of waarde 2 in tuple 2 zit => true or false

for v in tuple1: #doorloopr elk element 
    print(v, end = " ") #print ze naast elkaar ipv onder mekaar met spatie 
print() #uitvoer; green red blue
    
#tuple => lijst => sorteren => terug tuple (je kan geen tuples sorteren)
list1 = list(tuple2) # Obtain a list from a tuple 
list1.sort()
tuple4 = tuple(list1)
tuple5 = tuple(list1)
print(tuple4)
print(tuple4 == tuple5) # Compare two tuples, 2 tuples zijn gelijk als zedezemfde lengte en zelfde elementen op zelfde positie hebben 
