# define all game characters here
define wt = Character("White Tail", color="#cfcfcf")
define op = Character("OnePaw", color="#cfcfcf")
define fe = Character("Frost Eyes", color="#e0fffe")
define un = Character("???", color="#ffffff")
define vp = Character("Vulpes Fox", color="#616161")

define de = Character(" ", color="#6b0000")

label start: # the game starts here
    play music "rickroll lofi.mp3" loop volume 0.7

    scene burrow

    "The sun hangs low in the sky, spilling long shadows across the snowy  forest floor. The air is crisp, cool. The kind that clings to fur and whispers of the coming night."
    "You move carefully beneath the tangle of branches, your ears twitching with every rustle, every distant birdcall."
    "Your paws ache, and your belly gnaws with hunger, but still, you press on."
    

    menu:
        "What do I do?"

        "Keep searching":
            jump KeepSearching1


        "Give up":
            jump Giveup1
    

label KeepSearching1:
        wt "{i} Not yet... I can’t go back yet.{/i}"

        "You pause at the base of a leaning tree, nose twitching as you scan the ground for anything edible, roots, seeds, even the brittle ends of last season’s leaves. "

        "Nothing..."
        jump introend

label Giveup1:
     wt "{i} The others found something, I know they did. Elder Onepaw will not approve if I come back empty handed.{/i}"

     "A cold breeze slips through the trees, stirring the freshly fallen powder snow at your feet."
     "Your shivers, but your jaw tightens with determination. You glance at the sinking sun, eyes narrowing."

     wt "{i}Just a little further. Just a little more… then I’ll go back. Then I can be proud and the others won't be hungry.{/i}"
     jump introend

label introend:
    "You take a breath and move forward again, each step heavier than the last. The forest seems to darken around you, not yet night, but no longer day."
    "Still, you couldn’t turn back. Not without proving you can do this, on your own."

    jump wolf1