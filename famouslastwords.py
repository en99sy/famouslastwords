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

nicewords = ["Necessity is the mother of invention.", "Genius is 99% perspiration and 1% inspiration.\n\t-Thomas Edison",
    "There is a desire deep within the soul which drives man from the seen to the unseen,\n to philosophy and the divine.\n\t-Kahil Gibran",
    "Inspiration is a slender river of brightness leaping from a vast and eternal knowledge.\n\t-Sri Aurobindo",
    "It's not the size of the dog in the fight, it's the size of the fight in the dog. \n\t-Mark Twain",
    "You miss 100% of the shots you don't take.\n\t-Wayne Gretsky\n\t\tMichael Scott",
    "Between your dreams in the sky and your reality on the ground is your future, your horizon.\n\t-Eric Burns",
    "Inspiration is the windfall from hard work and focus. Muses are too unreliable to keep on the payroll.\n\t-Helen Hanson",
    "A breath of our inspiration\nIs the life of each generation;\nA wondrous thing of our dreaming\nUnearthly, impossible seeming --\nThe soldier, the king, and the peasant\nAre working together in one,\nTil our dream shall become their present,\nAnd their work in the world be done.\n\t-Authur O'Shaughnessy",
    "If you're going through hell, keep on going.", "Fear kills more dreams than failure ever will.",
    "You can't use up creativity. The more you use, the more you have. \n\t-Maya Angelou",
    "Never let go of that fiery sadness called desire.", "What would you do if you weren't afraid?",
    "I think I can, I think I can, I think I can.", "One, remember to look up at the stars and not down at your feet.\nTwo, never give up work. Work gives you meaning and purpose and life is empty without it.\nThree, if you are lucky enough to find love, remember it is there and don't throw it away.\n\t-Stephen Hawking",
    "Innovation distinguishes between a leader and a follower.\n\t-Steve Jobs", "I have not failed.\nI've just found 10,000 ways that won't work.\n\t-Thomas Edison",
    "Do not go where the path may lead;\ngo instead where there is no path and leave a trail.\n\t-Ralph Waldo Emerson",
    "Things work out best for those who make the best of how things work out.", "The people who are crazy enough to think they can change the world are the ones that do.\n\t-Steve Jobs"]





lastwords = ["Goodbye cruel world.", "I go to seek a great perhaps.\n\t-e e cummings", "See you around, kid.",
    "How rude.", "All compounded things are subject to vanish. Strive with earnestness.",
    "Tonight we dine in hell!", "Et tu, Brute?", "A dying man can do nothing easy.",
    "Now is not the time for making new enemies.", "Go on, get out! Last words are for fools who haven't said enough!",
    "My wallpaper and I are fighting a duel to the death. One or the other of us has to go.\n\t-Oscar Wilde",
    "Swing low, sweet chariot.", "Now I can cross the shifting sands.\n\t-Frank Baum", "So long and thanks for all the fish.",
    "No comment.", "Aequanimitas.", "Applaud my friends, the comedy is finished.", "May the Force be with you always.",
    "Fly, you fools!", "Fool! No man can kill me.", "I am one with the Force and the Force is with me.",
    "It is a far, far better rest that I go to than I have ever known.", "Fear is the mind-killer.", "The horror! the horror!",
    "I don't want to go.", "Avada kedavra!", "Dobby is happy to be with his friend.", "My God, it's full of stars.",
    "All dogs go to heaven.", "All those moments will be lost in time like tears in the rain. Time to die.", "Rosebud...",
    "To the stars...", "We Are Groot.", "Make death proud to take us.\n\tAntony&Cleopatra,\n\t\tShakespeare", "I am a leaf on the wind. Watch me soar.",
    "With great power comes great responsibility.", "And the beat goes on.", "That's all, folks!",
    "Against you I will fling myself, unvanquished and unyielding, O Death!\n\t-Virgina Woolfe",
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
    "I was a victim of a series of accidents, as are we all.", "Busy, busy, busy.\n\tCat's Cradle\n\t\t-Kurt Vonnegut", "So it goes.\n\tSlaughterhouse Five\n\t\tKurt Vonnegut", "Things die. All things die.",
    "We are healthy only to the extent that our ideas are humane.\n\tBreakfast of Champions,\n\t\tKurt Vonnegut", "Make me young, make me young, make me young!\n\t-Breakfast of Champions,\n\t\tKurt Vonnegut",
    "If you can do no good, at least do no harm.\n\t-Kurt Vonnegut", "This is my principal objection to life. I think: it is too easy, when alive, to make perfectly horrible mistakes.\n\t-Kurt Vonnegut",
    "Time is liquid. One moment is no more important than any other and all moments quickly run away.\n\t-Kurt Vonnegut",
    "All persons, living and dead, are purely coincidental.\n\t-Kurt Vonnegut", "See you later, alligator.", "Existence is suffering."]


def complain():
    print("\n***********")
    print(random.choice(lastwords))
    print("***********\n")

def encourage():
    print("\n***********")
    print(random.choice(nicewords))
    print("***********\n")

def main():
    pass


if __name__ == "__main__":
    main()
