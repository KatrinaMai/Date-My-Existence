label leah_1:
    $ persistent.currentbkg = "courtyard"
    scene bg courtyard with fade_transistion

    show leah
    leah.c "my route 1!"

    menu:
        leah.c "my route 1!"
        "1":
            $ leah.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ leah.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ leah.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    leah.c "Goodbye!"
    
    $ courtyard.add_visit()

    jump expression "morning_" + str(day + 1)
    
label leah_2:
    $ persistent.currentbkg = "courtyard"
    scene bg courtyard with fade_transistion

    show leah
    leah.c "my route 2!"

    menu:
        leah.c "my route 2!"
        "1":
            $ leah.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ leah.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ leah.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    leah.c "Goodbye!"

    $ courtyard.add_visit()

    jump expression "morning_" + str(day + 1)

label leah_3:
    $ persistent.currentbkg = "courtyard"
    scene bg courtyard with fade_transistion

    show leah
    leah.c "my route 3!"
    leah.c "Let's go somewhere else."

    $ persistent.currentbkg = "dorms"
    show bg dorms with fade_transistion

    leah.c "and we are somewhere else"

    menu:
        leah.c "and we are somewhere else"
        "1":
            $ leah.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ leah.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ leah.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    leah.c "Goodbye!"

    $ courtyard.add_visit()

    jump expression "morning_" + str(day + 1)
    
label leah_4:
    $ persistent.currentbkg = "courtyard"
    scene bg courtyard with fade_transistion
    
    show leah
    leah.c "my route 4!"
    leah.c "Let's go somewhere else."

    $ persistent.currentbkg = "dorms"
    show bg dorms with fade_transistion

    leah.c "and we are somewhere else"

    menu:
        leah.c "and we are somewhere else"
        "1":
            $ leah.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
        "2":
            $ leah.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
        "3":
            $ leah.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"

    leah.c "Goodbye!"

    $ courtyard.add_visit()

    jump expression "morning_" + str(day + 1)
    