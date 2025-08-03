
screen dvd():
    zorder 2
    frame:
        if timeofday == 0:
            background "gui/HUD/HUD_Morning.png"
        elif timeofday == 1:
            background "gui/HUD/HUD_Afternoon.png"
        else:
            background "gui/HUD/HUD_AfterSchool.png"
        xpos 20
        ypos 25

        hbox:
            add "gui/HUD/dvd.png" at spin
            
            vbox:
                xpos -10
                ypos -2
                hbox:
                    text dates[day - 1] style "date_style"
                    text weekdays_short[day - 1] style "weekday_style"
                    spacing 35
                if timeofday == 0:
                    text "Morning" style "morning_style"
                elif timeofday == 1:
                    text "Afternoon" style "time_style"
                else:
                    text "After School" style "time_style"

transform spin:
    subpixel True
    xpos -18
    ypos -18
    rotate 0
    linear 10.0 rotate 360
    repeat

style date_style:
    color "#251F1F"
    font "fonts/PTSansNarrow-Bold.ttf"
    size 40

style weekday_style:
    font "fonts/PTSansNarrow-Bold.ttf"
    # xalign 0.0
    xpos -5
    ypos 1
    size 40
    color "#E7E8E9"

style morning_style:
    font "fonts/PTSansNarrow-Bold.ttf"
    size 64
    color "#251F1F"
    ypos -15
    xpos 8

style time_style:
    font "fonts/PTSansNarrow-Bold.ttf"
    size 64
    ypos -12

transform weekday_transform:
    alpha 0.0 xalign .10 yalign .40
    ease 0.6 alpha 1.0 xalign .40
    pause 0.9
    ease 0.5 alpha 0.0 xalign .80

transform previous_time_transform:
    alpha 0.0 xalign .50 yalign .50
    ease 0.1 alpha 1.0
    pause 0.5
    ease 0.2 alpha 0.0 xalign 0.4

transform current_time_transform:
    alpha 0.0 xalign .60 yalign .50
    pause 0.8
    ease 0.3 alpha 1.0 xalign .50
    pause 0.9
    ease 0.4 alpha 0.0 xalign .40

style time_text:
    size 65

screen time_change():
    # key "dismiss" action NullAction()
    # text "[weekday]" style "time_text" xalign 0.4 yalign 0.4
    showif timeofday == 2:
        text weekdays_long[day - 1]
    text timesofday[timeofday] style "time_text" at previous_time_transform
    text timesofday[(timeofday + 1)%3] style "time_text" at current_time_transform
    # call(None)

#screen day_change():


# screen time_change():
#     text "[weekday]" style "time_text" xalign 0.4 yalign 0.4
#     text "[previous_time]" style "time_text" at previous_time_transform
#     text "[current_time]" style "time_text" at current_time_transform

# screen day_change():
#     showif day == 1:
#         text "Monday" style "time_text" at weekday 
#     elif day == 2:
#         text "Tuesday" style "time_text" at weekday
#     elif day == 3:
#         text "Wednesday" style "time_text" at weekday
#     elif day == 4:
#         text "Thursday" style "time_text" at weekday
#     else:
#         text "Friday" style "time_text" at weekday
    
#     text "[timeofday]" style "time_text" at timeofday