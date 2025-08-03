label himitsu_1:
    $ persistent.currentbkg = "courtyard"
    scene bg courtyard with fade_transistion

    show himitsu
    himitsu.c "my route 1."

    menu:
        himitsu.c "my route 1."
        "1":
            $ himitsu.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ himitsu.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ himitsu.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    himitsu.c "Farewell."

    $ courtyard.add_visit()

    jump expression "morning_" + str(day + 1)
    
label himitsu_2:
    $ persistent.currentbkg = "courtyard"
    scene bg courtyard with fade_transistion

    show himitsu
    himitsu.c "my route 2."

    menu:
        himitsu.c "my route 2."
        "1":
            $ himitsu.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ himitsu.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ himitsu.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    himitsu.c "Farewell."

    $ courtyard.add_visit()

    jump expression "morning_" + str(day + 1)

label himitsu_3:
    $ persistent.currentbkg = "courtyard"
    scene bg courtyard with fade_transistion

    show himitsu
    himitsu.c "my route 3."
    himitsu.c "Let's go somewhere else."

    $ persistent.currentbkg = "dorms"
    show bg dorms with fade_transistion

    himitsu.c "and we are somewhere else"

    menu:
        himitsu.c "and we are somewhere else"
        "1":
            $ himitsu.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ himitsu.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ himitsu.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    himitsu.c "Farewell."

    $ courtyard.add_visit()

    jump expression "morning_" + str(day + 1)
    
label himitsu_4:
    $ persistent.currentbkg = "courtyard"
    scene bg courtyard with fade_transistion
    
    show himitsu
    himitsu.c "my route 4."
    himitsu.c "Let's go somewhere else."

    $ persistent.currentbkg = "dorms"
    show bg dorms with fade_transistion

    himistu.c "and we are somewhere else"

    menu:
        himitsu.c "and we are somewhere else"
        "1":
            $ himitsu.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ himitsu.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ himitsu.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    himitsu.c "Farewell."

    $ courtyard.add_visit()

    jump expression "morning_" + str(day + 1)
    