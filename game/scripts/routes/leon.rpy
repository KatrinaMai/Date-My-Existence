label leon_1:
    $ persistent.currentbkg = "gameroom"
    scene bg gameroom with fade_transistion

    show leon
    leon.c "my route 1"

    menu:
        leon.c "my route 1"
        "1":
            $ leon.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ leon.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ leon.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    leon.c "later bro"

    $ gameroom.add_visit()

    jump expression "morning_" + str(day + 1)
    
label leon_2:
    $ persistent.currentbkg = "gameroom"
    scene bg gameroom with fade_transistion

    show leon
    leon.c "my route 2"

    menu:
        leon.c "my route 1"
        "1":
            $ leon.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ leon.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ leon.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    leon.c "later bro"

    $ gameroom.add_visit()

    jump expression "morning_" + str(day + 1)

label leon_3:
    $ persistent.currentbkg = "gameroom"
    scene bg gameroom with fade_transistion

    show leon
    leon.c "my route 3"
    leon.c "Let's go somewhere else."

    $ persistent.currentbkg = "dorms"
    show bg dorms with fade_transistion

    leon.c "and we are somewhere else"

    menu:
        leon.c "my route 1"
        "1":
            $ leon.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ leon.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ leon.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    leon.c "later bro"

    $ gameroom.add_visit()

    jump expression "morning_" + str(day + 1)
    
label leon_4:
    $ persistent.currentbkg = "gameroom"
    scene bg gameroom with fade_transistion
    
    show leon
    leon.c "my route 4"
    leon.c "Let's go somewhere else."

    $ persistent.currentbkg = "dorms"
    show bg dorms with fade_transistion

    leon.c "and we are somewhere else"

    menu:
        leon.c "and we are somewhere else"
        "1":
            $ leon.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ leon.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ leon.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    leon.c "later bro"

    $ gameroom.add_visit()
    
    jump expression "morning_" + str(day + 1)