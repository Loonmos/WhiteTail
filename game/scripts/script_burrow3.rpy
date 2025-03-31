

label burrow3:

     if help_wolf:
         jump burrow3_help
     else:
         jump burrow3_leave

label burrow3_help:
    scene burrow

    show rabbit at left
    show rabbit2 at right

    "The burrow is tense. Whitetail has just returned, her fur still bristling from the encounter."
    "Rabbits whisper among themselves as Elder Onepaw watches her from his usual place, his single front paw tapping against the dirt."
    "His ears are low, his expression unreadable. Until she steps closer, dropping a small pile of food before him."

    op "Hmph. You did bring something back, at least. Perhaps I underestimated you."

    menu:
     "Tell Onepaw about helping the wolf.":
        jump Behonest1
     "Try to lie about it.":
        jump Trylie1

    label Behonest1:
        wt "(Quietly) I didn't get it on my own"

        op "(Ears flicking) Oh? And what exactly, does that mean?"

        wt "(Takes a breath) I helped her. The wolf. She was trapped, and she allowed me to gather some food in that area."

        "Silence. Onepaw stares at her, unblinking, before his good paw clenches slightly "
        jump continueburrow3

    label Trylie1:
        wt "Yes... I... I met the wolf again... but she was trapped and... "
        " And I left her there and she got what she deserved!"

        wt "{i}What am I thinking, that didn't sound convincing at all, He'll see right through me..."

        "A tense moment of silence"
        jump continueburrow3

    label continueburrow3:    
        op "Tell me it isn't true"

        wt "(Steady but wary) I did what I thought was right"

        op "Right..."

        "Onepaw rises slightly, his voice edged with disbelief, perhaps even anger."

        op "I knew you were young, but I did not think you were a fool. You helped her?! The same creature that tore through our kind like dry grass? The same teeth that decommissioned me?!"

        "(Your ears twitch, but you stand firm.)"

        wt "She was trapped. Helpless. I couldn't just..."

        op "(Interupting) Oh, you could have! You should have! You think she would've spared you, given the chance? No. That beast would've swallowed you whole and left your bones to the crows."

        "A silence stretches between them. Your breath is heavy, your paws tense."

        wt "(Softer, but firm) Maybe. But I don't think so. Not this time. I made a choice. Not out of fear, not because I was weak, but because I believe it meant something."

        "Onepaw's nose twitches. His whiskers flick. He exhales sharply, his gaze scrutinizing, searching her face."

        op "You believe?..."

        wt "Yes."

        "For a long moment, he says nothing. Then, with a tired sigh, he eases himself back down, shaking his head."

        op "Belief won't fill our bellies"

        wt "Maybe not. But it might change the future."

        "Onepaw doesn't reply immediately. His good paw presses against the ground, thoughtful."
        "Then, with the smallest, almost imperceptible nod, he looks at her again, not with approval, but with something closer to reluctant trust."

        op "Then I hope, for all our sakes, that you're right."



    hide rabbit
    hide rabbit2

    jump fox

label burrow3_leave:
   scene burrow

   show rabbit at left
   show rabbit2 at right

   "The burrow is quiet. The other rabbits glance at you but do not whisper this time."
   "Onepaw is already watching you as you step inside, his ears turned toward you expectantly."
   "You drop a few meager roots and seeds at his feet, far less than you had hoped to bring back."

   op "Not much..."

   wt "No, I lost time."

   op "(examining you closely) Oh? And what, exactly, took your time?"

   menu:
    "Tell Onepaw about leaving the wolf in the trap":
   
        "You hesitate, then straighten your posture."
   
    wt "I found her. The wolf. She was caught in a poachers trap"

   "Onepaw doesn't move, his gaze sharpening"

   op "And?"

   wt "(Quietly) I left her there..."

   "A long silence. Then Onepaw gives a single satisfied nod"

   op "You left her in that trap"

   wt "(Nods) Yes, I did"

   op"(exhales, slow and deliberate) Good, that's the first wise choice I've seen from you"

   "He studies you, perhaps expecting you to be shaken, to look for approval. But You don't speak. Something lingers in you mind."
   "Words from the wolf, whispered between breaths."

   fe "{i} When I get out of this, I will remember you little rabbit{/i}"

   op "You did right, Whitetail. That creature is nothing but death. The less mercy she sees from us, the better"

   "You nod again,but your paws feel heavy. You remember the way the wolf looked at you. Not pleading, not grateful, but calculating."
   "{i}I have left her there, trapped, to die, haven't I?{/i}"
   "{i}If she gets out... If she meant what she said.../i}"

   "Onepaw is still looking at you, curiously."

   op "You look troubled"

   wt "No... Just tired"

   "Onepaw doesn't question it. He gives another small nod and turns away, satisfied."
   "But as you move deeper into the burrow, you can't shake the weight in you chest. The wolf's voice lingers in your mind, and for the first time, you aren't sure if you made the right choice."


   hide rabbit
   hide rabbit2

   jump fox
