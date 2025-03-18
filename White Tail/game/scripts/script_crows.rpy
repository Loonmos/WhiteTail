define c1 = Character("Crow 1", color="#616161")
define c2 = Character("Crow 2", color="#616161")
define c3 = Character("Crow 3", color="#616161")
define c4 = Character("Crow 4", color="#616161")

define pay_crows = False

label crows:
    scene snowy forest

    show rabbit at left
    show crow at right

    "This is where the player meets the crows."

    menu:
        "What do I do?"

        "Give the Crows your food":
            $ pay_crows = True
            jump crows_pay

        "Ignore the Crows request":
            $ pay_crows = False
            jump crows_ignore

label crows_pay:

    "You pay the crows, yippie."

    hide rabbit
    hide crow

    jump burrow2

label crows_ignore:

    "You don't pay the crows, uh oh."

    hide rabbit
    hide crow

    jump burrow2