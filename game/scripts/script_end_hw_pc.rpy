# this is the ending in which you help the wolf and pay the crows

define stepped_up = False

label end_hw_pc:
    scene forestlightup with fade
    "The sun is starting to set, casting its long shadows across the forest floor."

    "You've been out here for a while now and your bundle is filled with food."

    show rabbit forest mid with dissolve

    wt "{i}I'm finally getting the hang of this.{/i}"
    
    # cawing sounds

    "Then, a loud caw rings out above you, followed by three more."

    "You look up. It's that murder of crows you encountered before."

    "They circle down and land in front of you."

    show crow1 forest with dissolve
    show crow2 forest with dissolve
    show crow3 forest with dissolve
    show crow4 forest with dissolve

    c2 "Well well.."
    c3 "Hee hee!"
    c4 "Found you."

    wt "Again!?"

    c1 "It's been a while, little flower."

    
    wt "W-what do you want from me now?"

    
    c1 "Haven't you realised?"
    c2 "Slow!"
    c3 "Stupid!"

    "The three laugh and cackle, before being shut up by Shadewing"
    c1 "Calm yourself."
    c1 "Anyways, you might be curious as to why we're here?"

    wt "I won't let you take anything from me, not this time!" 
        

    c1 "Hasn't this rabbit grown quite capable? Perhaps you could one day serve us."
    c1 "No, we don't need anything from you anymore. At least for now..."

    c2 "We fly"
    c4 "We listen"
    c3 "We see..."
    c1 "Something, or someone is on the move."
    c1 "The Murder may not murder, but we are the eyes of the forest. We know what's coming."
    c2 "A flash of red!"
    c3 "Narrow, yellow eyes"
    c4 "Mad with hunger"
    c1 "Coming for..."
    
    "{i} The Burrow..!{/i}"

    wt "No... no..."
    "Whitetail dashes, making a run for it the other direction. She doesn't even look back at the crows, who cackle and smirk."
    c2 "Go, go!"
    c3 "Run, run!"
    c4 "Maybe you'll make it, maybe not..."

    hide crow1 forest with dissolve
    hide crow2 forest with dissolve
    hide crow3 forest with dissolve
    hide crow4 forest with dissolve

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
    scene burrowinsideup with fade
    show onepaw burrow right
    show softpaw burrow left
    show rabbit burrow left with dissolve

    wt "The fox! The fox is coming!"

    "Panic quickly spreads through the burrow. Some rabbits look ready to flee, some run to the entrance to look outside, others run towards the children."

    "Nobody really knows what to do and nobody is stepping up to give direction."

    menu:
        "What do you do?"

        "Gather everyone's attention":
            # move whitetail

            $ stepped_up = True

            wt "Everyone listen to me!"

            "The rabbits stop what they're doing and turn their heads towards you."

            menu:
                "What's your plan?"

                "Fortify your home":
                    wt "We can't run from a predator again."

                    wt "Let's stand our ground and protect our home."

                    "The others nod. They are determined, but the fear is evident in their eyes."

                    hide rabbit with dissolve
                    hide softpaw with dissolve
                    hide onepaw with dissolve

                    "You and the others gather sticks, stones and anything else that can help reinforce the burrow's entrance."

                    jump fortify

                "Flee to the abandoned burrow":
                    jump other_burrow

        "Wait for someone to take the lead":
            "You look around, waiting for someone to take the lead."

            "You see elder Onepaw and he looks at you in disappointment."

            "He stands tall and with a loud voice he shouts:"
            "Alright everyone, if you all listen to me we'll all survive this."
            "Gather everything lying around and barricade the burrow!"

            "The other rabbits agree, but you can feel the fear in the air."

            scene burrowoutsideup with fade

            "You and the others gather sticks, stones and anything else that can help reinforce the burrow's entrance."

            jump fortify

label fortify:
    "After a while, one of the other rabbits shouts in alarm: The fox has been spotted..."

    scene burrowinsideup with fade
    show rabbit burrow left
    show softpaw burrow left
    show onepawflip burrow right

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
            show rabbit burrow front with dissolve
            "You move towards the front and the other rabbits look at you with respect."

            wt "{i}I have to protect my burrow. Maybe I can hold off the fox long enough for them to escape.{/i}"

            "A final snap and the barricade breaks. The fox lunges in and begins his attack."

            jump fox_attack

        "Move to back to stay a bit safer":
            show rabbit burrow back with dissolve
            "You move towards the back and elder Onepaw shoots you a disgusted glance."

            wt "{i}I don't want to die today. Maybe I can somehow make it out.{/i}"

            "A final snap and the barricade breaks. The fox lunges in and begins his attack."

            jump fox_attack

label other_burrow:
    wt "We have to go now! I found an abandoned burrow yesterday where we can hole up."

    "The rest of the burrow looks at you with newfound hope and elder Onepaw looks at you proudly."

    wt "Gather what you can and follow me."

    scene forestlightup with fade
    show rabbit forest left with dissolve
    show softpaw forest mid with dissolve
    show onepaw forest right with dissolve

    "Everyone moves out but you have to be careful. Going to fast might make obvious tracks, but going to slow and the fox might find you."

    "As you travel, you instruct the others to gather sticks and stones. Just in case the fox manages to track you down."

    scene burrowoutsideup with fade

    "By the time you get to the other burrow, you've gathered enough to make some fortifications."

    jump fortify

label fox_attack:
    scene burrowoutsideup with fade
    show fox entrance right with dissolve
    "Sharp teeth and faster than any rabbit can react. One is caught, another barely escapes. Panic erupts in the burrow."

    "Then- before the fox can strike again, another sound cuts through the air."
    "A low, deep growl. A shadow moves from the treeline."
    hide fox
    "The pale-eyed wolf"
    hide rabbit
    show wolf entrance right with dissolve
    show fox entrance left with dissolve
    "She bursts forward, teeth flashing in the dim light, slamming into the fox before it can claim another life."
    "A vicious fight follows, snarls, snapping jaws, a tangle of fur and claws"
    hide fox
    "And then- Silence..."
    "The wolf stands there, breathing hard, blood on her muzzle."
    "Not hers."
    "She turns to you, those sharp eyes locking onto yours."
    "The fox had been fast, cunning, hunting the young ones with sharp eyes and sharper teeth. But the wolf had been faster."
    "Now, the clearing is still, except for the ragged breath in your chest and the smell of blood in the air."
    "The fox lies in a heap, throat torn, its clever eyes staring at nothing."
    "The wolf licks the blood from her muzzle, then turns to you."
    show rabbit entrance left with dissolve
    show wolf entrance right with dissolve
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

    jump ending_hw_pc

label ending_hw_pc:
    #scene burrowinsideup with fade
    #show rabbit burrow left
    #show softpaw burrow left
    #show onepaw burrow right

    #"And the rabbits lived happily ever after or smt"

    return