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
    "Things work out best for those who make the best of how things work out.", "The people who are crazy enough to think they can change the world are the ones that do.\n\t-Steve Jobs",
    "Hang in there, buddy.."]

about_computers = ["The trouble with computers, of course, is that they are very sophisticated idiots.",
    "I have bought this wonderful machine- a computer. Now I am rather an authority on gods, so I identified the machine- it seems to me to be an Old Testament god with a lot of rules and no mercy.\n\t-Joseph Campbell",
    "If you don't know anything about computers, just remember that they are machines that do exactly what you tell them but often surprise you in the result. \n\t-Richard Dawkins",
    "On two occasions, I have been asked,\n \"Pray, Mr. Babbage, if you put into the machine wrong figures, will the right answers come out?\"\n...I am not able rightly to apprehend the kind of confusion of ideas that could provoke such a question.\n\t-Charles Babbage",
    "What do such machines really do? They increase the number of things we can do without thinking.\nThings we do without thinking -- there's the real danger.\n\t-Frank Herbert, Dune",
    "Computers are good at following instructions, but not at reading your mind.\n\t-Donald Knuth", "Never underestimate the bandwidth of a station wagon full of tapes hurtling down the highway.\n\t-Andrew Tanenbaum",
    "A computer would deserve to be called intelligent if it could deceive a human into believe that it was human.\n\t-Alan Turing",
    "The danger of computers becoming like humans is not as great as the danger of humans becoming like computers.\n\t-Konrad Zuse",
    "Einstein argued that there must be simplified explanations of nature, because God is not capricious or arbitrary.\nNo such faith comforts the software engineer.\n\t-Fred Brooks",
    "Software engineering is the part of computer science which is too difficult for the computer scientist.\n\t-Friedrich Bauer",
    "Any problem in computer science can be solved with another level of indirection.\n\tDavid Wheeler",
    "Playing with pointers is like playing with fire.\n Fire is perhaps the most important tool known to man.\n Carefully used, fire brings enormous benefits; but when fire gets out of control, disaster strikes.\n\t-John Barnes",
    "The programmer, like the poet, works only slightly removed from pure thought-stuff.\n He builds his castles in the air, from air, creating by exertion of the imagination.\n Few media of creation are so flexible, so easy to polish and rework, \nso readily capable of realizing grand conceptual structures.\n\t-Fred Brooks",
    "And programming computers was so fascinating. You create your own little universe, and then it does what you tell it to do.\n\t-Vint Cerf",
    "Applications programming is a race between software engineers, who strive to produce idiot-proof programs,\n and the universe which strives to produce bigger idiots.\n So far the Universe is winning.\n\t-Rick Cook",
    "Computers are man's attempt at designing a cat: it does whatever it wants, whenever it wants, and rarely ever at the right time.",
    "There is no programming language, no matter how structured, that will prevent programmers from making bad programs.\n\t-Larry Flon",
    "There are two ways of constructing a software design.\n One way is to make it so simple that there are obviously no deficiencies.\n And the other way is to make it so complicated that there are no obvious deficiencies.\n\t-CAR Hoare",
    "One in a million is next Tuesday.", "There are two ways to write error-free programs; only the third one works.", "Software and cathedrals are much the same – first we build them, then we pray.",
    "Real Programmers always confuse Christmas and Halloween because Oct31 == Dec25.", "Testing can only prove the presence of bugs, not their absence.\n\t-Djikstra",
    "A documented bug is not a bug; it is a feature."]




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
    "Language is a ford through the river of time.", "Free at last, free at last. Thank God Almighty, I'm free at last.",
    "If I take the wings of the morning\nand\ndwell in the uttermost parts of the sea.",
    "While you live, shine\nDon't suffer anything at all;\nLife exists only a short while\nAnd time demands its toll.",
    "This be the verse you grave for me:\nHere he lies where he longed to be. Home is the sailor, home from the sea,\nAnd the hunter home from the hill.",
    "EVERYTHING WAS BEAUTIFUL AND NOTHING HURT.", "The last enemy that shall be defeated is death.",
    "Timshel! Thou mayest!", "Since I am so quickly done for\nI wonder what I was begun for?",
    "THE ONLY PROOF HE NEEDED\nFOR THE EXISTENCE OF GOD\nWAS MUSIC", "All living things are brothers, and all dead things are even more so.",
    "I was a victim of a series of accidents, as are we all.", "Busy, busy, busy.\n\tCat's Cradle\n\t\t-Kurt Vonnegut", "So it goes.\n\tSlaughterhouse Five\n\t\tKurt Vonnegut", "Things die. All things die.",
    "We are healthy only to the extent that our ideas are humane.\n\tBreakfast of Champions,\n\t\t-Kurt Vonnegut", "Make me young, make me young, make me young!\n\t-Breakfast of Champions,\n\t\tKurt Vonnegut",
    "If you can do no good, at least do no harm.\n\t-Kurt Vonnegut", "This is my principal objection to life. I think: it is too easy, when alive, to make perfectly horrible mistakes.\n\t-Kurt Vonnegut",
    "Time is liquid. One moment is no more important than any other and all moments quickly run away.\n\t-Kurt Vonnegut",
    "All persons, living and dead, are purely coincidental.\n\t-Kurt Vonnegut", "See you later, alligator.", "Existence is suffering.",
    "[...] the grey rain-curtain turned all to silver glass and was rolled back, and he beheld white shores and beyond them a far green country under a swift sunrise.",
    "Little by little, and also in great leaps, life happened to me.", "In the end, everyone is aware of this:\nnobody keeps any of what he has,\nand life is only a borrowing of bones.",
    "Oh no, not again.", "Call no man happy till he is dead.\n\tAeschylus", "It is not death that a man should fear, but never beginning to live.\n\t-Marcus Aurelius",
    "Our bodies are prisons for our souls.\nOur skin and blood, the iron bars of confinement.\nBut fear not. All flesh decays. Death turns all to ash.\nAnd thus, death frees every soul.\n\t-Darren Aronofsky",
    "Do not stand at my grave and weep.\nI am not there, I do not sleep.\n\t-Mary Elizabeth Frye",
    "So fades a summer cloud away;\nSo sinks the gale when storms are o'er;\nSo gently shuts the the eye of day;\nSo dies a wave along the shore.\n\t-Anna Barbauld",
    "To die would be an awfully big adventure.", "Never the spirit was born, the spirit shall cease to be never.\n Never was time it was not, end and beginning are dreams.\n\t-The Bhagavad Gita",
    "Don't fear the reaper.", "how do you like your blueeyed boy\nMister Death\n\te. e. cummings, \"Buffalo Bill\"",
    "Only the good die young.", "To live in hearts we leave behind is not to die.\n\t-Thomas Campbell",
    "Death is not the end. Death can never be the end.\nDeath is the road. Life is the traveller.\nThe soul is the guide.\n\t-Sri Chinmoy",
    "The lone and level sands stretch far away.\n\t-Percy Bysshe Shelley, \"Ozymandias\"",
    "Rage, rage against the dying of the light.\n\t-Dylan Thomas",
    "How well he fell asleep!\nLike some proud river, widening toward the sea;\nCalmly and grandly, silently and deep,\nLife joined eternity.\n\t-Samual Coleridge",
    "We are going to die, and that makes us the lucky ones.\nMost people are never going to die because they are never going to be born.\n\t-Richard Dawkins",
    "One short sleepe past, wee wake eternally,\nAnd death shall be no more; death, thou shalt die.\n\tJohn Donne",
    "He thought it happier to be dead,\nTo die for Beauty, than live for bread.\n\t-Ralph Waldo Emerson",
    "Life's race well run,\nLife's work well done,\nLife's crown well won,\nNow comes rest.\n\tEpitaph of President James Garfield",
    "And the last long lap is the hardest,\nAnd I shall be dumped where the weed decays,\nAnd the rest is rust and stardust\n\t-Nabokov.",
    "Life is a dream;\nAll dreams must end.", "You will be assimilated.", "Exterminate!", "I am death, not taxes. I only turn up once.\n\tTerry Pratchet, \"Feet of Clay\"",
    "A heap of dust remains of thee;\n'Tis all thou art, and all the proud shall be!\n\t-Alexander Pope", "We're all just stories in the end.",
    "To sleep! perchance to dream -- ay, there's the rub;\nFor in that sleep of death what dreams may come?",
    "Life into death -- life's other shape; no rupture, only crossing.\n\t-Dejan Stojanovic.",
    "Death is nature's way of saying, \"Your table is ready.\"\n\t-Robin Williams",
    "Rejoice for those around you who transform into the Force. Mourn them do not. Miss them do not.",
    "A samurai once asked Zen Master Hakuin where he would go after he died.\nHakuin answered \"How am I supposed to know?\"\n\"How do you know? You're a Zen master!\" exclaimed the samurai.\n\"Yes, but not a dead one\", Hakuin answered.\n\t-Zen koan"
    ]


def complain():
    print("\n***********")
    print(random.choice(lastwords))
    print("***********\n")

def encourage():
    print("\n***********")
    print(random.choice(nicewords))
    print("***********\n")

def talk_about_computers():
    print("\n***********")
    print(random.choice(about_computers))
    print("***********\n")

def main():
    pass


if __name__ == "__main__":
    main()
