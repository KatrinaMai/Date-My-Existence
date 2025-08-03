label kd_1:
    $ persistent.currentbkg = "track"
    scene bg track with fade_transistion

    show kd
    kd.c "my route 1!"

    menu:
        kd.c "my route 1!"
        "1":
            $ kd.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ kd.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ kd.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    kd.c "Peace out"

    $ track.add_visit()

    jump expression "morning_" + str(day + 1)
    
label kd_2:
    $ persistent.currentbkg = "track"
    scene bg track with fade_transistion

    show kd
    kd.c "my route 2!"

    menu:
        kd.c "my route 2!"
        "1":
            $ kd.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ kd.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ kd.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    kd.c "Peace out"

    $ track.add_visit()

    jump expression "morning_" + str(day + 1)

label kd_3:
    $ persistent.currentbkg = "track"
    scene bg track with fade_transistion

    show kd
    kd.c "my route 3!"
    kd.c "Let's go somewhere else."

    $ persistent.currentbkg = "dorms"
    show bg dorms with fade_transistion

    kd.c "and we are somewhere else"

    menu:
        kd.c "and we are somewhere else"
        "1":
            $ kd.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ kd.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ kd.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    kd.c "Peace out"

    $ track.add_visit()

    jump expression "morning_" + str(day + 1)
    
label kd_4:
    $ persistent.currentbkg = "track"
    scene bg track with fade_transistion
    
    show kd
    kd.c "my route 4!"
    kd.c "Let's go somewhere else."

    $ persistent.currentbkg = "dorms"
    show bg dorms with fade_transistion

    kd.c "and we are somewhere else"

    menu:
        kd.c "and we are somewhere else"
        "1":
            $ kd.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ kd.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ kd.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    kd.c "Peace out"

    $ track.add_visit()
    
    jump expression "morning_" + str(day + 1)
    