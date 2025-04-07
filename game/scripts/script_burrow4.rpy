

label burrow4:
    #scene burrowinsideup with fade

    #show rabbit burrow left with dissolve
    #show onepaw burrow right with dissolve

    #"Fourth burrow encounter."

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