define c1 = Character("Crow 1", color="#616161")
define c2 = Character("Crow 2", color="#616161")
define c3 = Character("Crow 3", color="#616161")
define c4 = Character("Crow 4", color="#616161")

define pay_crows = False

label crows:
    scene burrow

    show rabbit at left
    
    "A single bird caws in the distance, waking you up from your uncomfortable sleep."
    "After yesterday you're still shaken from that encounter, but perhaps even more from OnePaws lecture."
    wt "I can't dissapoint him, no, the whole burrow again..."
    "You head out into the misty forest while the rest have not awoken yet. But still, you must push on."
    
    scene snowy forest

    show rabbit at left

    "As a cold breeze winds through the forest, the last remaining leaves on the trees have started to come loose. It was a misty day, grey clouds loomed overhead with a few rays of dim sunlight peek through the canopy."
    "You've already spent an multiple hours looking through the snow, finding just a small amount of dead leaves. Your gaze was locked to the ground, not even noticing a change of scenery around you."
    "The thickly grown part of the forest has thinned out, leaving many open spaces and smaller bushes. In the distance you notice an opening in the trees."
    wt "Have I gone too far? This area feels unfamiliar, but I've barely gathered anyhting..."
    "With that thought, your nose suddenly twitches. A faint, sweet smell ahead of you."
    "You sprint to the opening, and encounter a large open meadow. Though it has snowed over, it seems to not be as thick here. Small purple and yellow flowers peek through the thin layer."
    wt "Flowers! Thank the forest, finally something! How come no one has come here before?"
    
    menu:
        "I'm really hungry... should I eat one now?"

        "Eat one":
            $ eat = True
            jump eat

        "Take all of them home":
            $ take = False
            jump take

label eat:

   "She dashes to the flowers, immediately eating a single one."
   wt "If I hadn't, i might not even make it back home. It's okay, right?"
   jump collecting

label take:
   wt "No, I can't... this might be our only chance, I'll just have to hold off til im back."
  
   jump collecting

   

label collecting:
    show rabbit at right
    "You rummage through the tall grass, looking for the colourful flowers that stick out."
    wt "These will be perfect for my little siblings. They love the sweet taste."
    "The mist started growing thicker, and the sunlight was already dissapearing. With as many as she can fit in her mouth, you heading back."

    "Suddenly, shadows sweep overhead. You quickly try to duck in the grass"
    wt "(What?! Please, not now!)"
    
    show Crow 2 at left
    show Crow 3 at left
    show Crow 4 at left 

    c2 "Long ears!"
    c3 "Snow flake!"
    c4 "Thief..."

    "The cawing of multiple crows surrounds you, landing on the branches on the rim of the forest."

    c2 "Come out, come out!"
    c3 "I heard something move."
    c4 "We can smell you, you know.."

    "The three crows swoop down, almost planting their beaks in the dirt."
    "They hop over sparatically."

    wt "(What the hell do they want from me? They're in the way of where I need to go!)"
    
    menu:
        "The crows are coming closer. What will you do?"

        "Stay down":
            $ stay = True
            jump stay

        "Run the other direction":
            $ run = False
            jump run

label stay:
   "You lower your body, trying to look as small as possible."
   "The three crows search through the grass, noticing flowers have been plucked."
   c2 "Petals plucked.."
   c3 "Our orchard..!!"
   c4 "Like I said... a thief is here."
   c1 "Wait, a flower is left here!"

   "He starts picking at a white fluffy flower, which isn't a flower at all."
   wt "Ow-"

   c2 "Here, here!"
   c3 "An imposter!"
   c4 "Thief! Thief!"
   "They caw and screech as they surround you."

   "A deep, scratchy voice calls from above."
   c1 "My kin, behave."

   "With a flap of his wing, a large crow up in the trees shuts the others up."

   jump negotiate

label run:
  
    "You sprint away from the crows, but also away from the path home."

    c2 "There she goes!"

    "You don't make it far across the meadow when a black mass drops before you."
    "A crow, much larger than the others stands in front, looking down with a glint in his eyes."


    jump negotiate


label negotiate:
    "The large crow was decorated, a necklace made of sparkling stones, shells and... are those bones?"

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

    c2 "Liar, liar!"
    c3 "She's an enemy of our Murder!"
    c4 "Don't you dare disrespect our Lord Shadewing!"

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


    c2 "Shiny! Something pretty!"
    c3 "Can we have her eyes? Or maybe that fluffy tail?"
    c4 "How about you retun what you stole..."


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
              c1 "Forgetting something?"
              wt "What??"
              "He flies over and drops the last flower in front of you."

           "Take flower":
              "While distracted, you take the last flower lying there."
              "Shadewing notices."
              c1 "Greedy aren't you? But fine, that one's petals have a faded colour. Would look horrible."
         
           
    c1 "Those who pay the Murder will be rewarded. Beware, little Whitetail. Blue-eyed and red-coated beasts grow hungrier, just like you."

    "As the sun sets, you dash back to the burrow, arriving later than you were supposed to."
    hide rabbit
    hide crow

    jump burrow2

label crows_ignore:

    wt "You don't even eat flowers! I'm leaving!"
    c2 "Thief..!!"
    c3 "Fleeing after this?"

    c1 "It seems you don't realise your position..."
    c1 "Disrespect the murder, and you won't be rid of us easily."
    "He takes a good look at your face."
    c1 "Your skull would look great on my necklace..."

    "The crows suddenly sweep towards you, their claws stretched out."

    menu(time=3, timeout="freeze2"):
        "{color=#9c3730}RUN!!!{/color}"

        "Jump away":
            jump jump_over

label jump_over:
     "The crows knock into eachother, giving you a slight amount of time to make a run for it."
     c2 "Coward! Coward!"
     c3 "I'll remember you, Grey.. foot or something?!"
     c4 "You've made yourselves an enemy of the Murder..."
     "You run back as fast as you can, holding on to quite a lot of flowers."
     "A succes, maybe? Though you don't notice the trail of black feathers just behind you..."
     hide rabbit
     hide crow
     jump burrow2
    


label freeze2:
    "The crows' claws dig in your eyes."
    return

    