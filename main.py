import emoji
from emoji import emojize

attempts = 3
answers = ["titanic", "shrek", "toy story", "jurassic park", "godzilla", "jaws", "the martian", "transformers", "terminator", "john wick"]
losing = False

def guess(answer, attempts_left):
    while True: #lives > 0
        attempt = input("The movie is: ")
        if attempt.lower() == answer:
            print("Correct!\n")
            break
        else:
            print("That was incorrect!")
            attempts_left -= 1
            print("Lives Left: " + str(attempts_left))
            print("")
            if attempts_left == 0:
                 print("You lost!")
                 losing = True
                 return losing

def round(round, emojis, is_losing):
    print("Round " + round)
    while not is_losing:
        print(emojis)
        guess(answers[int(round) - 1], attempts)
        if attempts <= 0:
                print("You lost!")
                break
        return attempts

print("Welcome to the movie emoji guesser!")
print("You will be given some emojis and guess what movie it is!")
input("Press Enter to Begin\n")

while True: 
    round("1", emojize(":ice:") + emojize(":motor_boat:") + emojize(":two_hearts:"), losing)
    round("2", emojize(":nauseated_face:") + emojize(":onion:") + emojize(":donkey:") + emojize(":princess:"), losing)
    round("3", emojize(":cowboy_hat_face:") + emojize(":alien:") + emojize(":open_book:"), losing)
    round("4", emojize(":sauropod:") + emojize(":dna:") + emojize(":national_park:"), losing)
    round("5", emojize(":fire:") + emojize(":lizard:")+ emojize(":ogre:"), losing)
    round("6", emojize(":shark:") + emojize(":speedboat:"), losing)
    round("7", emojize(":rocket:") + emojize(":ringed_planet:") + emojize(":potato:") + emojize(":astronaut:"), losing)
    round("8", emojize(":robot:") + emojize(":alien:") + emojize(":automobile:"), losing)
    round("9", emojize(":mechanical_arm:") + emojize(":mechanical_leg:") + emojize(":smiling_face_with_sunglasses:") + emojize(":robot:"), losing)
    round("10", emojize(":dog_face:") + emojize(":person_in_suit_levitating:") + emojize(":water_pistol:"), losing)

    if losing:
         print("You lost!")

print("You won!")