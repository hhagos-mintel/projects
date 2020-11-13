import random

#variables
answer = False
score = 100
random_number = random.randint(0,10)
print(random_number)
while answer is False and score > 0:
    guess = input('Im thinking of a number. Can you guess?: ').strip()
    diff = int(guess) - random_number

    if diff == 0:
        answer = True
        print(f'Correct! You win! Your score is {score}')
    elif diff == 1 or diff == -1:
        score -= 10
        if score < 0:
            print('Wrong :( you suck. Your score dropped to 0. Try again!')
        else:
            print(f'Youre so close! Your score dropped to {score}. Try again!')
    else:
        score -= 20
        if score < 0:
            print('Wrong :( you suck. Your score dropped to 0. Try again!')
        else:
            print(f'Wrong :( you suck. Your score dropped to {score}. Try again!')
        

if score <= 0:
    print('Womp womp. Your score is 0. You lose.')