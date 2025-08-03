label lynn_1:
    $ persistent.currentbkg = "track"
    scene bg track with fade_transistion

    show lynn
    lynn.c "my route 1!"

    menu:
        lynn.c "my route 1!"
        "1":
            $ lynn.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ lynn.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ lynn.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    lynn.c "It was rad hanging out!"

    $ track.add_visit()

    jump expression "morning_" + str(day + 1)
    
label lynn_2:
    $ persistent.currentbkg = "track"
    scene bg track with fade_transistion

    show lynn
    lynn.c "my route 2!"

    menu:
        lynn.c "my route 2!"
        "1":
            $ lynn.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ lynn.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ lynn.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    lynn.c "It was rad hanging out!"

    $ track.add_visit()

    jump expression "morning_" + str(day + 1)

label lynn_3:
    $ persistent.currentbkg = "track"
    scene bg track with fade_transistion

    show lynn
    lynn.c "my route 3!"
    lynn.c "Let's go somewhere else."

    $ persistent.currentbkg = "dorms"
    show bg dorms with fade_transistion

    lynn.c "and we are somewhere else"

    menu:
        lynn.c "and we are somewhere else"
        "1":
            $ lynn.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ lynn.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ lynn.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    lynn.c "It was rad hanging out!"

    $ track.add_visit()

    jump expression "morning_" + str(day + 1)
    
label lynn_4:
    $ persistent.currentbkg = "track"
    scene bg track with fade_transistion
    
    show lynn
    lynn.c "my route 4!"
    lynn.c "Let's go somewhere else."

    $ persistent.currentbkg = "dorms"
    show bg dorms with fade_transistion

    lynn.c "and we are somewhere else"

    menu:
        lynn.c "and we are somewhere else"
        "1":
            $ lynn.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ lynn.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ lynn.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    lynn.c "It was rad hanging out!"

    $ track.add_visit()
    
    jump expression "morning_" + str(day + 1)
    