label rand_encounter_zhen:
    $ persistent.currentbkg = "hallway"
    scene bg hallway with fade
    show screen dvd

    show zhen right negative:
        xalign 0.25
    with Dissolve(0.1)

    "As you're approaching the dininghall, you spot Zhen standing outside a classroom door. Instead of continuing your path, you begin to make your way towards your lone roommate."

    show zhen right negative at LiveDissolve("zhen right open"):
        easein 0.4 xalign 0.5

    zhen "[player]!"

    zhen "Our paths have crossed yet again today."

    zhen "I guess you really can’t get enough of me."

    show zhen right

    menu:
        zhen "I guess you really can’t get enough of me."
        "What are you doing?":
            pass
        "Why are you hanging around in the hallways?":
            pass

    show zhen right at LiveDissolve("zhen right negative")

    "Zhen lets out an annoyed groan."

    zhen "It’s a whole mess. I don’t even know if I have the time to tell you everything."

    zhen "..."

    show zhen right negative at LiveDissolve("zhen right open")

    zhen """

    I mean, if you're just {i}dying{/i} to hear about it...

    So, there’s this actress I'm working with for my group project and we had to turn in our scripts today.

    She had it last because she was soooo insistent on writing everything down.
    """

    show zhen right open at LiveDissolve("zhen right negative")

    zhen """
    Then {i}of course{/i} she chose the day it’s {i}due{/i} to not go to school.

    So now she needs her roommate drop it off 'cause she doesn’t want to get in trouble for skipping.

    Which is honestly far more work than just comming to school today and turning it in herself.

    Or, I don’t know, letting someone else in the group write everything down instead!

    But nooooo {i}\"I have to write it down cause my hand writing’s the prettiest\".{/i}

    And for {i}some{/i} reason, I was the one in the group forced to fix this little mess up.

    Like, why {i}me{/i}!? I want to enjoy my lunch too, not stand around waiting on some mysterious roommate!!
    """

    menu:
        zhen "Like, why {i}me{/i}!? I want to enjoy my lunch too, not stand around waiting on some mysterious roommate!!"
        "Maybe she's not in school for a reason":
            $ zhen.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
            zhen "Whatever the reason, she could've handled it a lot sooner than the period {i}right before{/i} the class!"
            #show zhen right negative at LiveDissolve("zhen right")
        "I hate people like her too":
            $ zhen.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
            zhen "Believe me, especially in the acting program, there's so many people like her. Frankly, it's getting real annoying."
            #show zhen right negative at LiveDissolve("zhen right")
        "You're just that realiable": #, you've helped me so often
            $ zhen.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"
            show zhen right negative at LiveDissolve("zhen right open")
            zhen.c "Well, if that's the case, I guess I can't let my group down! {size=*0.75}{i}Unlike that stupid flake.{/i}{/size}"
            show zhen right

    show zhen right at LiveDissolve("zhen right")
    
    "You both hear the bell ring, causing many lingering students to rush into a room. Zhen lets out a sigh and waves you away."

    show zhen open

    zhen "Ah, I should let you head to lunch now."

    zhen "Thanks for listening to me vent though."

    zhen "I’ll see you after school!"

    show zhen -open

    $ quick_menu = False
    hide screen dvd
    scene black with fade_transistion

    "You wave back to Zhen as you hurry into the dininghall before a teacher catches you."

    $ zhen.set_rand_1()

    return

label rand_encounter_leah:
    $ persistent.currentbkg = "hallway"
    scene bg hallway with fade_transistion
    show screen dvd

    "You're making your way towards the dininghall until you almost step on a fallen flyer."

    show leah right:
        yalign 0.0 xalign 0.5
        easeout 0.2 yalign -0.1
        easein 0.2 yalign 1.0
    with Dissolve(0.1)
    
    "You reach down to pick it up and on the way back up, almost accidentally bump into Leah who seems to have dropped it."
    
    "You pass the flyer over to her before she has the chance to speak."

    show leah positive open

    leah "Oh! Thank you, [player]."

    show leah -positive

    leah "Normally I’d be eating lunch right about now, but the student council needed extra help putting up event posters."

    show leah right open at LiveDissolve("leah right negative open")

    leah "I didn’t expect it to bleed into lunch time."

    show leah right negative

    menu:
        leah "I didn’t expect it to bleed into lunch time."
        "Can I help you?":
            pass
        "Do you need help?":
            pass
    
    show leah right negative at LiveDissolve("leah right positive open")

    leah "Actually, yeah. I think I could use some help."

    show leah right open

    leah "You'll miss some of lunch though."

    show leah -open

    "You shrug and take a small stack out of Leah's hands. It didn't take very long until the stack was fully hung up."

    show leah open

    leah "Thanks again [player]!"

    show leah -open

    menu:
        leah "Thanks again [player]!"
        "What are the flyers for?":
            pass
        "What's the event?":
            pass
    
    show leah open

    leah "The school’s hosting a music festival to raise some money for charity."

    leah "The student council has been real busy with the event prep in hopes that it'll 
            be more successful than the last one."

    show leah right open at LiveDissolve("leah right negative open")

    leah "With how low the attendance was {i}last{/i} time, I do hope our efforts pay off this time."

    show leah right negative

    menu:
        leah "With how low the attendance was, I do hope our efforts pay off this time."
        "We should go together":
            $ leah.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"
            show leah right negative at LiveDissolve("leah right positive open")
            leah "That'd be really nice! I normally go to these kinds of things alone so some company 
                    would be much appreciated."
            show leah right positive open at LiveDissolve("leah right open")
        "With you working on it, I know it'll be successful":
            $ leah.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
            show leah right negative at LiveDissolve("leah right open")
            leah "That's very kind of you, but I shouldn't be taking all the credit."
        "You shouldn't stress yourself out about it":
            $ leah.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
            show leah right negative at LiveDissolve("leah right open")
            leah "Yeah... Well, thanks to your help, that's one less worry."

    show leah right open
    
    leah "Apologies for holding you up for so long. Let's go out for some lunch!"

    leah "There's this place that just opened up and it has amazing milkshakes. I think you'd really like it!"

    leah "My treat of course."

    show leah right

    $ quick_menu = False
    hide screen dvd
    scene black with fade_transistion

    "You and Leah head out of the campus together, spending the rest of lunch period trying out these famous milkshakes."

    return

label rand_encounter_lukas:
    $ persistent.currentbkg = "dininghall"
    scene bg dininghall with fade_transistion
    show screen dvd

    "You enter the dininghall and are immediately faced with a group of friends play fighting each other. 
    One of them bumps into you harshly and you almost topple over."
    
    "Before your inevitable fall, someone manages to pull you upright."

    show lukas:
        xalign 0.5
        easeout 0.25 xalign 0.6
        easein 0.25 xalign 0.5

    lukas "You good man?"

    "Before you manage to say anything, Lukas looks you over and seems to come to a decision. 
    He begins to drag you away from the group, waving them off."

    lukas "Here, let's get you some water."

    lukas "Sorry about that by the way."

    menu:
        lukas "Sorry about that by the way."
        "Are they your friends?":
            pass
        "Do you know them?":
            pass

    "Lukas dramatically rolls his eyes."

    lukas "Don't act so shocked."

    lukas "I have so many friends outside of you and the others."

    lukas "Y'know. Since I'm so charismatic and popular."

    menu:
        lukas "Y'know. Since I'm so charismatic and popular."
        "...":
            pass
        "Popular?":
            pass
    
    lukas """
    
    uh

    OKAY WELL not {i}everyone{/i} can be the child of two famous celebrities!

    Nah but for real, they're just some bandmates.

    Well, not really bandmates. More like a group I play with sometimes?

    We're not actually a {i}band{/i} band.

    It's not like we perform live or anyting.

    I'm in it to improve my guitar skills and I'm only okay at it so it'd make for a pretty shitty performance anyways.
    """

    menu:
        lukas "I'm in it to improve my guitar skills and I'm only okay at it so it'd make for a pretty shitty performance anyways."
        "Being able to play so many instruments is already impressive":
            $ lukas.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
            lukas "Not so impressive if you're not that great at any of them."
            lukas "Like \"jock of all trades but master of nothing\" or something. However that saying goes. I think I heard Leah say it once."
        "I bet it'd still be a pretty cool performance":
            $ lukas.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
            lukas "Maybe maybe."
            lukas "I guess if you give us some time, we can make a pretty neat set."
            lukas "Simple, but neat."
        "Can I at least hear you guys play?":
            $ lukas.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"
            lukas "They did say they've always wanted us to have at least one fan."
            lukas "Maybe I'll hold you up to that offer sometime."
        
    "Without realizng, you both made it to the other side of the dininghall with the water fountains."
    
    "You quickly get your fix of water and are slightly surpised to still see Lukas standing beside you."

    lukas "C'mon, I still haven't picked up lunch yet."

    "Lukas urges you to a lunchline as his bandmates make their way over."

    $ quick_menu = False
    hide screen dvd
    scene black with fade_transistion

    "You end up spending the rest of the period sitting besides him and his group of bandmates."

    return

label rand_encounter_kd:
    $ persistent.currentbkg = "hallway"
    scene bg hallway with fade_transistion
    show screen dvd

    show kd:
        xalign 0.9
        easein 0.35 xalign 0.45
        easeout 0.2 xalign 0.5

    "As you’re walking down the hallway, you notice KD rushing down the hall towards you with a 
    towering pile of stuff in his arms."

    #show kd:
    #    easeout 0.35 xalign 0.5

    "You aren't able to get out of the way in time and KD ends up running headfirst into you. 
    Luckily, you manage to stablize the pile before the hallway becomes a mess." with hpunch

    kd "Oh! [player], I'm so sorry- I didn't see you there."

    menu:
        kd "Oh! [player], I'm so sorry- I didn't see you there."
        "What's the big rush?":
            pass
        "Are you... okay?":
            pass
    
    kd "I've kind of bitten off more than I can chew."

    kd "Promised a teacher to help deliver stuff from the dorms to his classroom but now I might end up late to my internship."

    menu:
        kd "Promised a teacher to help deliver stuff from the dorms to his classroom but now I might end up late to my internship."
        "Let me deliver it for you":
            kd "Oh no no I couldn't ask you to do all that. Just a few things would already be more than enough help."
        "I can help":
            kd "Actually, that'd be great."


    kd "Here, you can help carry the smaller stuff."

    "KD passes over some of the boxes that sat atop the tower he's still balancing and you proceed to follow him down the hallway."

    "Only to be suddenly stopped by a random girl. She looks like an upperclassman."

    "Panicked Upperclassman" """
    
    Oh my god, KD! I really need your help.

    Soo you know Tyler, right? The big dude? Well, yeah, he's on vacation and our group needs a replacement for him pronto.

    Our performance is only a few days from now.

    And then I remembered that you scored that internship with Maganate so I know you gotta be able to pick up new roles real quick.

    You're, like, one hell of an actor after all.
    """

    kd "Ah, I'm really busy right now. I don't know..."

    "Panicked Upperclassman" "Please please please- KD we’re gonna fail the project without a replacement!"

    kd "Okay, okay, I'll do it."

    kd "Just send me the script soon, I'll look it over tonight."

    "Panicked Upperclassman" "You're a life saver you know that KD?"

    "KD chuckles lightly and takes a glance at his watch. He turns from her and nudges you to continue walking."

    kd "I really gotta go now. Sorry for making this so brief!"

    "You and KD continue to speedwalk to the classroom. Once out of earshot of the upperclassman, you glance back over at KD."

    menu:
        "You and KD continue to speedwalk to the classroom. Once out of earshot of the upperclassman, you glance back over at KD."
        "You really love helping people":
            $ kd.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
            kd "I really do but trust me, if I had it in me to say \"no\" to people more often, I'd do it in a heart beat."
        "You should've told her no":
            $ kd.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
            kd "Gosh, I would've beat myself up if she did end up failing that project!"
            kd "It's fine. The script should be short anyways."
        "Getting more work to do can't be good for you":
            $ kd.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"
            kd "Yeah, doing all this on top of saving the world has been making my back sore more often."
            kd "Maybe taking a break is well warrented at this point."

    "You both finally make it to the classroom. The teacher manages to thank both you and KD before KD rushes out of the classroom."

    "KD sends you a quick wave and \"thank you\" then he's gone."
    
    $ quick_menu = False
    hide screen dvd
    scene black with fade_transistion

    "You begin to backtrack to where you were heading before."

    return

label rand_encounter_cadenza:
    $ persistent.currentbkg = "dininghall"
    scene bg dininghall with fade_transistion
    show screen dvd
    
    "You enter the dininghall and make your way towards the lunch line. On the way there, 
    you overhear a conversation happening beside the line."
    
    "To your suprise, you realize the conversation is between Cadenza and an obnoxious sounding student."

    show cadenza:
        xalign 0.4

    "Unpleasant Boy" "Come on, Cadenza. I thought we had a spark when we played the leads in last semester's musical."

    "Unpleasant Boy" "You really gonna say no after all that?"

    cadenza "Again, I really don't reciprocate your feelings but I'm flattered."

    "Unpleasant Boy" "Our character were sooo into each other too! I thought you were realy feeling it."

    cadenza "We must have been acting in two different musicals then because my character still ended up rejecting your character."

    "Unpleasant Boy" "But that's just a play, come on."

    cadenza "Exactly. So whatever \"spark\" you felt was because I was {i}acting{/i}. In a {i}play{/i}."

    "Cadenza glances around for an out and zeros in on you approaching the area. 
    She grabs a hold of your arm, quickly tugging you over to join in on the conversation."

    cadenza "Besides, I already have a date for the event anyways."

    menu:
        cadenza "Besides, I already have a date for the event anyways."
        "I can't wait to bring my honeybuns":
            $ nickname = "honeybuns"
        "Please quit talking to my little caviar":
            $ nickname = "little caviar"
    
    "The boy looks between you and Cadenza with a raised eyebrow. You remain in a staring contest for a few seconds 
    before he lets out a groan and walks away."

    "You and Cadenza stand together in silence for a moment until Cadenza breaks it with hysterical laughter."

    cadenza "Oh...my...god!"

    cadenza "I can't believe that worked!"

    cadenza "Thanks so much [player]!"

    cadenza "I think I've been spending a little too much time with Lynn because it you weren't there, 
    I think I fully would've killed the guy."

    menu:
        cadenza "I think I've been spending a little too much time with Lynn because it you weren't there, I think I fully would've killed the guy."
        "You should've":
            $ cadenza.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
            cadenza "As long as you promise to help bury the body!"
            cadenza "...Wow, I think I really {/i}have{/i} been spending too much time with her."
            cadenza "But, hey, at least now I know you'd cover for me."
        "Good thing we avoided a murder, [nickname]":
            $ cadenza.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"
            "Cadenza seems caught off guard and almost falls over in renewed laughter, holding onto your shoulder for support."
            cadenza "Stop! You're going to end up killing {i}me{/i}!"
        "So... I'm taking you out to the event?":
            $ cadenza.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
            cadenza "You trying to score a date too?"
            cadenza "..."
            cadenza "Maybe I'll think about it."

    "Cadenza ends up joining you in line, recounting a few funny confessions she's had to you." 

    $ quick_menu = False
    hide screen dvd
    scene black with fade_transistion
    
    "You both enjoy your lunch together without interuption."
    
    return

label rand_encounter_oriel:
    $ persistent.currentbkg = "dininghall"
    scene bg dininghall with fade_transistion
    show screen dvd
    
    "As you're walking across the dininghall to throw away your trash, you notice a familiar blob of black hair 
    resting on top of a table."
    
    show oriel
    
    "When you get closer to greet them, you begin to notice a few weird things."

    "Like how a bitten apple was resting in limp hands or how their body was completely stiff."
    
    "...Was he even breathing?"
    
    menu:
        "...Was he even breathing?"
        "Shake them":
            "You begin to hover over him, frantically shaking him to get a reaction. 
            It didn’t take long for his head to shoot up in shock and knocking right into yours."
            oriel "Ow.. what the fuck?"
        "Call out their name":
            "You say his name but he doesn’t move. You say it again, slightly louder, but still no response."
            "In the loudest voice you can muster in a public space, you say their name one last time."
            "You hear Oriel groan from against the table and lift his head up."

    "Oriel looks up at you in agitation."

    oriel.c "What are you doing here [player]?"

    menu:
        oriel "What are you doing here [player]?"
        "Lunch is almost over":
            oriel "Oh..."
        "I though you were dead":
            oriel "Sorry... about that."
    
    "You follow Oriel's lingering gaze to behind you. The dininghall is rapidly emptying with students, the bell must have went off not too long ago."

    oriel "You can go now though."

    oriel "..."

    oriel "Thanks for waking me up."

    "Oriel begins to clean up his mostly uneaten lunch. Instead of leaving the now empty dininghall you stay back and pick up some lingering trash left behind from Oriel."

    oriel "I'm going to make you late."

    menu:
        oriel "I'm going to make you late."
        "It's okay":
            pass
        "I'd probably be late anyways":
            pass
    
    "Oriel looks at you skeptically but throws out the rest of his trash and gathers his bag to leave the dininghall. You follow beside him as he heads towards what you assume to be his next class. You dig into your bag and pull out a bag of chips and nudges it towards them."

    oriel "Wha-?"

    oriel "Why are you giving me those?"

    menu:
        oriel "Why are you giving me those?"
        "You couldn't finish your lunch":
            $ oriel.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
            oriel "It's fine."
            oriel "I ate enough but thanks."
        "You like this brand, right?":
            $ oriel.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"
            oriel "Uh...yeah."
            oriel "Thanks."
        "It's a post-nap snack":
            $ oriel.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
            oriel "..."
            oriel "That's dumb."

    "Oriel takes the bag from your hands and you both proceed to walk to where his class was located (which was luckily very close). You reach the door to his classroom and midway walking into it he looks up at you."

    oriel "Please don't be too late to your class."

    oriel "..."

    oriel "I hope to see you later."

    "They fully walk into the classroom before you could respond so you decided to just head straight to class."

    "Like in another building far away."

    protag "..."

    $ quick_menu = False
    hide screen dvd
    scene black with fade_transistion

    "You end up being extremely late to class."

    return

label rand_encounter_leon:
    $ persistent.currentbkg = "hallway"
    scene bg hallway with fade_transistion
    show screen dvd
    
    "You’re walking down the hallways towards the dininghall. On the way there, you pull out your phone to look through missed any notifications, texts, and -"

    leon "Woah man, watch out!"

    "You feel hands, seemingly from the floor, grab onto your leg to prevent you from moving."

    "You look down to the sight of Leon crouched on the hallway floor, sitting beside the object you were about to kick over. A paint bucket."

    show leon

    leon "Maaan, I would've gotten in so much trouble if that fell over."

    menu:
        leon "Maaan, I would've gotten in so much trouble if that fell over."
        "Sorry":
            leon "No no- it's really no biggie."
            leon "I don't really call all that much about this whole mural-painting-thingy."
        "You paint?":
            leon "Pfft- NO!"
            leon "God, I {i}so{/i} don't want to be doing this right now."
    
    "You look against the wall and notice a new, in-progress mural and besides Leon sat a few other students each working on a portion of the painting."

    menu:
        "You look against the wall and notice a new, in-progress mural and besides Leon sat a few other students each working on a portion of the painting."
        "Why did they ask you to paint?":
            leon "Funny thing is, they didn't."
        "Then don't...paint?":
            leon "I can't just walk away and stop. I'd get into so much trouble for that too."
    
    leon "I owe this guy in one of my art classes."

    leon "And he just so happens to be a painter."

    leon "{i}And{/i} was tasked to help with this mural."

    leon "{i}And{/i} doesn’t want to do this mural."

    leon "{i}And{/i} knows a guy that owes him..."

    leon "And unfortunately... I’m that guy."

    "Leon heaves a deep sigh."

    leon "So now I'm just wasting away during lunch doing something I suck at."

    "You look back over to the work Leon had already completed. It seems he got tasked with painting a blue background."

    "But as you look up towards his more recent brushstrokes, they seem to get worse in quality."

    "At some point, Leon seems to have given up entirely based on the bored cat doodles in blue paint that will soon be covered up and filled in."

    leon "...Is this what Lukas feels like whenever he vents to me?"

    menu:
        leon "...Is this what Lukas feels like whenever he vents to me?"
        "But Lukas is actually good at what he does":
            $ leon.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
            leon "Alright, alright. Fair enough."
            leon "I can take being considered an inferior Lukas."
        "Your painting isn't that bad":
            $ leon.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
            "Leon quirks an eyebrow up at you and glances back towards what he had already completed."
            leon "I can't believe you just implied I could be somewhat bad at painting a blue background. Ouch."
        "At least the cats are cute?":
            $ leon.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"
            "Leon chuckles lightly."
            leon "They're the one thing keeping me going."
            "Leon points to a lopsided cat he painted"
            leon "I named this one Bartholo-mew."
            
    "Before your conversation can continue, the bell rings."

    leon "Just because I gotta suffer, doesn't mean you gotta too."

    leon "Enjoy lunch man."

    $ quick_menu = False
    hide screen dvd
    scene black with fade_transistion

    "You wave Leon goodbye as you watch him continue to lazily paint his section of the mural."

    return

label rand_encounter_lynn:
    $ persistent.currentbkg = "dininghall"
    scene bg dininghall with fade
    show screen dvd
    
    """
    You enter the dininghall fairly late due to being held back in your previous class.
    
    As you walk in, you're immediately greeted with... a mini dance party? A semi mosh?
    
    You decide to ignore the loud music and cluster of bodies in favor of lunch.
    """

    lynn "[player]? [player]!"

    show lynn with Dissolve(0.1)

    "You see Lynn within the crowd of dancing students. She gestures for you to come over and you follow."

    lynn "You came at the perfect time!"

    lynn "Come dance with me!"

    "Without saying anything further, she grabs your wrists and playfully moves your arms up and down to the beat of the music playing in the background."

    lynn "You're so stiff. Come on, loosen up!"

    "Lynn moves her hands from your wrists to your shoulders and starts to move them a bit more aggressively than she had with your arms."

    menu:
        "Lynn moves her hands from your wrists to your shoulders and starts to move them a bit more aggressively than she had with your arms."
        "I don't know how to dance":
            lynn "Wha- everyone has a little boggie in them!"
        "I don't like dancing":
            lynn "Lameeee excuse. You willingly came over here! You totally knew what was coming."
    
    lynn "Like, c'mon, you've had to have, like, danced to {i}something{/i} before and had the time of your life!"

    lynn "Like when you do the Chu Chu Glide at a wedding full of drunk adults!"

    menu: 
        lynn "Like when you do the Chu Chu Glide at a wedding full of drunk adults!"
        "Chu Chu Glide?":
            pass
        "I don't know what you're talking about":
            pass

    "Lynn lets out a very dramatic gasp. One that can be clearly heard over the already blaring music."

    lynn "You don't know what the Chu Chu Glide is??"

    "You shake your head."

    lynn "YOU'VE NEVER DANCED TO THE CHU CHU GLIDE BEFORE?!?!"

    "You continue to shake your head."

    "Lynn wordlessly releases her hold on your shoulders and rushes to the speakers at the front of the crowd."

    "A few seconds pass as the current song fades out into something else. Suddenly, the crowd begins to clap their hands and move into a series of more organized lines."

    "Lynn quickly runs back over and plants herself right next to you."

    lynn "Just follow my lead."

    lynn "You'll love this, trust!"

    "Lynn guids you through the dance instructions of the song that everyone else in the crowd already knew."

    "And you hate to admit it."
    extend "But."
    extend "It was kinda..."
    extend " fun."

    "As the song ends, you hear Lynn cheering next to you."

    lynn "Wasn't that fun!?"

    lynn "Life changing!!"

    lynn "Perhaps you had the..."

    lynn "Time of your life?"

    menu: 
        lynn "Time of your life?"
        "But it wasn't a wedding?":
            $ lynn.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
            lynn "Ah, you're right!"
            lynn "Don't worry! Best believe at my wedding, your life will change just by the sheer amount of \'the time of your li-"
            lynn "Times of?"
            lynn "Whatever"
            lynn "You'll have the time of your life for sure!"
        "Only a little life changing":
            $ lynn.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
            lynn "Oh don't act like thaaat."
            lynn "You were all wide eyed in awe!"
            lynn "..."
            lynn "Or maybe it was in fear?"
        "Chu Chu real smooth":
            $ lynn.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"
            lynn "Now that's the spirit!"
            "Lynn grabs your wrists and moves your arms around to mimic the dance move."
            "This time you've loosened up significantly more and are able to match her movements."

    "As you both continue to shuffle to the music, a loud growl in your stomach interrupts your little dance."

    lynn "Oh right, you were probably on your way to get some food."

    lynn "Sorry, you can go now."

    lynn "But of course, when you're done eating, you know where to find me!"

    "Lynn shoots you finger guns at you with a wink before waving you away."

    $ quick_menu = False
    hide screen dvd
    scene black with fade_transistion

    "You end up finishing lunch with some time to spare. Maybe just enough time to spend dancing with Lynn before the bell rings and you head to class."

    return

label rand_encounter_himitsu:
    $ persistent.currentbkg = "dininghall"
    scene bg dininghall with fade_transistion
    show screen dvd
    
    show himitsu with Dissolve(0.1)

    "You enter the dininghall and you notice Himitsu sitting alone staring at... nothing?"

    "Feeling concerned now, you make your way over to her table and take a seat next to her."

    "Right as you open your mouth to ask if she was okay, she quickly puts her own hand over it before you could get a word out."

    "You glance at her with a raised eyebrow and she responds by pointing to a group of kids across the way."

    "Gossiping Student" "Ok ok, let me get to the point!"

    "Impatient Student" "Sorry sorry!!"

    "Gossiping Student" "Listen, you can't tell anyone else about this cause, like, the admin still doesn't know who did it."

    "Gossiping Student" "But Tyler found out about her racist comments, so guess what he did to her."

    "Nosy Student" "What, WHAT?!"

    "Gossiping Student" "Y'know that bright-ass pink wig she always wears?"

    "Impatient Student" "Oh. My. God."

    "Gossiping Student" "YUP!"

    "Gossiping Student" "He took that wig off!"

    "Nosy Student" "STOP!!!!"

    "Gossiping Student" "But guess what."

    "Gossiping Student" "THERE WAS ANOTHER WIG!"

    "The table erupted in laughter and you couldn't help but chuckle a bit, coming out muffled underneath Himitsu's hand."
    
    "You glance over at her and see a familiar deadpan expression, but it was obvious she was invested in the story."

    "She catches your eye and quickly removes her hand from your mouth."

    himistu "Sorry, I just didn't want them to realize that we could hear them."

    menu: 
        himistu "Sorry, I just didn't want them to realize that we could hear them."
        "Didn't know you were one for gossip":
            $ himitsu.add_points(2)
            show screen MusicNote(2)
            play sound "audio/point_2.wav"
            himitsu "I'm not, but it's fascinating to listen to."
            himistu "I love listening to people's reactions, especially the more dramatic ones."
            himitsu "..."
            himitsu "I guess that would be considered \'one for gossip\'."
        "Will your next book feature a girl with two wigs?":
            $ himitsu.add_points(3)
            show screen MusicNote(3)
            play sound "audio/point_3.wav"
            himitsu "No."
            himitsu "But I wasn't listening for nothing."
            himitsu "I don't really embody the stereotypical high school experience so..."
            himitsu "Ah. But I've found lunch room drama to be a good reference point."
        "Isn't this borderline stalking?":
            $ himitsu.add_points(1)
            show screen MusicNote(1)
            play sound "audio/point_1.wav"
            "Himitsu shrugs."
            himitsu "It's a public location and they're talking loud enough to hear from all the away over here."
            himitsu "It's more of an invasion of privacy rather than stalking."

    "Himitsu jots down something down into her notebook and then looks back up at you."

    himistu "Oh right, did you come over to eat lunch with me?"

    menu:
        "Yeah":
            pass
        "If I do, will we eavesdrop more?":
            himitsu "Eavesdropping is illegal, we're not doing that."
            himitsu "We just happened to overhear conversations that pass our way."

    $ quick_menu = False
    hide screen dvd
    scene black with fade_transistion
    
    "You spend the rest of your lunch in silence sitting besides her."
    
    "You end up overhearing more conversations that certainly alter your perception of some of your classmates before the bell rings and you both part ways."

    return