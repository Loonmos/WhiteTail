# define all game characters here
define r = Character("White Tail", color="#e3fffe")
define wt = Character("White Tail", color="#cfcfcf")
define fe = Character("Frost Eyes", color="#e0fffe")
define un = Character("???", color="#ffffff")

define de = Character(" ", color="#6b0000")

label start: # the game starts here
    # play music "rickroll lofi.mp3" loop volume 0.7

    scene burrow

    "This is the introduction to the game."

    "The player gets chosen by the burrow to go out and gather food."

    jump wolf1