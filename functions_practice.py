# A function named hello() that prints a greeting to the user. 
#This function should accept no arguments and returns nothing.

def hello():
  print("Hello Welcome!")
  
# A function named pack() that accepts three arguments, and 
#returns a single list with the three arguments inside as list elements.

def pack(item1, item2, item3,item4):
    return [item1, item2, item3, item4]
  
# A function called eat_lunch(). This function should accept a list of any length, and
# print out a series of strings that say "First I eat __" 
# (the first element of the list), and "Next I eat ___" (for the following elements in the list).
# If the list is empty, print "My lunchbox is empty!". 
# The function should not return anything.

def eat_lunch(foodList):
  if len(foodList) == 0:
    print("My lunchbox is empty!")
  else:
    for index in range(len(foodList)):
      if index == 0:
        print(f"First I eat {foodList[0]}")
      else:
        print(f"Next I eat {foodList[index]}")

# Call hello() function

hello() # Output: Hello Welcome!

# Call pack() function

packed_items = pack("sandwich", "apple", "chips","Milk")
print(packed_items)  # Output: ['sandwich', 'apple', 'chips', 'Milk']

# Call eat_lunch() function

eat_lunch([]) # Output: My lunchbox is empty!
eat_lunch(["sandwich", "apple", "chips","Milk"]) 
# Output: First I eat sandwich
#Next I eat apple
#Next I eat chips
#Next I eat Milk
