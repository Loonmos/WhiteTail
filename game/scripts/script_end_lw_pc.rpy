# this is the ending in which you help the wolf and pay the crows

label end_lw_pc:

    "The sun is starting to set, casting its long shadows across the forest floor."

    "You've been out here for a while now and your bundle is filled with food."

    wt "{i}I'm finally getting the hang of this.{/i}"
    
    # cawing sounds

    "Then, a loud caw rings out above you, followed by three more."

    "You look up. It's that murder of crows you encountered before."

    "They circle down and land in front of you."

    "(idk how the crow personalities work, but here they tell you whats up. maybe add a dialogue choice: say you wont give them more food or hear them out first.)"

    wt "{i}Oh no oh no oh no{/i}"

    wt "{i}I have to get back now!{/i}"

    "You take off in the direction of the burrow, your heart pounding in your chest."

    wt "{i}I hope I won't be too late.{/i}"

    "You went pretty far from the burrow and your legs are starting to tire."

    menu:
        "What do you do?"

        "Keep going":
            wt "{i}No I cannot slow down.{/i}"

            wt "{i}I need to be there as fast as possible.{/i}"

            "You arrive at the burrow, completely out of breath. The other rabbits look at you in alarm."

            jump arrive_at_burrow2

        "Go slower":
            wt "{i}I won't have any use if I collapse before I even get back.{/i}"

            wt "{i}Let's keep up a light jog.{/i}"

            "You arrive at the burrow. The other rabbits look happy when they see your filled bundle."

            jump arrive_at_burrow2

label arrive_at_burrow2:
    wt "The fox and the wolf! They're coming!"

    "Panic quickly spreads through the burrow. Some rabbits look ready to flee, some run to the entrance to look outside, others run towards the children."

    "Nobody really knows what to do and nobody is stepping up to give direction."

    jump other_burrow2

label other_burrow2:
    wt "We have to go now! I found an abandoned burrow yesterday where we can hole up."

    "The rest of the burrow looks at you with newfound hope and elder Onepaw looks at you proudly."

    wt "Gather what you can and follow me."

    "Everyone moves out but you have to be careful. Going to fast might make obvious tracks, but going to slow and the fox might find you."

    "As you travel, you instruct the others to gather sticks and stones. Just in case the fox manages to track you down."

    "By the time you get to the other burrow, you've gathered enough to make some fortifications."

    jump fortify2

label fortify2:
    "After a while, one of the other rabbits shouts in alarm: The fox has been spotted..."

    "Everyone runs inside and groups together. The air is tense, the barricade isn't perfect and everyone hopes it will hold up."

    "The children hide behind their parents and siblings and even elder Onepaw can't stop the tremble in his legs."

    "You wait..."

    "And you wait..."

    "Until the the sunlight starts to creep through the small gaps of the barricade."

    wt "{i}Did we survive?{/i}"

    jump fox_wolf

label fox_wolf:
    "A couple hours ago..."

    "The snow falls in gentle flakes, covering the burrow's entrance in a fresh white layer."

    "Red fur emerges from the tree line."

    "The Fox moves cautiously as he approaches the burrow. He sniffs once. Twice. A growl rumbles in his throat."

    vp "No scent... Where are they?"

    "He steps forward, brushing the snow away with his paw. Nothing. The den is empty."

    "A heavier set of mismatched steps follows. The Wolf emerges from the shadows, her blue eyes narrowing. But something is wrong, her stance is uneven."

    "As she steps into the pale light, the reason becomes clear. One of her front legs is gone, chewed off just above the joint. The wound is still red and raw, evident that it only just closed."

    "She circles the burrow, sniffing. Her tail flicks once before she turns a sharp gaze on the fox."

    fe "Where are they {i}Fox{/i}?"

    vp "I don't know- I swear. They were supposed to be here."

    "The Wolf slowly stalks towards the Fox."

    fe "You 'supposed' they'd be here?"

    vp "No- no. The crows told me! You know the crows don't lie."
    
    "The Wolf starts to growl."

    fe "And you trust those scheming bastards?!"

    "The fox' ears flatten, but he quickly regains his composure, flashing a sly grin."

    vp "Well someone lied, but it wasn't me. Maybe the rabbits caught wind of the plan."

    "The Wolf tilts her head, watching him carefully. Her muscles coil, poised to strike at the slightest provocation."

    fe "Or maybe you tricked me again, Vulpes."

    vp "Oh, please. Don't be like that. You wound me."

    "He places a paw on his chest as if deeply offended, but his eyes remain sharp, calculating."

    "The Wolf is not amused."

    fe "Tell me, Fox, how many times have I fallen for your silver tongue?"

    "Vulpes chuckles, taking a step back."

    vp "Oh, don't be dramatic. What would I possibly gain from deceiving you?"

    "The Wolf's lip curls into a sadistic grin."

    fe "Last time, it cost me a meal. This time, it won't."

    "The Fox' eyes widen slightly. He moves to speak, but the Wolf is faster."

    "She lunges and Vulpes barely dodges it."

    "He pivots, his tail fanning out as he tries to sidestep her next move. The Wolf shifts to follow, but the sudden movement causes her wound to re-open"

    "A sharp jolt of pain ripples through her body"

    "The Wolf falters and lets out a pained grunt."

    "The Fox' sharp eyes flicker with realization."

    "He moves faster now, taking advantage of the opportunity. In a blur of red fur and flashing teeth, he twists, aiming for her neck."

    "But pain is hardly something that stops the Wolf."

    "Her snarl is vicious and before the Fox can sink his teeth in, she counters. Using her momentum, she swings her weight into him, driving her shoulder against his ribs. He stumbles, thrown off balance."

    "She recovers first."

    "He lets out a gurgled breath. And then... silence."

    "The Wolf steps back, the blood from her muzzle dripping onto the fresh snow. She exhales, the cold air turning her breath into mist."

    "Then, she picks up the Fox and disappears into the trees."

    "She won't be going hungry tonight."

    return