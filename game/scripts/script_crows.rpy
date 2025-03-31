define c1 = Character("Crow 1", color="#616161")
define c2 = Character("Crow 2", color="#616161")
define c3 = Character("Crow 3", color="#616161")
define c4 = Character("Crow 4", color="#616161")

define pay_crows = False

label crows:
    scene burrowoutside

    show rabbit at left
    

    "A single bird caws in the distance, waking you up from your uncomfortable sleep."
    "After yesterday you're still shaken from that encounter, but perhaps even more from OnePaws lecture."
    wt "I can't dissapoint him, no, the whole burrow again..."
    "You head out into the misty forest while the rest have not awoken yet. But still, you must push on."
    
    scene forestlight

    show rabbit at left

    "As a cold breeze winds through the forest, the last remaining leaves on the trees have started to come loose. It was a misty day, grey clouds loomed overhead with a few rays of dim sunlight peek through the canopy."
    "You've already spent an multiple hours looking through the snow, finding just a small amount of dead leaves. Your gaze was locked to the ground, not even noticing a change of scenery around you."
    "The thickly grown part of the forest has thinned out, leaving many open spaces and smaller bushes. In the distance you notice an opening in the trees."
    wt "Have I gone too far? This area feels unfamiliar, but I've barely gathered anyhting..."
    "With that thought, your nose suddenly twitches. A faint, sweet smell ahead of you."
    "You sprint to the opening, and encounter a large open meadow. Though it has snowed over, it seems to not be as thick here. Small purple and yellow flowers peek through the thin layer."
    wt "Flowers! Thank the forest, finally something! How come no one has come here before?"
    "She dashes to the flowers, immediately eating a single one."
    wt "Surely they won't mind me eating one, otherwise I won't make it back home..."
    "Having recovered some energy, you start plucking the other flowers."
    wt "These will be perfect for my little siblings. They love the sweet taste."
    "The mist started growing thicker, and the sunlight was already dissapearing. With as many as she can fit in her mouth, she starts heading back."

    "Suddenly, shadows sweep overhead"
    wt "What?! Please, not now!"
    
    show crow at right

    c2 "Long ears!"
    c3 ""


    menu:
        "What do I do?"

        "Give the Crows your food":
            $ pay_crows = True
            jump crows_pay

        "Ignore the Crows request":
            $ pay_crows = False
            jump crows_ignore

label crows_pay:

    "You pay the crows, yippie."

    hide rabbit
    hide crow

    jump burrow2

label crows_ignore:

    "You don't pay the crows, uh oh."

    hide rabbit
    hide crow

    jump burrow2