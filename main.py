import random 
integer = 0
times_looped = 1
def numlist():
  global times_looped
  global integer
  while integer != 500:
    integer = random.randint(0,500)
    print(integer)
    if integer == 500:
      print()
      print("This program looped",times_looped,"times!")
      integer = 500
    elif integer != 500:
      times_looped += 1
numlist() 
