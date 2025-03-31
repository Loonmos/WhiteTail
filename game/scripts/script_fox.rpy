define vp = Character("Vulpes Fox", color="#616161")
define wt = Character("White Tail", color="#A0A0A0")

label fox:
    scene snowy_forest with fade
    
    show rabbit at left
    show fox at right

    "Surrounded by dying leaves, their colors mirroring the late fall sunset, you stumble upon a hole in the cold soil."
    "A faintly familiar scent lingers in the air-something you can't quite place."
    "Following it, another scent pulls at your senses."
    "Richer. More nourishing."

    menu:
        "Don't go in":
            wt "This feels dangerous, but it does smell like food... I don't want to go in, but my own burrow is counting on me!"
        
        "Look at burrow":
            "The burrow's dirt has been overturned around the entrance, more than usual for a rabbit den."
            "You notice small clumps of fur with an auburn glint."
            "Yet your stomach rumbles, and the smell of food guides you toward the entrance."

        "Enter the burrow":
            "You seem determined to go into the burrow no matter what. A brave rabbit isn't afraid!"

    "As you wander in, the smell of cold, overturned soil feels strange. A burrow should be warm, lived in... this one is wrong."
    "The scent of your kind is here, but so is something else. Something weightier. A muskier scent laced with the sharp tang of flesh."
    "Before you can think another thought-a warm, smooth exhale rolls from the darkness behind you."

    vp "(Sly and smoothly) You seem far away from your own neighborhood, little one."

    "White Tail jerks, frozen. A shape stirs in the shadows-deep, golden eyes watching."
    "Slowly, Vulpes uncurls from where he's been lying, stretching like a lord in his stolen den."

    wt "(Shakily) I-I..."

    vp "Indeed. You-YOU."

    "Vulpes covers the only exit with his fluffy tail. He watches you closely, his eyes narrowing."
    "With a knot in your throat, you try to breathe, but the air feels so thick-it's almost suffocating."

    vp "A little rabbit so deep in the woods... Tell me, did you follow the scent of dinner, or did it lead you here?"

    jump fox_choice1

label fox_choice1:
    menu:
        "Say nothing":
            vp "(Cocky, but lazy, he cuts in and says)"
            vp "Mm. Yes. That's the trouble with burrows. Leave them unattended, and suddenly someone else is making themselves at home."
            vp "(Chuckles now sitting up with its eyes squinted)"
            vp "Did someone teach you? Break in first, ask questions later-that's not how it works."
            jump fox_inbetween

        "Apologize":
            wt "I'm sorry for wandering into your burrow."
            vp "Oh? Feeling sorry already, little one? Careful where you roam. Could be worse than a cold, empty den..."
            jump fox_inbetween
        
        "Stand up for self":
            wt "I go wherever I please, fox!"
            vp "(Eyes narrowing, leaning in slightly)"
            vp "Is that so? Grandiose words for a lost little bunny. Let's see how far that bravado gets you."
            jump bravado1
        
        "Bluff":
            wt "My cousin, Grey Tail, once lived here. What are you doing here?"
            vp "(Chuckles, now sitting up with eyes squinted)"
            vp "Grey Tail, huh? Never heard of them. As far as I'm concerned, you've stumbled into my domain."
            jump fox_inbetween

label fox_inbetween:
    vp "(Leaning in slightly closer, now revealing the auburn color of his fur)"
    vp "But that doesn't answer my question, little one."
    vp "(Low, smooth) Tell me-what shall we do about this?"
    jump fox_choice2

label fox_choice2:
    menu:
        "Say nothing":
            "White Tail glares deeply at Vulpes, locked into the cunning fox's eyes, refusing to speak."
            vp "(After a long pause, not grinning anymore but with a coy smile)"
            vp "Oh... I see. You think you can make me bored. But alas, a fox never grows tired of a game of patience."
            "The silence becomes tense, and Vulpes' smile disappears."
            jump tension_scene

        "Ask for help":
            wt "Please, Fox, I didn't mean any harm. You're scaring me, and I'm lost. Can you please help me?"
            vp "Help, huh? What can I, as a fox, do for a lonely, cold little rabbit like you?"
            "He tilts his head, intrigued."
            jump tension_scene
        
        "Negotiate":
            wt "From the scent of it, there's plenty of food in this burrow. But I think you've got more than just me to choose from."
            vp "You're offering a deal? Trying to barter, hmm? Daring little bunny, aren't you?"
            "Vulpes eyes White Tail carefully."
            vp "Clever. Very clever."
            vp "But cleverness... isn't the same as safety."
            jump negotiation_outcome
        
        "Stand their ground":
            wt "If you think you can scare me, you're wasting your time. I know how to handle foxes."
            vp "Oh? Do you, now? That makes this much more interesting..."
            jump bravado2

label fox_choice3:
     menu:
        "Negotiate with Vulpes (second option)":
            vp "(Leaning in closer, his sharp eyes narrowing as he watches White Tail, a grin slowly spreading across his face.)"
            vp "You're offering a deal? A deal from a rabbit?"
            vp "(He chuckles to himself, as if the idea amuses him.)"
            vp "I have to admit, you've got guts, little one."
            "(Vulpes stretches out, lazily circling the food pile, tapping a paw on a small carrot, picking it up and inspecting it before playfully tossing it from paw to paw.)"
            vp "You're right. There is plenty of food in this burrow, but it's not about the food, is it? You're trying to find a way to save that fluffy little tail of yours."
            vp "(He pauses, giving White Tail a long, calculating stare.)"
            vp "Seems like you're not as scared as I thought... Or maybe you're just really bad at negotiating."
            wt "(His eyes flicker, assessing the situation, but staying composed. He gives a nonchalant shrug.)"
            wt "I'm not scared... Not when I know how to play the game."
            "(White Tail takes a step back, eyeing Vulpes, his gaze flicking to the side, clearly thinking.)"
            wt "But you know, I'm sure there's better prey out there. A nest of possums, for example. Nice and fattened up, not too quick to escape. You wouldn't even have to chase them... You'd be done in a minute, probably less."
            vp "(His ears twitch at the mention of the possums. The idea clearly catches his attention, his tail flicking in thought as he slows down.)"
            vp "A nest of possums, huh?"
            vp "(He licks his lips, tail swishing with interest.)"
            vp "Sounds delicious... and easy."
            vp "(He looks back at White Tail, who is holding her breath, hoping the bluff works.)"
            vp "But how do I know you're not just trying to send me on a wild goose chase?"
            wt "(Grinning slyly, but trying to keep up the act.)"
            wt "Would I lie about such a thing? I'm just a simple rabbit. I don't have anything to gain by sending you off in the wrong direction..."
            wt "(White Tail gives a nonchalant wink and twitches his nose.)"
            wt "You are a fox, after all, and surely you like an easy meal over a stubborn rabbit."
            vp "(After a long pause, he looks like he's about to dismiss the idea, but his curiosity gets the better of him.)"
            vp "Maybe... maybe you're right. An easy meal would be better than wasting time with a stubborn rabbit."
            vp "(Vulpes looks toward the forest, sniffing the air as if trying to track the scent of the possums.)"
            vp "Alright, fine. You've piqued my interest, little bunny. I'll let you go... for now."
            vp "(He begins to stalk off, following the vague direction White Tail pointed toward, already losing interest in the rabbit for the moment.)"
            jump burrow4


        "Take the chance and escape, but...":
            "White Tail thinks she's outsmarted Vulpes, but as she tries to dash out with a small stash of food in her paws, the fox's sharp eyes turn back to her."
            "The chase is on. White Tail runs faster than she ever has before, but Vulpes is swift, and with a few well-placed leaps, the fox catches up."
            vp "White Tail feels a sharp bite at her tail before his world goes black."
            vp "Well... that's the end little bunny rabbit."
            jump death_scene2


label tension_scene:
    # The build-up of tension between White Tail and Vulpes
    "Vulpes' voice is smooth like honey, but with a dangerous undertone. Every word that escapes his mouth feels like a trap."
    "The air seems to grow heavier, thicker with uncertainty as the fox steps forward, closing the distance."
    "You feel the hairs on the back of your neck rise, the stillness amplifying your every movement."
    wt "White Tail remains motionless, heart pounding, eyes scanning for any opening."
    vp "The fox's grin sharpens, as if savoring the suspense. He doesn't say a word, only watching you closely."
    vp "(After a long moment, Vulpes tilts his head, his voice dripping with amusement.)"
    vp "Well, little rabbit, it seems you've run out of tricks. But I don't mind playing a little longer. You've earned this moment, for now."
    wt "(In a steady, calm voice) Not out of tricks yet, fox."
    vp "He chuckles. The silence stretches, the forest's sounds distant, but your pulse is a steady drumbeat in your ears."
    vp "You can't wait much longer. What will you do?"
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
            jump fox_choice3
        "Go back to the beginning of the chapter":
            jump fox

label negotiation_outcome:
    "Vulpes considers the offer."
    "He takes a slow step back, tail curling tighter around the exit."
    vp "Alright, little one. I'll bite. Show me."
    "If White Tail plays it right, they might just slip away."
    jump fox_choice3

# label fox_outcome:
   # "Depending on previous choices, White Tail either tricks the fox or gains a dangerous ally."
    #"Regardless, Vulpes' golden eyes will always watch the burrow. The fox never forgets a scent."
