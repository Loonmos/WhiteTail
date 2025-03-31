# this is the ending in which you help the wolf and pay the crows

label end_hw_pc:
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

            jump arrive_at_burrow

        "Go slower":
            wt "{i}I won't have any use if I collapse before I even get back.{/i}"

            wt "{i}Let's keep up a light jog.{/i}"

            "You arrive at the burrow. The other rabbits look happy when they see your filled bundle."

            jump arrive_at_burrow

label arrive_at_burrow:
    wt "The fox! The fox is coming!"

    "Panic quickly spreads through the burrow. Some rabbits look ready to flee, some run to the entrance to look outside, others run towards the children."

    "Nobody really knows what to do and nobody is stepping up to give direction."

    menu:
        "What do you do?"

        "Gather everyone's attention":
            wt "Everyone listen to me!"

            "The rabbits stop what they're doing and turn their heads towards you."

            menu:
                "What's your plan?"

                "Fortify your home":
                    wt "We can't run from a predator again."

                    wt "Let's stand our ground and protect our home."

                    "The others nod. They are determined, but the fear is evident in their eyes."

                    "You and the others gather sticks, stones and anything else that can help reinforce the burrow's entrance."

                    jump fortify

                "Flee to the abandoned burrow":
                    jump other_burrow

        "Wait for someone to take the lead":
            "You look around, waiting for someone to take the lead."

            "You see elder Onepaw and he looks at you in disappointment."

            "(Onepaw gathers everyone's attention and tells them to fortify the burrow.)"

            "The other rabbits agree, but you can feel the fear in the air."

            "You and the others gather sticks, stones and anything else that can help reinforce the burrow's entrance."

            jump fortify

label fortify:
    "After a while, one of the other rabbits shouts in alarm: The fox has been spotted..."

    "Everyone runs inside and groups together. The air is tense, the barricade isn't perfect and everyone hopes it will hold up."

    "The children hide behind their parents and siblings and even elder Onepaw can't stop the tremble in his legs."

    "You wait... And then-"

    # thumping sounds

    "The fox is here."

    "He's pounding on the barricades, snarling and trying to get in."

    "Then- a loud BANG and the barricade cracks, dust and debris filling the air."

    "He continues his barrage and more cracks and holes start to form."

    menu:
        "What do you do?"

        "Move to the front to fend off the fox":
            "You move towards the front and the other rabbits look at you with respect."

            wt "{i}I have to protect my burrow. Maybe I can hold off the fox long enough for them to escape.{/i}"

            "A final snap and the barricade breaks. The fox lunges in and begins his attack."

            jump fox_attack

        "Move to back to stay a bit safer":
            "You move towards the back and elder Onepaw shoots you a disgusted glance."

            wt "{i}I don't want to die today. Maybe I can somehow make it out.{/i}"

            "A final snap and the barricade breaks. The fox lunges in and begins his attack."

            jump fox_attack

label other_burrow:
    wt "We have to go now! I found an abandoned burrow yesterday where we can hole up."

    "The rest of the burrow looks at you with newfound hope and elder Onepaw looks at you proudly."

    wt "Gather what you can and follow me."

    "Everyone moves out but you have to be careful. Going to fast might make obvious tracks, but going to slow and the fox might find you."

    "As you travel, you instruct the others to gather sticks and stones. Just in case the fox manages to track you down."

    "By the time you get to the other burrow, you've gathered enough to make some fortifications."

    jump fortify

label fox_attack:
    "Sharp teeth and faster than any rabbit can react. One is caught, another barely escapes. Panic erupts in the burrow."

    "Then- before the fox can strike again, another sound cuts through the air."
    "A low, deep growl. A shadow moves from the treeline."
    hide fox
    "The pale-eyed wolf"
    hide rabbit
    show wolf at right
    show fox at left
    "She bursts forward, teeth flashing in the dim light, slamming into the fox before it can claim another life."
    "A vicious fight follows, snarls, snapping jaws, a tangle of fur and claws"
    hide fox
    "And then- Silence..."
    "The wolf stands there, breathing hard, blood on her muzzle."
    "Not hers."
    "She turns to You, those sharp eyes locking onto yours."
    "The fox had been fast, cunning, hunting the young ones with sharp eyes and sharper teeth. But the wolf had been faster."
    "Now, the clearing is still, except for the ragged breath in your chest and the smell of blood in the air."
    "The fox lies in a heap, throat torn, its clever eyes staring at nothing."
    "The wolf licks the blood from her muzzle, then turns to you."
    show rabbit at left
    show wolf at right
    fe "Consider my debt paid, little rabbit."

    "She steps forward, lowering her head slightly so that only Whitetail can hear her next words"
    fe "(low, warning tone) Watch your back next time you leave this place. There are worse things than foxes in these woods."

    menu:
    #show rabbit at left
        "How do you respond?"

        "You saved us... Why?":
            fe "(snorts, glancing at the fox's body) I owed you. And I pay my debts."
            "She steps over the fox's corpse, her tail flicking as she moves away."
            fe "But don't think this means I'll always be there. Next time, you might have to fight for yourself."
        "This doesn't make us even!":
            "The wolf stops, ear twitching. Then she laughs, a low, dangerous sound."
            fe "Oh? And what do you think I owe you, little rabbit? A pack at your back? A safe life?"
            "She steps closer, her eyes gleaming"
            fe "You helped me. I helped you. You want more than that? Then next time, be useful."
            "She turns, padding away without waiting for an answer."
        "I understand, thank you":
            "The wolf studies you for a moment, then nods."
            fe "Good. You learn fast."
            "She steps back, looking toward the trees."
            fe "Keep learning. Keep surviving. If you do... maybe we'll meet again."
            "Then, without another word, she melts into the underbrush."
        "Say nothing":
           "The wolf lingers for a moment, tilting her head as if expecting something. But you stay quiet."
           fe " (softly, almost to herself) Hmm... Rabbits..."
           "Then, with a final glance at the fox's body, she disappears into the woods."

    hide wolf
    hide rabbit

    return