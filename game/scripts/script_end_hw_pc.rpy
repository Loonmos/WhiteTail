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

    "They're pounding on the barricades, snarling and trying to get in."

    "Then- a loud BANG and the barricade cracks, dust and debris filling the air."

    "They continue their barrage and more cracks and holes start to form."

    menu:
        "What do you do?"

        "Move to the front to fend off the fox":
            "You move towards the front and the other rabbits look at you with respect."

            wt "{i}I have to protect my burrow. Maybe I can hold off the fox long enough for them to escape.{/i}"

            "A final snap and the barricade breaks. The fox lunges in and begins their attack."

            return

        "Move to back to stay a bit safer":
            "You move towards the back and elder Onepaw shoots you a disgusted glance."

            wt "{i}I don't want to die today. Maybe I can somehow make it out.{/i}"

            "A final snap and the barricade breaks. The fox lunges in and begins their attack."

            return

label other_burrow:
    wt "We have to go now! I found an abandoned burrow yesterday where we can hole up."

    "The rest of the burrow looks at you with newfound hope and elder Onepaw looks at you proudly."

    wt "Gather what you can and follow me."

    "Everyone moves out but you have to be careful. Going to fast might make obvious tracks, but going to slow and the fox might find you."

    "As you travel, you instruct the others to gather sticks and stones. By the time you get to the other burrow, you've gathered enough to make some fortifications."

    jump fortify