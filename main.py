import emoji
from emoji import emojize

lives = 10
answers = ["titanic", "shrek", "toy story", "jurassic park", "godzilla", "jaws", "the martian", "transformers", "terminator", "john wick"]

def guess(answer, lives):
    while True:
        attempt = input("The movie is: ")
        if attempt.lower() == answer:
            print("Correct!\n")
            break
        else:
            print("That was incorrect!")
            lives -= 1
            print("Lives Left: " + str(lives))
            print("")
            if lives == 0:
                 break

def round(round, emojis):
    print("Round " + round)
    while True:
        print(emojis)
        guess(answers[int(round) - 1], lives)
        if lives == 0:
                print("You lost!")
                break
        break

print("Welcome to the movie emoji guesser!")
print("You will be given some emojis and guess what movie it is!")
input("Press Enter to Begin\n")

round("1", emojize(":ice:") + emojize(":motor_boat:"))
round("2", emojize(":nauseated_face:") + emojize(":onion:") + emojize(":donkey:"))
round("3", emojize(":cowboy_hat_face:") + emojize(":alien:") + emojize(":open_book:"))
round("4", emojize(":t_rex:") + emojize(":sauropod:") + emojize(":dna:") + emojize(":national_park:"))
round("5", emojize(":fire") + emojize(":lizard:") + emojize(":ogre:"))