style tx_button:
    color "#000"
    hover_color '#EC008C'

style button_sound:
    hover_sound "audio/button_hover.wav"
    activate_sound "audio/button_click.wav"

transform quarter_size:
    zoom 0.25

screen MapUI():
    # window hide
    
    frame:
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 1080
        background None

        textbutton "Track":
            style "button_sound"
            text_style "tx_button"
            xpos 1550
            ypos 750

            action Jump("track")
        
        textbutton "Courtyard":
            style "button_sound"
            text_style "tx_button"
            xpos 400
            ypos 500

            action Jump("courtyard")

        textbutton "Game Room":
            style "button_sound"
            text_style "tx_button"
            xpos 600
            ypos 300
            
            action Jump("gameroom")

        imagebutton:
            style "button_sound"
            mouse "hover"
            xpos 1470
            ypos 390
            idle "images/blankImage.png" at quarter_size
            
            action Jump("dorms")
