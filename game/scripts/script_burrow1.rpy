

label burrow1:
    scene burrow

    show rabbit at left
    show rabbit2 at right

    "The burrow is dimly lit, warmed by the presence of its inhabitants."
    "Whitetail stands near the entrance, your fur bristling with cold, paws empty."
    "Across from you, Onepaw sits hunched, ears flicking as he eyes your return with measured doubt."

    op "Ah. Back at last, are you?"

    wt "(Your ears flatten, voice defensive)"
    wt "I tried"

    op "Chuckles, dry and humorless"
    op "Oh, I've no doubt you tried, Whitetail. The forest is full of fools who tried and are trying each day."
    op "The difference is in who comes back with something, and who comes back with excuses"

    wt "(Quietly,hesitant)"
    wt "It wasn't an excuse. I... I ran into..."
    wt "her..."

    "The burrow falls silent. A few of the nearby rabbits shift uneasily. Onepaw's expression darkens."

    op "(Low voice) Her..."

    wt "I had no choice, I had to run, or I wouldn't have come back at all"

    "Onepaw's good paw clenches slightly. His torn ear twitches."

    op "(Snorts)"
    op "Hmph. So you ran. And she let you..."

    menu:
        "Agree":
            jump agree1
        "Disagree":
            jump disagree1
    
    label disagree1:
        wt "I.. No! She was hunting me! I barely got away..."
        op "(Shakes his head, scoffs)"
        op "If she wanted you, you'd be in her belly Whitetail. She doesn't let her pray go, not unless she means to. She won't forget you."
        "You stare at him, unsure. Onepaw leans forward slightly, his gaze sharp and cold."

    label agree1:
        wt "Yes, I'm sorry Onepaw"
        "Onepaw looks at you for a second, relaxing a bit"
        

    op "I know her. I know her patience. The way she plays with us, lets us run, lets us think we've won, just so she can take more from us later."
    op "She took my paw, yes. But before that? She took my trust."
    op "And now you stand before me, bright-eyed and empty-pawed, telling me you met her and walked away." 
    op "(Chuckles bitterly)" 
    op "So tell me, Whitetail, did she take something from you today? Or did she just let you go?"

    wt "I... I don't know"

    op "(Tilts his head, unimpressed)"
    op "Hmph. That's a problem, then. Because if you don't know what she took, then maybe she took more than you think."

    "The burrow feels smaller now, the weight of Onepaw's words pressing down on Whitetail."
    "The elder watches you, a glint of something unreadable in his gaze-pity, skepticism, or maybe just cold understanding."
    
    op "(Scoffs and turns away)"
    op "First day out, and already you've lost. I only wonder what it cost the rest of us."

    hide rabbit
    hide rabbit2

    jump crows