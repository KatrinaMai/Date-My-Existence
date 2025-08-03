# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    class Person:
        instances = []

        def __init__(self, points, rand_counter):
            Person.instances.append(self)
            self.points = points
            self.rand_counter = rand_counter
        
        # def __init__(self, character, name, points = 0, rand_encount_1 = False, rand_encount_2 = False):
        #     Person.instances.append(self)
        #     self.c = character
        #     self.name = name
        #     self.points = points
        #     self.rand_encount_1 = False
        #     self.rand_encount_2 = False
        
        def add_points(self, change):
            self.points += change
            # TODO: call screen points
        
        def set_rand_1(self, change):
            self.rand_encount_1 = change
        
        # def set_rand_2(self):
        #     self.rand_encount_2 = True
        
        # def is_successful(self):
        #     if self.points > 3:
        #         return "success"
        #     else:
        #         return "fail"

init python:
    class Location:
        # instances = []
        
        def __init__(self, name):
            # Location.instances.append(self)
            self.name = name
            self.route = None
            self.visits = 0
        
        def add_visit(self):
            self.visits += 1

# init python:
#     def character_callback(event, **kwargs):
#         if event == "end":
#             renpy.music.play("audio/dialogue_click.wav", channel="audio")

#     config.all_character_callbacks.append(character_callback)

# init python:
#     def callbackcontinue(ctc, **kwargs):
#         if ctc == "end":
#             renpy.sound.play("audio/dialogue_click.wav")

init python:
    def dismiss_callback():
        renpy.play("audio/dialogue_click.wav")
        return True

    config.say_allow_dismiss = dismiss_callback

#main characters
default player = ""
# default protag = Person(Character("[player]"), [player])
# default zhen = Person(Character("Zhen"), "Zhen")
# default leah = Person(Character("Leah"), "Leah")
# default lukas = Person(Character("Lukas"), "Lukas")
# default kd = Person(Character("KD"), "KD")
# default cadenza = Person(Character("Cadenza"), "Cadenza")
# default oriel = Person(Character("Oriel"), "Oriel")
# default leon = Person(Character("Leon"), "Leon")
# default lynn = Person(Character("Lynn"), "Lynn")
# default himitsu = Person(Character("Himitsu"), "Himitsu")
# define ophelia = Person(Character("Ophelia"), "Ophelia")

define character.protag = Character("[player]", who_color = "#1d1946")
default protag = Person(points = 0, rand_counter = 0)

define character.zhen = Character("Zhen", who_color = "#251F1F")
default zhen = Person(points = 0, rand_counter = 0)

define character.leah = Character("Leah", who_color = "#328a36")
default leah = Person(points = 0, rand_counter = 0)

define character.lukas = Character("Lukas", who_color = "#bf1111")
default lukas = Person(points = 0, rand_counter = 0)

define character.kd = Character("KD", who_color = "#e3894f")
default kd = Person(points = 0, rand_counter = 0)

define character.cadenza = Character("Cadenza", who_color = "#ff0080")
default cadenza = Person(points = 0, rand_counter = 0)

define character.oriel = Character("Oriel", who_color = "#341946")
default oriel = Person(points = 0, rand_counter = 0)

define character.leon = Character("Leon", who_color = "#1058bc")
default leon = Person(points = 0, rand_counter = 0)

define character.lynn = Character("Lynn", who_color = "#886798")
default lynn = Person(points = 0, rand_counter = 0)

define character.himitsu = Character("Himitsu", who_color = "#deae1d")
default himitsu = Person(points = 0, rand_counter = 0)

define character.ophelia = Character("Ophelia", who_color = "#a106a2")
default ophelia = Person(points = 0, rand_counter = 0)


image noname:
    "gui/name_not_entered.png"
    pos(1020, 660)

# Locations
default track = Location("Track")
default courtyard = Location("Courtyard")
default gameroom = Location("Gameroom")
default dorms = Location("Dorms")

# Transitions
define fadeoutright = ComposeTransition(Dissolve(0.25), easeoutright, None)
define fadeoutleft = ComposeTransition(Dissolve(0.25), easeoutleft, None)
define fade_transistion = Fade(0.5, 0.8, 0.5)
define time_fade = Fade(0.5, 2.15, 0.5)

# Image Transforms
transform LiveDissolve(spriteB, duration = 0.08):
    DynamicImage(spriteB) with Dissolve(duration, alpha=True)

# Variables
define candidates = ["Zhen", "Leah", "Lukas", "KD", "Cadenza", "Oriel", "Leon", "Lynn", "Himitsu", "Ophelia"]
default date = "11/2"
default weekday = "MON"
default time = "Morning"

define dates = ["11/2", "11/3", "11/4", "11/5", "11/6"]
define weekdays_short = ["MON", "TUE", "WED", "THU", "FRI"]
define weekdays_long = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
define timesofday = ["Morning", "Afternoon", "After School"]

default rand_character = ""
default day = 1
default timeofday = 0


# The game starts here.
label start:
    $ quick_menu = False
    stop music fadeout 1.0
    scene black
    with fade
    
    # $ quick_menu = False
    # show screen fake_main_menu
    # hide screen fake_main_menu with fade

    play music "audio/junes.mp3" fadein 0.75 volume 0.1 loop 
    show image "gui/input_frame_bg.png" with fade
    call name_check
    
    # show image "gui/order_finished.png"
    # $ renpy.pause(1.5, hard = True)

    $ day = 1
    $ weekday = weekdays_short[day - 1]

    stop music fadeout 1.0
    scene black with fade
    jump expression "morning_" + str(day)

label demo_start:
    $ quick_menu = False
    stop music fadeout 1.0
    scene black
    with fade
    
    play music "audio/junes.mp3" fadein 0.75 volume 0.1 loop 
    show image "gui/input_frame_bg.png" with fade
    call name_check
    
    stop music fadeout 1.0
    scene black with fade
    $ quick_menu = True
    $ day = 1
    $ weekday = weekdays_short[day - 1]
    jump expression "demo_morning"

label name_check:
    call screen name_call
    $ player = player.strip()
    hide noname
    # $ player = player.lower()
    # $ player = ''.join( (c.upper() if i == 0 or player[i-1] == ' ' else c) for i, c in enumerate(player))

    if player == "":
        show noname
        # call screen error_message
        jump name_check
    else:
        call screen namecheck_screen("[player]!", Return(), Jump("name_check"))
    
    return

label rand_encounter:
    menu:
        "random":
            pass
        "zhen":
            call rand_encounter_zhen
            scene bg map with fade_transistion
            call screen MapUI()
        "leah":
            call rand_encounter_leah
            scene bg map with fade_transistion
            call screen MapUI()
        "lukas":
            call rand_encounter_lukas
            scene bg map with fade_transistion
            call screen MapUI()
        "kd":
            call rand_encounter_kd
            scene bg map with fade_transistion
            call screen MapUI()
        "cadenza":
            call rand_encounter_cadenza
            scene bg map with fade_transistion
            call screen MapUI()
        "oriel":
            call rand_encounter_oriel
            scene bg map with fade_transistion
            call screen MapUI()
        "leon":
            call rand_encounter_leon
            scene bg map with fade_transistion
            call screen MapUI()
        "lynn":
            call rand_encounter_lynn
            scene bg map with fade_transistion
            call screen MapUI()
        "himitsu":
            call rand_encounter_himitsu
            scene bg map with fade_transistion
            call screen MapUI()

    $ rand_character = "rand_encounter_" + renpy.random.choice(candidates).lower()
    
    if rand_character == "rand_encounter_ophelia":
        jump rand_encounter

    call time_change
    $ quick_menu = True
    $ timeofday = (timeofday + 1) % 3

    call expression rand_character

    call time_change
    $ quick_menu = True
    $ timeofday = (timeofday + 1) % 3

    scene bg map with fade_transistion
    call screen MapUI()

# transform change_time:
#     if day == 1:
#         weekday = "Monday"
#     elif day == 2:
#         weekday = "Tuesday"
#     elif day == 3:
#         weekday = "Wednesday"
#     elif day == 4:
#         weekday = "Thursday"
#     else day == 5:
#         weekday = "Friday"
    
#     parallel:
#         alpha 0.0 xalign 0.10 yalign 0.45
#         ease 1.25 alpha 1.0 xalign 0.40
#         pause 0.9
#         ease 1 alpha 0.0 xalign 0.80

label time_change:
    hide screen dvd
    $ quick_menu = False
    scene black with fade

    # if timeofday == "After School":
    #     $ weekday = weekdays[day - 1]
    #     show screen time_change("After School", "Early Morning", )
    #     $ timeofday = "Early Morning"
    # elif timeofday == "Early Morning":
    #     show screen time_change("Early Morning", "Morning")
    #     $ timeofday = "Morning"
    # else:
    #     show screen time_change("Morning", "After School")
    #     $ timeofday = "After School"

    show screen time_change()
    
    # show text "[weekday]" at weekday_transform
    # show text "[timeofday]" at timeofday_transform
    pause 2.35

    hide screen time_change

    return

label track:
    if track.visits != 0:
        jump expression track.route.name.lower() + "_" + str(track.visits)
    else:
        jump track_start

label courtyard:
    if courtyard.visits != 0:
        jump expression courtyard.route.name.lower() + "_" + str(courtyard.visits)
    else:
        jump courtyard_start

label gameroom:
    if gameroom.visits != 0:
        jump expression gameroom.route.name.lower() + "_" + str(gameroom.visits)
    else:
        jump gameroom_start
    
label track_start:
    $ persistent.currentbkg = "track"
    scene bg track with fade_transistion

    show kd:
        ease 0.25 xalign 0.1
    show lynn:
        ease 0.25 xalign 0.5
    show oriel:
        ease 0.25 xalign 0.9
    with Dissolve(0.25)

    kd "hi!"
    lynn "sup"
    oriel "..."

    menu:
        "KD":
            kd.c "aw, thank you!"
            $ kd.add_points(1)
            $ track.route = kd
        "Lynn":
            lynn.c "Score!"
            $ lynn.add_points(1)
            $ track.route = lynn
        "Oriel":
            oriel.c "...Hmph"
            $ oriel.add_points(1)
            $ track.route = oriel
    
    $ track.add_visit()

    $ day = day + 1
    call time_change
    $ quick_menu = True
    $ timeofday = (timeofday + 1) % 3
    
    jump expression "morning_" + str(day + 1)

label courtyard_start:
    $ persistent.currentbkg = "courtyard"
    scene bg courtyard with fade_transistion

    show himitsu:
        ease 0.25 xalign 0.1
    show leah:
        ease 0.25 xalign 0.5
    show cadenza:
        ease 0.25 xalign 0.9
    with Dissolve(0.25)

    himitsu "..."
    leah "Oh! Hello, [player]."
    cadenza "What's up?"

    menu:
        "Himitsu":
            himitsu "Oh, I see."
            $ himitsu.add_points(1)
            $ courtyard.route = himitsu
        "Leah":
            leah "Oh! Thank you so much!"
            $ leah.add_points(1)
            $ courtyard.route = leah
        "Cadenza":
            cadenza "Ah, I'm honored."
            $ cadenza.add_points(1)
            $ courtyard.route = cadenza

    $ courtyard.add_visit()

    $ day = day + 1
    call time_change
    $ quick_menu = True
    $ timeofday = (timeofday + 1) % 3

    jump expression "morning_" + str(day + 1)

label gameroom_start:
    $ persistent.currentbkg = "gameroom"
    scene bg gameroom with fade_transistion

    show lukas:
        ease 0.25 xalign 0.1
    show leon:
        ease 0.25 xalign 0.5
    show zhen left:
        ease 0.25 xalign 0.9

    lukas "yo waddup"
    leon "who says waddup anymore?"

    show zhen open
    zhen "I don't know you people"
    show zhen -open

    menu:
        "Lukas":
            lukas "Oh yea, I'm so good."
            $ lukas.add_points(1)
            $ gameroom.route = lukas
        "Leon":
            leon "Oh uh cool ig"
            $ leon.add_points(1)
            $ gameroom.route = leon
        "Zhen":
            show zhen left positive
            zhen "Of course ^ u ^"
            $ zhen.add_points(1)
            $ gameroom.route = zhen

    $ gameroom.add_visit()

    $ day = day + 1
    call time_change
    $ quick_menu = True
    $ timeofday = (timeofday + 1) % 3

    jump expression "morning_" + str(day + 1)

label dorms:
    $ persistent.currentbkg = "dorms"
    scene bg dorms with fade_transistion

    show ophelia
    ophelia "...why are you here?"
    $ ophelia.add_points(1)

    $ day = day + 1
    call time_change
    $ quick_menu = True
    $ timeofday = (timeofday + 1) % 3

    jump expression "morning_" + str(day + 1)

label choose_ending:
    menu:
        "Zhen":
            $ choice = zhen
        "Leah":
            $ choice = leah
        "Lukas":
            $ choice = lukas
        "KD":
            $ choice = kd
        "Cadenza":
            $ choice = cadenza
        "Oriel":
            $ choice = oriel
        "Leon":
            $ choice = leon
        "Lynn":
            $ choice = lynn
        "Himitsu":
            $ choice = himitsu
        "Ophelia" if ophelia.points >= 1:
            $ choice = ophelia

    jump expression "ending_" + getattr(choice, "name").lower() + "_" + choice.is_successful()