label oriel_1:
    $ persistent.currentbkg = "track"
    scene bg track with fade_transistion

    show oriel
    oriel.c "...my route 1."

    menu:
        oriel.c "...my route 1."
        "1":
            $ oriel.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ oriel.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ oriel.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"
    
    oriel.c "..."

    $ track.add_visit()

    jump expression "morning_" + str(day + 1)
    
label oriel_2:
    $ persistent.currentbkg = "track"
    scene bg track with fade_transistion

    show oriel
    oriel.c "...my route 2."

    menu:
        oriel.c "...my route 2."
        "1":
            $ oriel.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ oriel.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ oriel.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"
    
    oriel.c "..."

    $ track.add_visit()

    jump expression "morning_" + str(day + 1)

label oriel_3:
    $ persistent.currentbkg = "track"
    scene bg track with fade_transistion

    show oriel
    oriel.c "...my route 3"
    oriel.c "...Let's go somewhere else."

    $ persistent.currentbkg = "dorms"
    show bg dorms with fade_transistion

    oriel.c "...and we are somewhere else"

    menu:
        oriel.c "...and we are somewhere else"
        "1":
            $ oriel.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ oriel.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ oriel.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"
    
    oriel.c "..."

    $ track.add_visit()

    jump expression "morning_" + str(day + 1)
    
label oriel_4:
    $ persistent.currentbkg = "track"
    scene bg track with fade_transistion
    
    show oriel
    oriel.c "...my route 4."
    oriel.c "...Let's go somewhere else."

    $ persistent.currentbkg = "dorms"
    show bg dorms with fade_transistion

    oriel.c "...and we are somewhere else"

    menu:
        oriel.c "...and we are somewhere else"
        "1":
            $ oriel.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ oriel.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ oriel.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"
    
    oriel.c "..."

    $ track.add_visit()
    
    jump expression "morning_" + str(day + 1)
    