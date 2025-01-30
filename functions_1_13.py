import random
number_i_think = random.randint(1,20)
x = str(input("Hello! What is your name?"))
print(f"Well, {x}, I am thinking of a number between 1 and 20.")
y = int(input("Take a guess."))
i = 0
while number_i_think != y:
    i+=1
    if number_i_think > y:
        print("Your guess is too low.")
        y = int(input("Take a guess."))
        continue
    else: 
        print("Your guess is too high.")
        y = int(input("Take a guess."))
        continue
if number_i_think == y:
    print(f"Good job, {x} You guessed my number in {i} guesses!") 



