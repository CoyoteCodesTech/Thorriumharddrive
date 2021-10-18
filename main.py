import random 
integer = 0
times_run = 1
def numlist():
  global times_run
  global integer
  while integer != 500:
    integer = random.randint(0,500)
    print(integer)
    if integer == 500:
      print()
      print("This program looped",times_run,"times!")
      integer = 500
      break
    elif integer != 500:
      times_run += 1
numlist() 
