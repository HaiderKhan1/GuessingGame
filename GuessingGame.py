from random import randint
rand_int = randint(1,100)
print(f'Random number = {rand_int}')
inputList = []
correctdiff = False
i = 0

while i < 1:
    userInput = int(input('Enter Number'))
    if userInput > 1 and userInput < 100:
        inputList.append(userInput)
        diff = userInput - rand_int
        i +=1
        if diff < 0:
            diff = diff * -1
        if diff < 10:
            print('Warm')
        else:
            print('Cold')
    else:
        print("Out of Bounds")


while (correctdiff == False):
    userInput = int(input("Enter Your Guess: "))
    inputList.append(userInput)
    diff = userInput - rand_int
    if (diff < 0):
        diff = diff * -1

    #check the proximity of the diff #
    if userInput == rand_int:
        print('Nice Job You Guessed Correct')
        correctdiff = True
    elif(abs(inputList[-1] - rand_int) < abs(inputList[-2] - rand_int)) :
        print('Warmer!')
    elif(abs(inputList[-1] - rand_int) > abs(inputList[-2] - rand_int)):
        print('Colder')

print(f'The input List: {inputList}')
totalnum = len(inputList)
print(f'It took you {totalnum} guesses')
