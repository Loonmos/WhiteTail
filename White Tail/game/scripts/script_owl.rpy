define o = Character("Owl", color="#616161")

label owl:
    scene snowy forest

    show rabbit at left
    show owl at right

    "This is where you talk to the owl."

    "They say shit depending on what you did."

    hide rabbit
    hide owl

    jump ending_pick



label ending_pick:
    if help_wolf:
        if pay_crows:
            jump end_hw_pc
        else:
            jump end_hw_ic

    else:
        if pay_crows:
            jump end_lw_pc
        else:
            jump end_lw_ic