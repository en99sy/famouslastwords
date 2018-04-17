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
    "You miss 100% of the shots you don't take.\n\t-Wayne Gretsky\n\t\t-Michael Scott",
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
    "Hang in there, buddy..", "What doesn't kill you makes you stronger.", "This, too, shall pass.",
    "A fence to wisdom is silence.\n\t-Akiba ben Joseph", "A word after a word after a word is power.\n\t-Margaret Atwood",
    "Hope is like the sun;\nif you only believe in it when you can see it, you'll never make it through the night.", "Hope is the dream of a waking man.\n\t-Aristotle",
    "Everything passes away -- suffering, pain, blood, hunger, pestilence.\nThe sword will pass away too, but the stars will still remain when the shadows of our presence and our deeds have vanished from the earth.\nThere is no man who does not know that. Why, then, will we not turn our eyes towards the stars? Why?\n\t-Mikhail Bulgakov",
    "Until death, all is life.\n(While there's life, there's hope.)\n\t-Miguel de Cervants, Don Quixote",
    "Hope is the thing with feathers--\nThat perches in the soul--\nAnd sings the tune without the words--\nAnd never stops -- at all --\n\t-Emily Dickinson",
    "When we realize the degree of agency we actually do have, we no longer have to \"hope\" at all.\nWe simply do the work.\n\t-Derrick Jensen", "love is the every only god\n\t-e. e. cummings",
    "yes is a pleasant country--\nlove is a deeper season\nthan reason\n\t-e. e. cummings", "--tomorrow is our permanant address\nandthere they'll scarcely find us (if they do,\nwe'll move away still further: into now)\n\t-e. e. cummings",
    "completely dare\nbe beautiful\n\t-e. e. cummings", "lovers alone wear sunlight\n\t-e. e. cummings",
    "my advice to all young people who wish to become poets is:\ndo something easy, like learning how to blow up the world\n\t -- unless you're not only willing, but glad, to feel and work and fight till you die.\nDoes this sound dismal? It isn't.\nIt's the most wonderful life on earth.\nOr so I feel.\n\t-e. e. cummings",
    "Never let the future disturb you.\nYou will meet it, if you have to, with the same weapons of reason which today arm you against the present.\n\t-Marcus Aurelius Antonius",
    "People ask me to predict the future, when all I want to do is prevent it.\nBetter yet, build it. Predicting the future is much too easy, anyway.\nYou look at the people around you, the street you stand on, the visible air you breathe, and predict more of the same.\nTo hell with more. I want better.\n\t-Ray Bradbury",
    "The empires of the future are the empires of the mind.\n\t-Winston Churchill", "I never think of the future. It comes soon enough.\n\t-Albert Einstein",
    "A generation that ignores history has no past -- and no future.\n\t-Robert Heinlein", "Today is only one day in all the days that will ever be.\nHemingway",
    "Our virtures and failings are inseparable, like force and matter.\nWhen they separate, man is no more.\n\t-Nikola Tesla",
    "We live in deeds, not years: in thoughts, not breaths;\nIn feelings, not in figures on a dial.\nWe should count time by heart-throbs. He most lives\nWho thinks most, feels the noblest, acts the best.\n\t-Philip James Bailey",
    "It matters not how long we live, but how.\n\t-Philip James Bailey", "There are more things in heaven and earth, Horatio\nThan are dreamt of in your philosophy.\n\tShakespeare, Hamlet",
    "Since life is but a continuous series of experiences, everything ultimately helps me towards my final enlightenment.\n\t-Sri Chinmoy",
    "In three words I can sum up everything I've learned about life — It goes on.\n\t-Robert Frost", "If you need something to worship, then worship life — all life, every last crawling bit of it! We're all in this beauty together!\n\t-Frank Herbert",
    "Life is what happens to you while you're busy making other plans.", "It is possible to commit no mistakes and still lose. That is not a weakness; that is life.\n\t-Jean-Luc Picard",
    "Life is something that everyone should try at least once.\n\t-Henry J Tillman", "To see a World in a Grain of Sand\nAnd a Heaven in a Wild Flower,\nHold Infinity in the palm of your hand\nAnd Eternity in an hour.\n\t-William Blake",
    "As it once was, so shall it be again\nWorld without end.", "No one's ever really gone.",
    "What is the most important step a man can take?\n\tThe next one.", "He that will not when he may,\nWhen he will he shall have nay.\n\t-Robert Burton",
    "Love is the only thing that we can carry with us when we go, and it makes the end so easy.\n\t-Louisa May Alcott",
    "In dreams and in love there are no impossibilities.\n\t-Janos Arany", "If you never know truth then you never know love.\n\t-The Black Eyed Peas",
    "Duty makes us do things well, but love makes us do them beautifully.\n\tPhillips Brooks"

    ]

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




lastwords = ["Goodbye cruel world.", "I go to seek a great perhaps.\n\t-Rabelais", "See you around, kid.",
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
    "A samurai once asked Zen Master Hakuin where he would go after he died.\nHakuin answered \"How am I supposed to know?\"\n\"How do you know? You're a Zen master!\" exclaimed the samurai.\n\"Yes, but not a dead one\", Hakuin answered.\n\t-Zen koan",
    "There is only one god, and that is Death. What do we say to Death?\nNot today.", "I hope for nothing. I fear nothing. I am free.\n\t-Nikos Kazantzakis",
    "I am moved by fancies that are curled\nAround these images, and cling:\nThe notion of some infinitely gentle\nInfinitely suffering thing.\n\t-TS Eliot",
    "I was neither\nLiving nor dead, and I knew nothing,\nLooking into the heart of light, of silence.\n\t-TS Eliot, \"The Waste Land\"",
    "Of death's twilight kingdom\nThe hope only\nOf empty men.\n\t-TS Eliot, \"The Hollow Men\"", "This is the way the world ends\nThis is the way the world ends\nThis is the way the world ends\nNot with a bang but a whimper.\n\t-TS Eliot, \"The Hollow Men\"",
    "And the wind shall say: \"Here were decent godless people:\nTheir onlyl moument the asphalt road\nAnd a thousand lost golf balls.\"\n\t-TS Eliot, \"The Rock\"",
    "life's not a paragraph\nAnd death i think is no parenthesis\n\t-e. e. cummings", "Time's a strange fellow;\nmore he gives than takes\n(and he takes all)\n\t-e. e. cummings",
    "unbeingdead isn't beingalive\n\t-e. e. cummings", "Hell is other people.\n\t-Sartre",
    "It is time, love, to break off that sombre rose,\nshut up the stars and bury the ash in the earth;\nand, in the rising of the light, wake with those who awoke\nor go on in the dream, reaching the other shore of the sea which has no other shore\n\t-Pablo Neruda, \"The Watersong Ends\"",
    "Because I could not stop for Death --\nHe kindly stopped for me --\n\t-Emily Dickinson", "And then a Plank in Reason, broke,\nAnd I dropped down, and down--\nAnd hit a World, at every plunge,\nAnd Finished knowing -- then --\n\t-Emily Dickinson",
    "Still ending, and beginning still.\n\t-William Cowper", "Life is a jest; and all things show it.\nI thought so once; and now I know it.\n\t-John Gay's epitaph",
    "Let all live as they would die.\n\t-George Herbert", "Death is certain, life is not.\n\t-Augustus Hill",
    "I came like Water, and like Wind I go.\n\t-Omar Khayyam", "Death is chemical.",
    "The Lives\nWe try to make never seem to get\nUs anywhere but Dead.\n\t-Soundgarden", "Life is but a dream.",
    "No one is anyone, one single immortal man is all men.\nLike Cornelius Agrippa, I am god, I am hero, I am philosopher, I am demon and I am world,\nwhich is a tedious way of saying that I do not exist.\n\t-Jorge Luis Borges"
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
