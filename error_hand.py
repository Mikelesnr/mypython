# error Handling
import datetime
from tokenize import Number

while True:
    try:
        now = datetime.datetime.now().year
        yr_of_birth = int(input("what year were you born?\n"))
        print(f'You are {now - yr_of_birth} years old\n')
    except (ValueError, TypeError):
        print('Please enter a number')
    else:
        print('thank you!')
        break
    # finally:
    #     print('ok, I am finally done')
