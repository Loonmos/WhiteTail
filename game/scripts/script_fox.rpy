define vp = Character("Vulpes Fox", color="#616161")
define wt = Character("White Tail", color="#A0A0A0")

label fox:
    scene snowy_forest with fade
    
    show rabbit at left
    show fox at right

    "Surrounded by dying leaves, their colors mirroring the late fall sunset, you stumble upon a hole in the cold soil."
    "A faintly familiar scent lingers in the air—something you can't quite place."
    "Following it, another scent pulls at your senses."
    "Richer. More nourishing."

    menu:
        "Don't go in":
            wt "This feels dangerous, but it does smell like food... I don't want to go in, but my own burrow is counting on me!"
        
        "Look at burrow":
            "The burrow’s dirt has been overturned around the entrance, more than usual for a rabbit den."
            "You notice small clumps of fur with an auburn glint."
            "Yet your stomach rumbles, and the smell of food guides you toward the entrance."

        "Enter the burrow":
            "You seem determined to go into the burrow no matter what. A brave rabbit isn't afraid!"

    "As you wander in, the smell of cold, overturned soil feels strange. A burrow should be warm, lived in... this one is wrong."
    "The scent of your kind is here, but so is something else. Something weightier. A muskier scent laced with the sharp tang of flesh."
    "Before you can think another thought—a warm, smooth exhale rolls from the darkness behind you."

    vp "(Sly and smoothly) You seem far away from your own neighborhood, little one."

    "White Tail jerks, frozen. A shape stirs in the shadows—deep, golden eyes watching."
    "Slowly, Vulpes uncurls from where he’s been lying, stretching like a lord in his stolen den."

    wt "(Shakily) I-I..."

    vp "Indeed. You—YOU."

    "Vulpes covers the only exit with his fluffy tail. He watches you closely, his eyes narrowing."
    "With a knot in your throat, you try to breathe, but the air feels so thick—it's almost suffocating."

    vp "A little rabbit so deep in the woods... Tell me, did you follow the scent of dinner, or did it lead you here?"

    jump fox_choice1

label fox_choice1:
    menu:
        "Say nothing":
            vp "(Cocky, but lazy, he cuts in and says)"
            vp "Mm. Yes. That’s the trouble with burrows. Leave them unattended, and suddenly someone else is making themselves at home."
            vp "(Chuckles now sitting up with its eyes squinted)"
            vp "Did someone teach you? Break in first, ask questions later—that’s not how it works."
            jump fox_inbetween

        "Apologize":
            wt "I'm sorry for wandering into your burrow."
            vp "Oh? Feeling sorry already, little one? Careful where you roam. Could be worse than a cold, empty den..."
            jump fox_inbetween
        
        "Stand up for self":
            wt "I go wherever I please, fox!"
            vp "(Eyes narrowing, leaning in slightly)"
            vp "Is that so? Grandiose words for a lost little bunny. Let’s see how far that bravado gets you."
            jump bravado1
        
        "Bluff":
            wt "My cousin, Grey Tail, once lived here. What are you doing here?"
            vp "(Chuckles, now sitting up with eyes squinted)"
            vp "Grey Tail, huh? Never heard of them. As far as I'm concerned, you've stumbled into my domain."
            jump fox_inbetween

label fox_inbetween:
    vp "(Leaning in slightly closer, now revealing the auburn color of his fur)"
    vp "But that doesn’t answer my question, little one."
    vp "(Low, smooth) Tell me—what shall we do about this?"
    jump fox_choice2

label fox_choice2:
    menu:
        "Say nothing":
            "White Tail glares deeply at Vulpes, locked into the cunning fox’s eyes, refusing to speak."
            vp "(After a long pause, not grinning anymore but with a coy smile)"
            vp "Oh… I see. You think you can make me bored. But alas, a fox never grows tired of a game of patience."
            "The silence becomes tense, and Vulpes' smile disappears."
            jump tension_scene

        "Ask for help":
            wt "Please, Fox, I didn't mean any harm. You're scaring me, and I'm lost. Can you please help me?"
            vp "Help, huh? What can I, as a fox, do for a lonely, cold little rabbit like you?"
            "He tilts his head, intrigued."
            jump tension_scene
        
        "Negotiate":
            wt "From the scent of it, there's plenty of food in this burrow. But I think you've got more than just me to choose from."
            vp "You're offering a deal? Trying to barter, hmm? Daring little bunny, aren’t you?"
            "Vulpes eyes White Tail carefully."
            vp "Clever. Very clever."
            vp "But cleverness... isn't the same as safety."
            jump negotiation_outcome
        
        "Stand their ground":
            wt "If you think you can scare me, you’re wasting your time. I know how to handle foxes."
            vp "Oh? Do you, now? That makes this much more interesting…"
            jump bravado2

label fox_choice3:
    menu:

label tension_scene:
    # The build-up of tension between White Tail and Vulpes
    "Vulpes' voice is smooth like honey, but with a dangerous undertone. Every word that escapes his mouth feels like a trap."
    "The air seems to grow heavier, thicker with uncertainty as the fox steps forward, closing the distance."
    "You feel the hairs on the back of your neck rise, the stillness amplifying your every movement."
    wt "White Tail remains motionless, heart pounding, eyes scanning for any opening."
    vp "The fox’s grin sharpens, as if savoring the suspense. He doesn't say a word, only watching you closely."
    vp "(After a long moment, Vulpes tilts his head, his voice dripping with amusement.)"
    vp "Well, little rabbit, it seems you’ve run out of tricks. But I don’t mind playing a little longer. You’ve earned this moment, for now."
    wt "(In a steady, calm voice) Not out of tricks yet, fox."
    vp "He chuckles. The silence stretches, the forest's sounds distant, but your pulse is a steady drumbeat in your ears."
    vp "You can’t wait much longer. What will you do?"
    jump fox_choice3

label bravado1:
    "You've shown your utmost courage to the fox! But Vulpes senses your fear."
    "In a swift motion, you try to bolt for the entrance, but like a strike of lightning, the fox pounces at your tail."
    "You're dragged down further into the burrow and killed swiftly with a bite to the neck. Foxes like efficiency."
    jump death_scene1

label bravado2:
    "You've shown your utmost courage to the fox! But Vulpes senses your fear."
    "In a swift motion, you try to bolt for the entrance, but like a strike of lightning, the fox pounces at your tail."
    "You're dragged down further into the burrow and killed swiftly with a bite to the neck. Foxes like efficiency."
    jump death_scene1

label death_scene1:
    hide rabbit
    hide fox
    scene heaven
    "You died..."
    menu:
        "Go back to the last choice":
            jump fox_choice1
        "Go back to the beginning of the chapter":
            jump fox

label death_scene2:
    hide rabbit
    hide fox
    scene heaven
    "You died..."
    menu:
        "Go back to the last choice":
            jump fox_choice2
        "Go back to the beginning of the chapter":
            jump fox

label negotiation_outcome:
    "Vulpes considers the offer."
    "He takes a slow step back, tail curling tighter around the exit."
    vp "Alright, little one. I’ll bite. Show me."
    "If White Tail plays it right, they might just slip away."
    jump fox_choice3

label fox_outcome:
    "Depending on previous choices, White Tail either tricks the fox or gains a dangerous ally."
    "Regardless, Vulpes' golden eyes will always watch the burrow. The fox never forgets a scent."
