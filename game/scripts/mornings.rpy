label demo_morning:
    $ quick_menu = False
    play music "audio/Popcorn.mp3" fadein 1.0 volume 0.25 loop
    $ persistent.currentbkg = "dininghall"
    scene bg dininghall with fade
    $ timeofday = 0
    
    show screen dvd
    show zhen right
    $ quick_menu = True
    with Dissolve(0.2)

    "As you finish your order, Zhen turns to you with a mischevious look in his eyes."

    show zhen open

    zhen "Ooh, stay right here. I'll be right back."

    show zhen -open
    hide zhen with Dissolve(0.1)
    
    protag "..."

    "It becomes noticibly quiet after Zhen leaves."

    "Suddenly, you feel like you're being watched."

    menu:
        "Suddenly, you feel like you're being watched."
        "Investigate":
            "You take a glance around and spot someone impatiently waving at you from an empty hallway usually used by the lunch staff."
            show ophelia right negative:
                xalign 0.5
            with Dissolve(0.1)
            "Making your way towards the hallway, you discover it was Ophelia staring daggers into you."
        "Ignore":
            "???" "Ugh. Unbelievable!"
            "You get yanked backwards into an empty hallway that's primarily used by the lunch staff." with hpunch
            show ophelia right negative:
                xalign 0.0
                ease 0.2 xalign 0.5
            with Dissolve(0.1)
            "Before you can react, you're face to face with Opehlia."


    "It's a little surreal to see the literal god you and your friends have been housing for the past few months just casually in the school dininghall."

    show ophelia open

    ophelia "[player]! God, I hate the way you humans act in the morning."

    show ophelia -open

    menu:
        ophelia "[player]! God, I hate the way you humans act in the morning."
        "Sorry":
            show ophelia right negative at LiveDissolve("ophelia right open")
            ophelia "It's fine. From what I've learned, humans tend to not act \"right\" before their morning coffee so I won't complain {i}too much{/i} of your lack of perception."
        "What are you doing here?":
            pass

    show ophelia open -negative

    ophelia "I simply needed a chance to speak to you privately without gaining the attention of your... little group."
    ophelia "I have an important mission for you, but only you can know of it."

    show ophelia -open

    "Ophelia lets out a hesitant sigh and you begin to sweat."

    protag "{i}Could it be a new foe or are there current plans not working out? What if the world is on the verge of collapse and Ophelia doesn't want to worry the oth-{/i}"
    
    show ophelia open

    ophelia "I require you to attend an event. A... convention of sorts one could call it."

    show ophelia -open

    menu:
        ophelia "I require you to attend an event. A... convention of sorts one could call it."
        "What.":
            pass
        "That's it?":
            pass

    show ophelia open

    ophelia "This is far from what I typically assign you to do, I'm well aware. But, since I've begun inhabiting your realm, I've been developing interests of my own."
    ophelia "I'm also aware that I lack the knowledge necessary to traverse freely. Well, not that I've needed to with your other comrades' assistance."
    ophelia "Only fair since it's {i}your group's{/i} fault that I'm even here in the first place."

    show ophelia -open

    menu:
        ophelia "Only fair since it's {i}your group's{/i} fault that I'm even here in the first place."
        "Why specifically me?":
            pass
        "Can't you ask the others?":
            pass

    show ophelia right at LiveDissolve("ophelia right negative open")

    ophelia "Of course I had to resort to you over the others! The relationship between me and your friends is strictly professional. Hmph."
    ophelia "I can't let my embarrassing interests alter the intimidating perception your friends have of me."

    show ophelia right negative open at LiveDissolve("ophelia right open")

    ophelia "Though, you seem the least judgmental, so I believe you to be the best candidate."

    show ophelia right -open -negative

    menu:
        ophelia "Though, you seem the least judgmental, so I believe you to be the best candidate."
        "What makes it so embarrassing?":
            pass
        "I'm sure it's not that embarrassing.":
            pass

    show ophelia open

    ophelia "Well Leon, in providing me what he calls \"unsupervised access to the internet\", has unfortunately led me to indulge in media stereotypically seen as \"lame\" by your kind."

    show ophelia -open

    protag "..."
    extend "?"

    show ophelia open

    ophelia "Ahem. In other words, I've gotten really into a... reality show."

    show ophelia -open

    ophelia "..."

    show ophelia right at LiveDissolve("ophelia right embarrassed")

    ophelia "...about dating."

    menu:
        ophelia "...about dating."
        "...":
            show ophelia right embarrassed at LiveDissolve("ophelia right open")
            show ophelia right open
        "That's it?":
            show ophelia right embarrassed at LiveDissolve("ophelia right negative open")
            ophelia "It may seem normal for you humans, but a deity such as myself shouldn't recieve satisfaction out of watching humans miscommunicate their way into relationships."
            show ophelia right negative at LiveDissolve("ophelia right open")
            show ophelia right open
        "That's honestly really embarrassing":
            show ophelia right embarrassed at LiveDissolve("ophelia right")
            ophelia "{size=*0.75}Maybe I should have confided with the tall happy boy instead{/size}"
            show ophelia right open

    ophelia "Well. Anyway, the details are unimportant. There is an event being hosted at this very city by the end of the week."
    ophelia "I'd like to aquire some limited edition memorabilia alongside a few signatures."
    ophelia "Only, one issue."
    ophelia "It's couples only."

    show ophelia right open at LiveDissolve("ophelia right negative open")

    ophelia "I don't care how you obtian a partner for the event so long as you never utter my name or refer to me {i}at all{/i} to the others under any circumstance."
    
    show ophelia right negative open at LiveDissolve("ophelia right open")
    
    ophelia "I have nothing to offer you but my gratitude in return. But I would be most appreciative if you accepted my request."

    show ophelia right

    menu:
        ophelia "I have nothing to offer you but my gratitude in return. But I would be most appreciative if you accepted my request."
        "Sure":
            pass
        "Of course":
            pass
        "I owe you anyways":
            pass

    show ophelia positive
    
    ophelia "Thank you for your readiness [player], you don't understand how muc-"

    show ophelia right -positive -open

    zhen "There you are [player]!"

    show ophelia left:
        easein 0.3 xalign 0.8
    with None
    show zhen right open:
        easein 0.3 xalign 0.2
    with Dissolve(0.1)

    # "Approaching the two of you, you see your best friend and roommate appearing quite exasperated."

    zhen "You disappeared all of a sudden! I looked {i}everywhere{/i} for you."

    zhen "Why are you even-"  
    
    show zhen right open at LiveDissolve("zhen right negative")

    zhen "Oh. Ophelia? What are you doing here?"

    show zhen right negative at LiveDissolve("zhen right")
    show ophelia open

    ophelia "Well I-I was just um..."
    ophelia "Oh my. Lost track of the time, I need to wake up Leon and Lukas."
    ophelia "You could say I became their unofficial alarm clock since they always oversleep on their own."
    ophelia "Yes, but that is all!"
    ophelia "Farewell [player]. As to you, Zhen."
    
    show ophelia right

    hide ophelia with fadeoutright
    
    "Before Zhen can respond, Ophelia wanders off down the hallway with a quickened pace."

    show zhen right open

    zhen "So uh..."

    show zhen right negative

    show zhen right:
        easein 0.35 xalign 0.5
    
    show zhen right open
    
    #show zhen right open at LiveDissolve("zhen left open")

    zhen "What was she doing here?"

    show zhen right
    
    menu:
        zhen "What was she doing here?"
        "Uh, nothing of course":
            show zhen open
            zhen "I've lived with you long enough to know you're lying but since I'm so {i}thoughtful{/i} and {i}respectful{/i} of your boundaries, I won't push you to tell me anything."
            zhen "But also, of course, you can tell me anything."
        "She needed my help for her research":
            show zhen open
            zhen "Ah, that checks. I suppose we haven't seen her in a while since things have slowed down."
        "She gave me a super secret mission": #"She told me this super secret mission that I can't tell anybody"
            show zhen right at LiveDissolve("zhen right negative")
            zhen "...Oh, she's back to her weird cryptidness again. Glad I'm not involved with that."
            show zhen right negative at LiveDissolve("zhen right open")

    zhen "Oh right! I got you something."

    show zhen right

    "Zhen shoves a small paper bag right in front of your face. Grabbing it, you look into it to be hit with the scent of a cinnamon bun."

    show zhen right positive open

    zhen "It's an overpriced pastry to go with your equally overpriced coffee."

    show zhen right positive -open

    menu:
        zhen "It's an overpriced pastry to go with your equally overpriced coffee."
        "Thanks":
            pass
        "Why'd you get this for me?":
            pass
    
    show zhen open -positive

    zhen """
    It's a thanks for helping me out with my film assignment last night.
    
    You know how I am, I always get overly ambitious.
    
    But luckily I have such a good actor as a roommate.
    
    Though, your expressions could use some work. Alongside your language.
    """

    show zhen right open at LiveDissolve("zhen right negative")
    
    zhen "And yikes, not just your verbal language either but your physical one too."

    show zhen right negative

    menu:
        zhen "And yikes, not just your verbal language either but your physical one too."
        "Thanks?":
            pass
        "I think you're complaining about me":
            show zhen right negative at LiveDissolve("zhen right open")
            zhen "Of course not!"

    show zhen positive open
    zhen "You are fantastic at following orders though, which is any director's dream."

    show zhen -positive

    "Zhen walks ahead to meet up with two friends already seated at the group's designated table."

    hide zhen with Dissolve(0.2)

    # "As you both continue your conversation, the two of you begin to walk up to the designated meetup table finding two friends aready at the table."

    $ quick_menu = False
    hide screen dvd
    scene black with fade_transistion

    "It seems like you need to charm one of your friends into a date before this friday."
    
    "Will you make it in time?"

    window hide
    with dissolve
    pause(0.75)

    show image "images/logo.png" at truecenter
    with Dissolve(1.5)

    pause(2)

    return

label morning_1:
    $ persistent.currentbkg = "dininghall"
    scene bg dininghall with fade
    $ timeofday = 0
    play music "audio/Popcorn.mp3" fadein 1.0 volume 0.25 loop
    show screen dvd with Dissolve(0.2)

    menu:
        "Day: [day], 
        track: [track.visits], courtyard: [courtyard.visits], gamroom: [gameroom.visits]"
        "Skip intro":
            jump rand_encounter
        "Play":
            pass

    show zhen left
    with Dissolve(0.1)

    "As you finish your order, Zhen turns to you with a mischevious look in his eyes."

    show zhen open

    zhen "Ooh, stay right here. I'll be right back."

    show zhen -open
    hide zhen with fadeoutleft
    
    protag "..."

    "It becomes noticibly quiet after Zhen leaves."

    "Suddenly, you feel like you're being watched."

    menu:
        "Suddenly, you feel like you're being watched."
        "Investigate":
            "You take a glance around and spot someone impatiently waving at you from an empty hallway usually used by the lunch staff."
            show ophelia right negative:
                xalign 0.5
            with Dissolve(0.1)
            "Making your way towards the hallway, you discover it was Ophelia staring daggers into you."
        "Ignore":
            "???" "Ugh. Unbelievable!"
            "You get yanked backwards into an empty hallway that's primarily used by the lunch staff." with hpunch
            show ophelia right negative:
                xalign 0.0
                easeout 0.25 xalign 0.5
            with Dissolve(0.1)
            "Before you can react, you're face to face with Opehlia."


    "It's a little surreal to see the literal god you and your friends have been housing for the past few months just casually in the school dininghall."

    show ophelia open

    ophelia "[player]! God, I hate the way you humans act in the morning."

    show ophelia -open

    menu:
        ophelia "[player]! God, I hate the way you humans act in the morning."
        "Sorry":
            show ophelia right negative at LiveDissolve("ophelia right open")
            ophelia "It's fine. From what I've learned, humans tend to not act \"right\" before their morning coffee so I won't complain {i}too much{/i} of your lack of perception."
        "What are you doing here?":
            pass

    show ophelia open -negative

    ophelia "I simply needed a chance to speak to you privately without gaining the attention of your... little group."
    ophelia "I have an important mission for you, but only you can know of it."

    show ophelia -open

    "Ophelia lets out a hesitant sigh and you begin to sweat."

    protag "{i}Could it be a new foe or are there current plans not working out? What if the world is on the verge of collapse and Ophelia doesn't want to worry the oth-{/i}"
    
    show ophelia open

    ophelia "I require you to attend an event. A... convention of sorts one could call it."

    show ophelia -open

    menu:
        ophelia "I require you to attend an event. A... convention of sorts one could call it."
        "What.":
            pass
        "That's it?":
            pass

    show ophelia open

    ophelia "This is far from what I typically assign you to do, I'm well aware. But, since I've begun inhabiting your realm, I've been developing interests of my own."
    ophelia "I'm also aware that I lack the knowledge necessary to traverse freely. Well, not that I've needed to with your other comrades' assistance."
    ophelia "Only fair since it's {i}your group's{/i} fault that I'm even here in the first place."

    show ophelia -open

    menu:
        ophelia "Only fair since it's {i}your group's{/i} fault that I'm even here in the first place."
        "Why specifically me?":
            pass
        "Can't you ask the others?":
            pass

    show ophelia right at LiveDissolve("ophelia right negative open")

    ophelia "Of course I had to resort to you over the others! The relationship between me and your friends is strictly professional. Hmph."
    ophelia "I can't let my embarrassing interests alter the intimidating perception your friends have of me."

    show ophelia right negative open at LiveDissolve("ophelia right open")

    ophelia "Though, you seem the least judgmental, so I believe you to be the best candidate."

    show ophelia right -open -negative

    menu:
        ophelia "Though, you seem the least judgmental, so I believe you to be the best candidate."
        "What makes it so embarrassing?":
            pass
        "I'm sure it's not that embarrassing.":
            pass

    show ophelia open

    ophelia "Well Leon, in providing me what he calls \"unsupervised access to the internet\", has unfortunately led me to indulge in media stereotypically seen as \"lame\" by your kind."

    show ophelia -open

    protag "..."
    extend "?"

    show ophelia open

    ophelia "Ahem. In other words, I've gotten really into a... reality show."

    show ophelia -open

    ophelia "..."

    show ophelia right at LiveDissolve("ophelia right embarrassed")

    ophelia "...about dating."

    menu:
        ophelia "...about dating."
        "...":
            show ophelia right embarrassed at LiveDissolve("ophelia right open")
            show ophelia right open
        "That's it?":
            show ophelia right embarrassed at LiveDissolve("ophelia right negative")
            ophelia "It may seem normal for you humans, but a deity such as myself shouldn't recieve satisfaction out of watching humans miscommunicate their way into relationships."
            show ophelia right negative at LiveDissolve("ophelia right open")
            show ophelia right open
        "That's honestly really embarrassing":
            show ophelia right embarrassed at LiveDissolve("ophelia right")
            ophelia "{size=*0.75}Maybe I should have confided with the tall happy boy instead{/size}"
            show ophelia right open

    ophelia "Well. Anyway, the details are unimportant. There is an event being hosted at this very city by the end of the week."
    ophelia "I'd like to aquire some limited edition memorabilia alongside a few signatures."
    ophelia "Only, one issue."
    ophelia "It's couples only."

    show ophelia right open at LiveDissolve("ophelia right negative open")

    ophelia "I don't care how you obtian a partner for the event so long as you never utter my name or refer to me {i}at all{/i} to the others under any circumstance."
    
    show ophelia right negative open at LiveDissolve("ophelia right open")
    
    ophelia "I have nothing to offer you but my gratitude in return. But I would be most appreciative if you accepted my request."

    show ophelia right

    menu:
        ophelia "I have nothing to offer you but my gratitude in return. But I would be most appreciative if you accepted my request."
        "Sure":
            pass
        "Of course":
            pass
        "I owe you anyways":
            pass

    show ophelia positive
    
    ophelia "Thank you for your readiness [player], you don't understand how muc-"

    show ophelia right -positive -open

    zhen "There you are [player]!"

    show ophelia left:
        easein 0.3 xalign 0.8
    with None
    show zhen right open:
        easein 0.3 xalign 0.2
    with Dissolve(0.1)

    # "Approaching the two of you, you see your best friend and roommate appearing quite exasperated."

    zhen "You disappeared all of a sudden! I looked {i}everywhere{/i} for you."

    zhen "Why are you even-"  
    
    show zhen right open at LiveDissolve("zhen right negative")

    zhen "Oh. Ophelia? What are you doing here?"

    show zhen right negative at LiveDissolve("zhen right")
    show ophelia open

    ophelia "Well I-I was just um..."
    ophelia "Oh my. Lost track of the time, I need to wake up Leon and Lukas."
    ophelia "You could say I became their unofficial alarm clock since they always oversleep on their own."
    ophelia "Yes, but that is all!"
    ophelia "Farewell [player]. As to you, Zhen."
    
    show ophelia right

    hide ophelia with fadeoutright
    
    "Before Zhen can respond, Ophelia wanders off down the hallway with a quickened pace."

    show zhen open

    zhen "So uh..."

    show zhen -open

    show zhen right open:
        easein 0.35 xalign 0.5
    
    show zhen left open
    
    #show zhen right open at LiveDissolve("zhen left open")

    zhen "What was she doing here?"

    show zhen left
    
    menu:
        zhen "What was she doing here?"
        "Uh, nothing of course":
            show zhen open
            zhen "I've lived with you long enough to know you're lying but since I'm so {i}thoughtful{/i} and {i}respectful{/i} of your boundaries, I won't push you to tell me anything."
            zhen "But also, of course, you can tell me anything."
        "She needed my help for her research":
            show zhen open
            zhen "Ah, that checks. I suppose we haven't seen her in a while since things have slowed down."
        "She gave me a super secret mission": #"She told me this super secret mission that I can't tell anybody"
            show zhen left at LiveDissolve("zhen left negative")
            zhen "...Oh, she's back to her weird cryptidness again. Glad I'm not involved with that."
            show zhen left negative at LiveDissolve("zhen left open")

    zhen "Oh right! I got you something."

    show zhen left

    "Zhen shoves a small paper bag right in front of your face. Grabbing it, you look into it to be hit with the scent of a cinnamon bun."

    show zhen left positive open

    zhen "It's an overpriced pastry to go with your equally overpriced coffee."

    show zhen left positive -open

    menu:
        zhen "It's an overpriced pastry to go with your equally overpriced coffee."
        "Thanks":
            pass
        "Why'd you get this for me?":
            pass
    
    show zhen open -positive

    zhen """
    It's a thanks for helping me out with my film assignment last night.
    
    You know how I am, I always get overly ambitious.
    
    But luckily I have such a good actor as a roommate.
    
    Though, your expressions could use some work. Alongside your language.
    """

    show zhen left open at LiveDissolve("zhen left negative")
    
    zhen "And yikes, not just your verbal language either but your physical one too."

    show zhen left negative

    menu:
        zhen "And yikes, not just your verbal language either but your physical one too."
        "Thanks?":
            pass
        "I think you're complaining about me":
            show zhen left negative at LiveDissolve("zhen left open")
            zhen "Of course not!"

    show zhen positive open
    zhen "You are fantastic at following orders though, which is any director's dream."

    show zhen -positive

    "As you both continue your conversation, the two of you begin to walk up to the designated meetup table finding two friends aready at the table."

    hide zhen
    with dissolve
    # continue morning dialogue

    jump rand_encounter

label morning_2:
    $ persistent.currentbkg = "dininghall"
    scene bg dininghall with fade_transistion
    show screen dvd

    "Day: [day], 
    track: [track.visits], courtyard: [courtyard.visits], gamroom: [gameroom.visits]"
    if track.route != None:
        "track: [track.route.name]"
    else:
        "track: [track.route]"
    if courtyard.route != None:
        "courtyard: [courtyard.route.name]"
    else:
        "courtyard: [courtyard.route]"
    if gameroom.route != None:
        "gameroom: [gameroom.route.name]"
    else:
        "gameroom: [gameroom.route]"
    "Zhen: [zhen.points], Leah: [leah.points], Lukas: [lukas.points],
        KD: [kd.points], Cadenza: [cadenza.points], Oriel: [oriel.points],
        Leon: [leon.points], Lynn: [lynn.points], Himitsu: [himitsu.points]"

    jump rand_encounter

label morning_3:
    $ persistent.currentbkg = "dininghall"
    scene bg dininghall with fade_transistion
    show screen dvd

    "Day: [day]"
    "track: [track.visits], courtyard: [courtyard.visits], gamroom: [gameroom.visits]"
    if track.route != None:
        "track: [track.route.name]"
    else:
        "track: [track.route]"
    if courtyard.route != None:
        "courtyard: [courtyard.route.name]"
    else:
        "courtyard: [courtyard.route]"
    if gameroom.route != None:
        "gameroom: [gameroom.route.name]"
    else:
        "gameroom: [gameroom.route]"
    "Zhen: [zhen.points], Leah: [leah.points], Lukas: [lukas.points],
        KD: [kd.points], Cadenza: [cadenza.points], Oriel: [oriel.points],
        Leon: [leon.points], Lynn: [lynn.points], Himitsu: [himitsu.points]"

    jump rand_encounter

label morning_4:
    $ persistent.currentbkg = "dininghall"
    scene bg dininghall with fade_transistion
    show screen dvd

    "Day: [day]"
    "track: [track.visits], courtyard: [courtyard.visits], gamroom: [gameroom.visits]"
    if track.route != None:
        "track: [track.route.name]"
    else:
        "track: [track.route]"
    if courtyard.route != None:
        "courtyard: [courtyard.route.name]"
    else:
        "courtyard: [courtyard.route]"
    if gameroom.route != None:
        "gameroom: [gameroom.route.name]"
    else:
        "gameroom: [gameroom.route]"
    "Zhen: [zhen.points], Leah: [leah.points], Lukas: [lukas.points],
        KD: [kd.points], Cadenza: [cadenza.points], Oriel: [oriel.points],
        Leon: [leon.points], Lynn: [lynn.points], Himitsu: [himitsu.points]"

    jump rand_encounter

label morning_5:
    $ persistent.currentbkg = "dininghall"
    scene bg dininghall with fade_transistion
    show screen dvd

    "Day: [day]"
    "track: [track.visits], courtyard: [courtyard.visits], gamroom: [gameroom.visits]"
    if track.route != None:
        "track: [track.route.name]"
    else:
        "track: [track.route]"
    if courtyard.route != None:
        "courtyard: [courtyard.route.name]"
    else:
        "courtyard: [courtyard.route]"
    if gameroom.route != None:
        "gameroom: [gameroom.route.name]"
    else:
        "gameroom: [gameroom.route]"
    "Zhen: [zhen.points], Leah: [leah.points], Lukas: [lukas.points],
        KD: [kd.points], Cadenza: [cadenza.points], Oriel: [oriel.points],
        Leon: [leon.points], Lynn: [lynn.points], Himitsu: [himitsu.points]"

    jump choose_ending