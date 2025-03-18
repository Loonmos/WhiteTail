
define r = Character("White Tail", color="#e3fffe")
define w = Character("Black Paw", color="#9e3939")

define help_wolf = False

label wolf2:
    scene snowy forest

    "You see a Wolf, their leg trapped in a beartrap. They appear to be struggling against the trap, but all it's doing is making the gashes in their leg deeper."

    "Out of curiosity you come a bit closer."

    show rabbit

    r "{i}It's her.{/i}"

    "You stop dead in your tracks. It's the Wolf who chased you not too long ago."

    r "{i}The wolf, she's... caught in a hunters trap.{/i}"

    "As she continues to struggle, you notice something else. Surrounding the Wolf is a small patch of burdock. You could really use that right now."

    "The wind picks up, causing the Wolf to pause and sniff the air. She turns her head towards you and her demeanor quickly changes. She lifts herself up again, chin high and ears pricked forward. But her eyes, wide and filled with pain, betray her."

    show wolf at right
    show rabbit at left

    fe "And so we meet again, little rabbit."

    "The sound of her voice urges you to run, but you don't. Not yet..."

    r "That we do, wolf. Luckily it's not me who is the prey this time."

    "The Wolf looks pained and she sighs."

    fe "I need your help. I... beg of you."

    "Your eyes widen in surprise. But her begging doesn't ease your worries."

    r "Why would I ever help you?"

    fe "You're out late. Haven't found enough food, have you?"

    "You stiffen and say nothing."

    fe "These plants... I obviously don't need them, but you? You look like you could use them."

    r "{i}She is right. I really do need the food if I don't want anyone to go hungry tonight. But...{/i}"

    r "Having some food means little when you'll kill me right after you get out."

    fe "I won't, you wouldn't have to worry about me or my pack. Not this winter. A life for a life."

    r "{i}Not having to worry about wolves would be nice. If she keeps to her promise that is...{/i}"

    r "{i}On the other hand, I still remember that time she chased me and leaving her here might be the end for her...{/i}"

    r "{i}I could really use the food though, the sun is starting to set already and I have nowhere near enough.{/i}"

    fe "We could help each other out here, little one. Help me get out of here and you won't go hungry nor have to worry about wolves again."

    menu:
        "What do I do?"

        "Help the Wolf":
            $ help_wolf = True
            jump wolf_help

        "Leave the Wolf":
            $ help_wolf = False
            jump wolf_leave

label wolf_help:
    r "{i}I need food and I would like to not have to worry about wolves. I will help her out, just this once. I hope she is a wolf of her word...{/i}"

    "Against every instinct you have, you move towards the wolf."

    r "You better stick to your words wolf."

    "The wolf doesn't make a sound as you work on opening the trap. She sighs when she can finally remove her leg."

    "She tests her leg and it gives out under her weight."

    fe "I will, little rabbit. I always keep my promises."

    fe "However, I can't make any guarantees for after this winter. When it's over, you may be wishing you'd let me rot."

    "The wolf stalks off, limping heavily and leaving a bloody trail."

    r "{i}I hope she keeps her promise... But for now, I'm safe and I have enough food to feed myself and the burrow.{/i}"
    
    hide rabbit
    hide wolf

    jump burrow3

label wolf_leave:
    r "{i}No, I shouldn't do this. You can never trust a predator. It's only a matter of time until she gets hungry again and I doubt a hungry wolf cares about promises.{/i}"

    r "{i}I need to be smart and leave her here. Let's hope the hunter will come back soon...{/i}"

    "You take a step back and the Wolf's ears flatten."

    fe "Wait. No! Don't go."

    "She tries to move, causing the trap to tear into her leg again. A fresh burst of blood stains the snow."

    fe "Please! Don't leave me here. I can't get out of this trap by myself."

    "You hesitate for just second and she notices."

    fe "I'll do anything! You-you want more food? I'll gather plants for you! I'll bring you something every night, I swear!"

    "You watch as her chest rises and falls, each breath quicker than the last. Her tail is tucked and her legs tremble."

    r "{i}So even wolves are afraid of death.{/i}"

    "You shake your head and start to move backwards."

    r "I will never trust a predator."

    fe "No! Wait!"

    "As you run off, you can hear the Wolf yell behind you."

    fe "When I get out of here, you are done little rabbit."

    r "{i}If she gets out of there... I might be hungry tonight, but I'm safe and that's the most important.{/i}"

    hide rabbit
    hide wolf

    jump burrow3