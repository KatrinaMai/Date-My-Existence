label cadenza_1:
    $ persistent.currentbkg = "courtyard"
    scene bg courtyard with fade_transistion

    show cadenza
    cadenza.c "my route 1!"

    menu:
        cadenza.c "my route 1!"
        "1":
            $ cadenza.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ cadenza.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ cadenza.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    cadenza.c "See ya!"

    $ courtyard.add_visit()

    jump expression "morning_" + str(day + 1)
    
label cadenza_2:
    $ persistent.currentbkg = "courtyard"
    scene bg courtyard with fade_transistion

    show cadenza
    cadenza.c "my route 2!"

    menu:
        cadenza.c "my route 2!"
        "1":
            $ cadenza.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ cadenza.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ cadenza.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    cadenza.c "See ya!"

    $ courtyard.add_visit()

    jump expression "morning_" + str(day + 1)

label cadenza_3:
    $ persistent.currentbkg = "courtyard"
    scene bg courtyard with fade_transistion

    show cadenza
    cadenza.c "my route 3!"
    cadenza.c "Let's go somewhere else."

    $ persistent.currentbkg = "dorms"
    show bg dorms with fade_transistion

    cadenza.c "and we are somewhere else"

    menu:
        cadenza.c "and we are somewhere else"
        "1":
            $ cadenza.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ cadenza.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ cadenza.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    cadenza.c "See ya!"

    $ courtyard.add_visit()

    jump expression "morning_" + str(day + 1)
    
label cadenza_4:
    $ persistent.currentbkg = "courtyard"
    scene bg courtyard with fade_transistion
    
    show cadenza
    cadenza.c "my route 4!"
    cadenza.c "Let's go somewhere else."

    $ persistent.currentbkg = "dorms"
    show bg dorms with fade_transistion

    cadenza.c "and we are somewhere else"

    menu:
        cadenza.c "and we are somewhere else"
        "1":
            $ cadenza.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ cadenza.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ cadenza.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    cadenza.c "See ya!"

    $ courtyard.add_visit()

    jump expression "morning_" + str(day + 1)
    