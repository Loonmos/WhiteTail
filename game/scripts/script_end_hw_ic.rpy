# this is the ending in which you help the wolf and pay the crows

label end_hw_ic:
    scene burrowinside
    show rabbit burrow left

    "The burrow is quiet. The usual rustling of leaves and distant chirping of birds fill the air. Whitetail is among her fellow rabbits, settling into the rhythm of daily life."
    "A sharp cry splits the air. You run outside and see the fox. The scent of blood follows."

    scene burrowoutside
    show fox entrance right

    "Before any of the rabbits outside can flee, it strikes."
    "Sharp teeth, faster than any rabbit can react. One is caught, another barely escapes. Panic erupts in the warren."

    menu (time=3, timeout="Freeze"):
         "What do you do"

         "Run for cover":
            "You dodge into the nearest burrow entrance. And try to hide."
            jump Freeze
         "Warn the others":
            "You shout a warning but it get's lost in the chaos"
            jump Freeze
         "Throw something":
            "In a desperate attempt to distract the fox and help a fellow rabbit escape, you throw a small rock and hit the fox on his nose"
            "The fox exclaims a small yelp and drops the rabbit it had just caught in its jaws, but it's focus is now on you"
            jump Freeze

    label Freeze:
      "Panic takes over, leaving you motionless as the chaos unfolds."

    "Before the fox can strike again, another sound cuts through the air."
    "a low, deep growl. A shadow moves from the treeline."
    hide fox
    "The wolf"
    hide rabbit
    show wolf entrance right
    show fox entrance left
    "She bursts forward, teeth flashing in the dim light, slamming into the fox before it can claim another life."
    "A vicious fight follows, snarls, snapping jaws, a tangle of fur and claws"
    hide fox
    "Silence"
    "The wolf stands there, breathing hard, blood on her muzzle."
    "Not hers."
    "She turns to you, those sharp eyes locking onto yours."
    "The fox had been fast, cunning, hunting the young ones with sharp eyes and sharper teeth. But the wolf had been faster."
    "Now, the clearing is still, except for the ragged breath in your chest and the smell of blood in the air."
    "The fox lies in a heap, throat torn, its clever eyes staring at nothing."
    "The wolf licks the blood from her muzzle, then turns to you."
    show rabbit entrance left
    show wolf entrance right
    fe "Consider my debt paid, little rabbit."

    "She steps forward, lowering her head slightly so that only Whitetail can hear her next words"
    fe "(low, warning tone) Watch your back next time you leave this place. There are worse things than foxes in these woods."

    menu:
    
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

    jump ending_hw_ic

label ending_hw_ic:
    scene burrowinside
    "Wowie people like that you saved the wolf but not much more"

    return