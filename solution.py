
#functions from the book for reference

def is_divisible(x, y):
     if x % y == 0:
        return True
     else: 
        return False

#function for is_power for the assignment

def is_power(a, b):
    if a == 1:
        return True
    if b ==1:
        return False
    if not is_divisible(a,b):
        return False
    return is_power(a/b, b)

#testing the script with given commands

print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))

#test to see if my program just says true to evrything or not

print("is_power(10, 3) returns: ", is_power(10, 3))

#i am not sure if this is how i am suppossed to interpret the assignment as the wording is a little cofusing to me
