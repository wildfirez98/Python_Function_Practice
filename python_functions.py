# 1.) Write a Python function called max_num()to find the maximum of three numbers.

def max_num(num1, num2, num3):
    return max([num1, num2, num3]) # Use Python max() Function: https://www.w3schools.com/python/ref_func_max.asp

print(max_num(5,10,15))

# 2.) Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(num_list):
    if len(num_list) == 0: # If nothing is in the list, return 0
        return 0
    number = num_list[0] # Number starts with the first number in the list

    if len(num_list) > 1: # If there are numbers in the list
        for i in num_list[1:]: # Iterate thru the numbers and multiply them together
            number = number * i

    return number        

print(mult_list([5, 10, 15]))

# 3.) Write a Python function called rev_string() to reverse a string.

def rev_string(text):
    return(text[::-1])

print(rev_string("Hello, my name is James"))


# 4.) Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(start, stop, step): 
    return start in range(stop, step+1) # Range Function: https://www.w3schools.com/python/ref_func_range.asp 

print(num_within(10, 5, 15))


# 5. Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together. 

triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)


pascal(1)
pascal(3)
pascal(5)