
define pay_crows = False

label crows:
    scene burrowoutsideup with fade

    show rabbit entrance
    
    "A single bird caws in the distance, waking you up from your uncomfortable sleep."
    "After yesterdays encounter you're still shaken, but perhaps even more from OnePaws lecture."
    wt "{i}I can't dissapoint him, no, the whole burrow again...{/i}"
    "You head out into the misty forest while the rest have not awoken yet. But still, you must push on."
    
    scene forestlightup with fade

    show rabbit forest mid with dissolve

    "As a cold breeze winds through the forest, the last remaining leaves on the trees have started to come loose. It is a misty day, grey clouds loom overhead and a few rays of dim sunlight peek through the canopy."
    "You've already spent an multiple hours looking through the snow, finding just a small amount of dead leaves."
    "Your gaze was locked to the ground, not even noticing a change of scenery around you."
    "The thickly grown part of the forest has thinned out, leaving many open spaces and smaller bushes. In the distance you notice an opening in the trees."
    wt "{i}Have I gone too far? This area feels unfamiliar, but I've barely gathered anything...{/i}"
    "With that thought, your nose suddenly twitches. A faint, sweet smell ahead of you."

    scene meadowflowersup with fade

    show rabbit meadow left with dissolve

    "You sprint to the opening, and encounter a large open meadow. Though it has snowed over, it seems to not be as thick here. Small purple and yellow flowers peek through the thin layer."
    wt "{i}Flowers! Thank the forest, finally something! How come no one has come here before?{/i}"
    
    menu:
        "{i}I'm really hungry... should I eat one now?{/i}"

        "Eat one":
            jump eat

        "Take all of them home":
            jump take

label eat:
    show rabbit meadow right with dissolve

    "You dashs to the flowers, immediately eating a single one."
    wt "{i}If I hadn't, i might not even make it back home. It's okay, right?{/i}"
    jump collecting

label take:
   wt "{i}No, I can't... this might be our only chance, I'll just have to hold off untill i'm back.{/i}"

   show rabbit meadow right with dissolve

   jump collecting

label collecting:
    #show rabbit meadow left
    "You rummage through the tall grass, looking for the colourful flowers that stick out."
    wt "{i}These will be perfect for my little siblings. They love the sweet taste.{/i}"

    scene meadownoflowersup with dissolve
    show rabbit meadow right

    "The mist starts growing thicker, and the sunlight is already dissapearing. With as many as she can fit in her bag, you head back."

    "Suddenly, shadows sweep overhead. You quickly try to duck in the grass"
    wt "{i}What?! Please, not now!{/i}"
    
    #show crow2 meadow right
    c2 "Long ears!"
    #hide crow2

    hide rabbit with dissolve
    show rabbitflip meadow right with dissolve

    #show crow3 meadow right 
    c3 "Snow flake!"
    #hide crow3
    #show crow4 meadow right
    c4 "Thief..."
    #hide crow4

    "The cawing of multiple crows surrounds you, landing on the branches on the rim of the forest."
    #show crow2 meadow right
    c2 "Come out, come out!"
    #hide crow2
    #show crow3 meadow right 
    c3 "I heard something move."
    #hide crow3
    #show crow4 meadow right
    c4 "We can smell you, you know.."
    #hide crow4

    "The three crows swoop down, almost planting their beaks in the dirt."
    show crow2 meadow with dissolve
    show crow4 meadow with dissolve
    show crow3 meadow with dissolve
    
    "They hop over sparatically."

    wt "{i}What the hell do they want from me? They're in the way of where I need to go!{/i}"

    hide crow2 with dissolve
    hide crow4 with dissolve
    hide crow3 with dissolve
    
    menu:
        "The crows are coming closer. What will you do?"

        "Stay down":
            jump stay

        "Run the other direction":
            jump run

label stay:
   "You lower your body, trying to look as small as possible."
   "The three crows search through the grass, noticing flowers have been plucked."
   show crow2 meadow 
   c2 "Petals plucked.."
   hide crow2 meadow 
   show crow3 meadow 
   c3 "Our orchard..!!"
   hide crow3
   show crow4 meadow 
   c4 "Like I said... a thief is here."
   hide crow4
   show crow3 meadow 
   c3 "Wait, a flower is left here!"
   hide crow3

   "He starts picking at a white fluffy flower, which isn't a flower at all."
   wt "Ow!"
   show crow2 meadow 
   c2 "Here, here!"
   hide crow2
   show crow3 meadow 
   c3 "An imposter!"
   hide crow3
   show crow4 meadow 
   c4 "Thief! Thief!"

   "They caw and screech as they surround you."
   hide crow4
   "A deep, scratchy voice calls from above."
   show crow1 meadow 
   c1 "My kin, behave."

   "With a flap of his wing, a large crow up in the trees shuts the others up."
   hide crow1
   jump negotiate

label run:
    "You sprint away from the crows, but also away from the path home."
    show crow2 meadow 
    c2 "There she goes!"
    hide crow2
    "You don't make it far across the meadow when a black mass drops before you."
    "A crow, much larger than the others stands in front, looking down with a glint in his eyes."

    jump negotiate


label negotiate:
    "The large crow is decorated, a necklace made of sparkling stones, shells and... are those bones?"
    show crow1 meadow 
    c1 "Heed not, small one."
    c1 "What do you seek here?"

    menu: 
     
       "I'm just passing through. My burrow is nearby" :
           c1 "Passing through our orchard?"
           c1 "I don't recall a rabbits burrow in the vicinity..."

       "Just looking for food." :
           c1 "Aren't we all?"
           c1 "And what makes you think you're allowed these flowers?"
       "Say nothing" :
           "Not talkative, are you?"

    wt "Just let me go. I-I need to get home."
    hide crow1
    show crow2 meadow 
    c2 "Liar, liar!"
    hide crow2
    show crow3 meadow 
    c3 "She's an enemy of our Murder!"
    hide crow3
    show crow4 meadow 
    c4 "Don't you dare disrespect our Lord Shadewing!"
    hide crow4
    show crow1 meadow 
    c1 "Calm yourselves. Can't you see, it can barely think for itself. Take some pity on it."
    c1 "Though, don't think the Murder will let you run off..."
    c1 "What is your name?"

    menu: 
      
       "Whitetail." :
           c1 "How adorable!"
           c1 "Well then, little Whitetail. Call me Shadewing. What will you offer to the murder?"

       "Onepaw. (lie)" :
           c1 "The famed one who escaped Frosteyes? You?"
           wt "I've encountered her and lived."
           c1 "Well then, brave OnePaw. Call me Shadewing. What will you offer to the murder?"

    hide crow1
    show crow2
    c2 "Shiny! Something pretty!"
    hide crow2
    show crow3 meadow 
    c3 "Can we have her eyes? Or maybe that fluffy tail?"
    hide crow3
    show crow4 meadow 
    c4 "How about you retun what you stole..."
    hide crow4

    menu:
        "What do I do?"

        "Give the Crows your food":
            $ pay_crows = True
            jump crows_pay

        "Ignore the Crows request":
            $ pay_crows = False
            jump crows_ignore

label crows_pay:
    "You drop the flowers on the ground."
    wt "Damn it!"

    "The three crows hurry to the flowers, while Shadewing stays still."
    "They hurry to lace the flowers into his necklace, after putting one on themselves."

    "They leave a single flower. While distracted, you notice an opening to escape."
    menu: 

           "Run":
              "You make a run for it, back to the burrow."
              show crow1 meadow 
              c1 "Forgetting something?"
              wt "What??"
              "He flies over and drops the last flower in front of you."
              hide crow1

           "Take flower":
              show crow1 meadow 
              "While distracted, you take the last flower lying there."
              "Shadewing notices."
              c1 "Greedy aren't you? But fine, that one's petals have a faded colour. Would look horrible."
              hide crow1
         
    show crow1 meadow       
    c1 "Those who pay the Murder will be rewarded. Beware, little Whitetail. Blue-eyed and red-coated beasts grow hungrier, just like you."
    hide crow1
    "As the sun sets, you dash back to the burrow, arriving later than you were supposed to."
    hide rabbit
    hide crow1

    jump burrow2

label crows_ignore:
    wt "You don't even eat flowers! I'm leaving!"
    show crow2 meadow 
    c2 "Thief..!!"
    hide crow3
    show crow3 meadow 
    c3 "Fleeing after this?"
    hide crow3

    show crow1 meadow 
    c1 "It seems you don't realise your position..."
    c1 "Disrespect the murder, and you won't be rid of us easily."
    "He takes a good look at your face."
    c1 "Your skull would look great on my necklace..."
    hide crow1
    "The crows suddenly sweep towards you, their claws stretched out."

    menu(time=3, timeout="freeze2"):
        "{color=#9c3730}RUN!!!{/color}"

        "Jump away":
            jump jump_over

label jump_over:
     "The crows knock into eachother, giving you a slight amount of time to make a run for it."
     show crow2 meadow 
     c2 "Coward! Coward!"
     hide crow2
     show crow3 meadow 
     c3 "I'll remember you, Grey.. foot or something?!"
     hide crow3
     show crow4 meadow 
     c4 "You've made yourselves an enemy of the Murder..."
     hide crow4
     "You run back as fast as you can, holding on to quite a lot of flowers."
     "A succes, maybe? Though you don't notice the trail of black feathers just behind you..."
     hide rabbit
     jump burrow2

label freeze2:
    "The crows' claws dig in your eyes."

    jump death_crows

label death_crows:
    scene heaven with fade

    menu:
        "You died..."

        "Go back to the last choice":
            scene meadownoflowersup with fade
            show rabbit meadow left
            
            jump jump_over

        "Go back to the beginning of the chapter":
            jump crows