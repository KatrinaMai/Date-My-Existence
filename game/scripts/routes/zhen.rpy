label zhen_1:
    $ persistent.currentbkg = "gameroom"
    scene bg gameroom with fade_transistion

    show zhen
    zhen.c "my route 1!"

    menu:
        zhen.c "my route 1!"
        "1":
            $ zhen.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ zhen.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ zhen.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    zhen.c "thanks for hanging out :)"

    $ gameroom.add_visit()

    jump expression "morning_" + str(day + 1)
    
label zhen_2:
    $ persistent.currentbkg = "gameroom"
    scene bg gameroom with fade_transistion

    show zhen
    zhen.c "my route 2!"

    menu:
        zhen.c "my route 2!"
        "1":
            $ zhen.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ zhen.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ zhen.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"
    
    zhen.c "thanks for hanging out :)"

    $ gameroom.add_visit()

    jump expression "morning_" + str(day + 1)

label zhen_3:
    $ persistent.currentbkg = "gameroom"
    scene bg gameroom with fade_transistion

    show zhen
    zhen.c "my route 3!"
    zhen.c "Let's go somewhere else."

    $ persistent.currentbkg = "dorms"
    show bg dorms with fade_transistion

    zhen.c "and we are somewhere else"

    menu:
        zhen.c "and we are somewhere else"
        "1":
            $ zhen.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ zhen.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ zhen.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"
    
    zhen.c "thanks for hanging out :)"

    $ gameroom.add_visit()

    jump expression "morning_" + str(day + 1)
    
label zhen_4:
    $ persistent.currentbkg = "gameroom"
    scene bg gameroom with fade_transistion
    
    show zhen
    zhen.c "my route 4!"
    zhen.c "Let's go somewhere else."

    $ persistent.currentbkg = "dorms"
    show bg dorms with fade_transistion

    zhen.c "and we are somewhere else"

    menu:
        zhen.c "and we are somewhere else"
        "1":
            $ zhen.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ zhen.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ zhen.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"
    
    zhen.c "thanks for hanging out :)"

    $ gameroom.add_visit()
    
    jump expression "morning_" + str(day + 1)