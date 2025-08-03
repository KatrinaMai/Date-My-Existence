label lukas_1:
    $ persistent.currentbkg = "gameroom"
    scene bg gameroom with fade_transistion

    show lukas
    lukas.c "my route 1!"

    menu:
        lukas.c "my route 1!"
        "1":
            $ lukas.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ lukas.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ lukas.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    lukas.c "Catch you later!"

    $ gameroom.add_visit()

    jump expression "morning_" + str(day + 1)
    
label lukas_2:
    $ persistent.currentbkg = "gameroom"
    scene bg gameroom with fade_transistion

    show lukas
    lukas.c "my route 2!"

    menu:
        lukas.c "my route 2!"
        "1":
            $ lukas.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ lukas.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ lukas.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    lukas.c "Catch you later!"

    $ gameroom.add_visit()

    jump expression "morning_" + str(day + 1)

label lukas_3:
    $ persistent.currentbkg = "gameroom"
    scene bg gameroom with fade_transistion

    show lukas
    lukas.c "my route 3!"
    lukas.c "Let's go somewhere else."

    $ persistent.currentbkg = "dorms"
    show bg dorms with fade_transistion

    lukas.c "and we are somewhere else"

    menu:
        lukas.c "and we are somewhere else"
        "1":
            $ lukas.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ lukas.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ lukas.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    lukas.c "Catch you later!"

    $ gameroom.add_visit()

    jump expression "morning_" + str(day + 1)
    
label lukas_4:
    $ persistent.currentbkg = "gameroom"
    scene bg gameroom with fade_transistion
    
    show lukas
    lukas.c "my route 4!"
    lukas.c "Let's go somewhere else."

    $ persistent.currentbkg = "dorms"
    show bg dorms with fade_transistion

    lukas.c "and we are somewhere else"

    menu:
        lukas.c "and we are somewhere else"
        "1":
            $ lukas.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ lukas.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ lukas.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    lukas.c "Catch you later!"

    $ gameroom.add_visit()
    
    jump expression "morning_" + str(day + 1)