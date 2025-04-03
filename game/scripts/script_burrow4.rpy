

label burrow4:
    scene burrowinside

    show rabbit burrow left
    show onepaw burrow right

    "Fourth burrow encounter."

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