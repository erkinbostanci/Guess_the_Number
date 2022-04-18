import random
import time

print("""************************
Guess the Number Game

Guess the number between 1 and 1000.
************************""")

rand_num = random.randint(1,1000)
guess_right = 10
while True:

    predict = int(input("Predict number:"))

    if (predict < rand_num):
        print("Information is being queried...")
        time.sleep(1)

        print("Is too low number")

        guess_right -= 1
    elif (predict > rand_num):
        print("Information is being queried...")
        time.sleep(1)

        print("Is too high number")

        guess_right -= 1
    else:
        print("Information is being queried...")
        time.sleep(1)
        print("Congratulations! Our number",rand_num)
        break
    if (guess_right == 0):
        print("Your Guess Is Over...")
        print("Number:",rand_num)
        break