import emoji
from emoji import emojize

lives = 10
answers = ["titanic", "shrek", "toy story", "jurassic park", "godzilla", "jaws", "the martian", "transformers", "terminator", "john wick"]
movies = [emojize(":ice:") + emojize(":motor_boat:") + emojize(":two_hearts:"),
              emojize(":nauseated_face:") + emojize(":onion:") + emojize(":donkey:") + emojize(":princess:"),
              emojize(":cowboy_hat_face:") + emojize(":alien:") + emojize(":open_book:"),
              emojize(":sauropod:") + emojize(":dna:") + emojize(":national_park:"),
              emojize(":fire:") + emojize(":lizard:")+ emojize(":ogre:"),
              emojize(":shark:") + emojize(":speedboat:"),
              emojize(":rocket:") + emojize(":ringed_planet:") + emojize(":potato:") + emojize(":astronaut:"),
              emojize(":robot:") + emojize(":alien:") + emojize(":automobile:"),
              emojize(":mechanical_arm:") + emojize(":mechanical_leg:") + emojize(":smiling_face_with_sunglasses:") + emojize(":robot:"),
              emojize(":dog_face:") + emojize(":person_in_suit_levitating:") + emojize(":water_pistol:")]


print("Welcome to my emoji movie guessing game!")
input("Press Enter to Begin!\n")

if lives > 0:
    for i in range(len(movies)):
        print("Round " + str(i+1))
        print(movies[i])
        while lives > 0:
            guess = input("The movie is: ")
            if guess.lower() == answers[i]:
                print("Correct! \n")
                break
            else:
                lives -= 1
                print("Wrong movie!")
                print(f"You have {lives} lives left.\n")
                continue
        if lives <= 0:
            break

if lives > 0:
    print("\nYou won!")
else:
    print("\nYou lost!")