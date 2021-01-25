# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

triangle = {
  'a': 0,
  'b': 0,
  'c': 0
}

def identifyTriangle():
  input('Enter the lengths of three side of a triangle [Enter...]')

  triangleType = 'isoceles'

  a = int(input('a: '))
  triangle['a'] = a

  b = int(input('b: '))
  triangle['b'] = b

  c = int(input('c: '))
  triangle['c'] = c
  
  # equalateral check
  if a == b and a == c and b == c:
    triangleType = 'equalateral'

  # scalene check
  if a != b and a != c and b != c:
    triangleType = 'scalene'

  print(f'A triangle with sides of {a}, {b} & {c} is a {triangleType} triangle')

  identifyTriangle()

identifyTriangle()