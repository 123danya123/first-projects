import random
print("H A N G M A N")
wins = 0
loses = 0


def game():
    global wins, loses
    keywords = "python", "java", "swift", "javascript"
    keyword = random.choice(keywords)
    hidden_word = list("-" * len(keyword))
    used_letters = set()
    attempts = 8
    while attempts > 0:

        if "".join(hidden_word) == keyword:
            print(f"You guessed the word {keyword}!")
            print("You survived!")
            wins += 1
            menu()
        print(f'\n{"".join(hidden_word)}')
        guess = input("Input a letter: ")
        try:
            if len(guess) > 1 or guess == "":
                print("Please, input a single letter.")
                continue
            elif not guess.islower():
                print("Please, enter a lowercase letter from the English alphabet.")
                continue
        except AttributeError:
            continue
        if guess in used_letters:
            print("You've already guessed this letter.")
            continue
        used_letters.add(guess)
        for index, val in enumerate(keyword):
            if guess in val:
                hidden_word[index] = val
        if guess not in keyword:
            attempts -= 1
            print("That letter doesn't appear in the word.")
    loses += 1
    print("You lost!")


def menu():
    a = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if a == "play":
        game()
        menu()
    elif a == "results":
        print(f'You won: {wins} times.')
        print(f'You lost: {loses} times.')
        menu()
    elif a == "exit":
        exit()
    else:
        menu()


menu()
