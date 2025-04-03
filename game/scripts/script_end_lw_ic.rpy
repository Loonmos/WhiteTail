# this is the ending in which you help the wolf and pay the crows

label end_lw_ic:
    scene burrowoutside
    "The morning is quiet, the air thick with the scent of damp earth and wildflowers."
    show rabbit entrance
    "You stretch, feeling the warmth of the sun on your fur."
    "Another day in the warren. Another day of..."
    
    "CRACK!"

    "A scream. A shape lunging from the tall grass. The scent of blood."

    "Chaos erupts. Rabbits scatter, but it's too late."
    "The fox and the wolf are among them, teeth flashing, claws slashing."
    "The wolf moves with ruthless precision, cutting off escape routes, striking down the ones who run."

    "One by one, your kin fall."

    "And then..."
    "There is only you..."
    "The fox prowls to your side, panting, eyes gleaming with triumph. But it is the wolf who steps forward, her shadow stretching long over you."
    show rabbit entrance left
    show wolf entrance right
    fe "(low, almost gentle) Did you think I would forget?"

    "She circles, slow and deliberate, the airthick with the weight of what is coming"

    fe "You left me there, caught like prey. Let me feel the steel bite into my flesh. Let me wonder if I would die alone."

    "She stops, towering over you now."

    fe "So I made sure you wouldn't die alone either."
    hide wolf
    show fox entrance right
    "The fox chuckles, blood dripping from his muzzle."
    "He leans in close"
    vp "You should've given the crows your food. Maybe then someone would have warned you."
    hide fox
    show wolf entrance right
    "You see teeth. You feel the weight of inevitability."
    "The wolf doesn't lunge, she doesn't need to."
    "She takes her time, letting you understand."

    "Then she strikes."

    jump ending_death

label ending_death:
    scene heaven
    show rabbit entrance

    "The consequences of your actions caught up with you..."

    return