import random

#HOW TO USE
#import famouslastwords
#import signal

# def interrupt_handler(signal, frame):
#
#    print("********************Keyboard interrupt detected.**************")
#    print("Exiting...")
#    famouslastwords.complain()
#    sys.exit()

#in main():
# signal.signal(signal.SIGINT, interrupt_handler)

#IF IT NEEDS TO RUN ON AWS:

# do the import like this
# try:
#     import famouslastwords
#     local = True
# except ImportError:
#     local = False

# and run like this
# if local:
#    famouslastwords.complain()







lastwords = ["Goodbye cruel world.", "I go to seek a great perhaps.", "See you around, kid.",
    "How rude.", "All compounded things are subject to vanish. Strive with earnestness.",
    "Tonight we dine in hell!", "Et tu, Brute?", "A dying man can do nothing easy.",
    "Now is not the time for making new enemies.", "Go on, get out! Last words are for fools who haven't said enough!",
    "My wallpaper and I are fighting a duel to the death. One or the other of us has to go.",
    "Swing low, sweet chariot.", "Now I can cross the shifting sands.", "So long and thanks for all the fish.",
    "No comment.", "Aequanimitas.", "Applaud my friends, the comedy is finished.", "May the Force be with you always.",
    "Fly, you fools!", "Fool! No man can kill me.", "I am one with the Force and the Force is with me.",
    "It is a far, far better rest that I go to than I have ever known.", "Fear is the mind-killer.", "The horror! the horror!",
    "I don't want to go.", "Avada kedavra!", "Dobby is happy to be with his friend.", "My God, it's full of stars.",
    "All dogs go to heaven.", "All those moments will be lost in time like tears in the rain. Time to die.", "Rosebud...",
    "To the stars...", "We Are Groot.", "Make death proud to take you.", "I am a leaf on the wind. Watch me soar.",
    "With great power comes great responsibility.", "And the beat goes on.", "That's all, folks!",
    "Against you I will fling myself, unvanquished and unyielding, O Death!",
    "Blessed be the man that spares these stones,\n And cursed be he that moves my bones.",
    "I may be gone, but rock and roll lives on.", "Love Will Tear Us Apart",
    "So we beat on, boats against\n the current, borne back\nceaselessly into the past.",
    "I had a lover's quarrel with the world.", "If life ain't just a joke, then why are we laughing?",
    "Language is a ford through the river of time.", "Free at last, free at last. Thank God Almight, I'm free at last.",
    "If I take the wings of the morning\nand\ndwell in the uttermost parts of the sea.",
    "While you live, shine\nDon't suffer anything at all;\nLife exists only a short while\nAnd time demands its toll.",
    "This be the verse you grave for me:\nHere he lies where he longed to be. Home is the sailor, home from the sea,\nAnd the hunter home from the hill.",
    "EVERYTHING WAS BEAUTIFUL AND NOTHING HURT.", "The last enemy that shall be defeated is death.",
    "Timshel! Thou mayest!", "Since I am so quickly done for\nI wonder what I was begun for?",
    "THE ONLY PROOF HE NEEDED\nFOR THE EXISTENCE OF GOD\nWAS MUSIC", "All living things are brothers, and all dead things are even more so.",
    "I was a victim of a series of accidents, as are we all.", "Busy, busy, busy.", "So it goes.", "Things die. All things die.",
    "We are healthy only to the extent that our ideas are humane.", "Make me young, make me young, make me young!",
    "If you can do no good, at least do no harm.", "This is my principal objection to life. I think: it is too easy, when alive, to make perfectly horrible mistakes.",
    "Time is liquid. One moment is no more important than any other and all moments quickly run away.",
    "All persons, living and dead, are purely coincidental.", "See you later, alligator."]


def complain():
    print("\n***********")
    print(random.choice(lastwords))
    print("***********\n")

def main():
    pass


if __name__ == "__main__":
    main()
