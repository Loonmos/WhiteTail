
label wolf1:
    scene snowy forest

    show rabbit at left

    "The cold bites at your nose as you sniff the air. It's quiet. Too quiet..."

    wt "{i}I should head back soon. I have wandered a bit too far I think...{/i}"

    wt "{i}I didn't manage to find much, but it's not too bad for a first try right?{/i}"

    "The small bundle of food shifts on your back. Hopefully it's enough to not go hungry tonight."

    play sound "snapping branch.mp3"

    "You freeze. Someone is behind you..."

    "Slowly, you turn your head and you see a pair of pale eyes gleam from the shadows."

    un "Well hello little rabbit, aren't you a bit far from home?"

    show wolf at right

    "A figure steps out of the undergrowth. She looks like a regular wolf, but those eyes... There is only one wolf with blue eyes around here."

    "You recognize her. Many from your burrow have gotten injured or died by her paw."

    wt "{i}Oh no.{/i}"

    "Your heart pounds in your chest. Your legs lock up and you can't do anything but gape up at her."

    "She moves forward, paws barely making a sound against the snow."

    wt "{i}Move! Run!{/i}"

    "But your legs won't listen..."

    fe "You're new, aren't you?"

    "She tilts her head."

    fe "The others don't wander this far. They're too smart for that. But you..."

    fe "No scars, little food and an all consuming fear."

    menu:
        "How should I say?"

        "Who are you?":
            fe "I think you know that very well. It hasn't been that long since I took a bite out of one of your elders..."

        "Please don't hurt me.":
            fe "Don't worry little rabbit, it won't hurt for long..."

        "Come any closer and I'll scream for the others.":
            "The wolf snorts and stalks closer."

    "You see her muscles shift."

    jump wolf1_choice1

label wolf1_choice1:

    menu(time=2, timeout="freeze"):
        "RUN!!!"

        "Run Away":
             jump run_away

label run_away:
    "You bolt. Snow kicks up behind you as your paws hit the ground."

    "The forest blurs around you. You twist and weave through the undergrowth."

    "Faster. {i}Faster.{/i}"

    "The sound of heavy paws thudding behind you sends terror through your limbs."

    "Then... your bundle of food gets caught behind some branches."

    jump wolf1_choice2

label wolf1_choice2:
    
    menu(time=2, timeout="pry"):
        "WHAT DO I DO?"

        "Free yourself":
             jump free

        "Pry the bundle loose":
            "You try to pry it loose from the branch but..."
            jump pry

label free:
    "You manage to shrug it off just in time to dodge her bite."

    "You continue running, but she's close. Too close."

    "And then..."

    "A fallen log with a gap just big enough for you. You throw yourself through it and..."

    "The wolf scratches and bites at the entrance, but she can't reach you."

    fe "You win this time little rabbit."

    "You hear the wolf walk away."

    wt "{i}Is... is she gone?{/i}"

    "You don't dare to go out and check."

    "You stay in the log until the sun starts to set."

    "You peak your head out, nothing to see, and bolt out. Not stopping until the burrow entrance comes into view."

    hide rabbit
    hide wolf

    jump burrow1

label pry:
    fe "Got you."

    "Your neck lights up in pain."

    "Your body gets thrown into the snow and you try to scream... But all that comes out are some gurgles."

    "Your vision blurs. The last thing you see are her pale eyes, glowing in the cold."

    jump death_wolf2

label freeze:
    "You stay rooted in place, unable to bring yourself to move."

    "She moves, fast as the wind."

    "The world spins as you're thrown into the snow. Sharp claws press deep into your chest, creating a growing pool of blood beneath you."

    "Your vision blurs. The last thing you see are her pale eyes, glowing in the cold."

    jump death_wolf1

label death_wolf1:
    hide rabbit
    hide wolf
    scene heaven

    de "You died..."

    menu:
        de "You died..."

        "Go back to the last choice":
            show rabbit at left
            show wolf at right
            scene snowy forest
            jump wolf1_choice1

        "Go back to the beginning of the chapter":
            show rabbit at left
            show wolf at right
            scene snowy forest
            jump wolf1

label death_wolf2:
    hide rabbit
    hide wolf
    scene heaven

    de "You died..."

    menu:
        de "You died..."

        "Go back to the last choice":
            show rabbit at left
            show wolf at right
            scene snowy forest
            jump wolf1_choice2

        "Go back to the beginning of the chapter":
            show rabbit at left
            show wolf at right
            scene snowy forest
            jump wolf1