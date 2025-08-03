screen MusicNote(points):
    timer 0.5 action Hide("MusicNote")

    if points == 1:
        image "gui/musicnotes/DME_musicnote_1.png" xalign 0.75 yalign 0.5:
            at my_transf
    elif points == 2:
        image "gui/musicnotes/DME_musicnote_2.png" xalign 0.75:
            at my_transf
    else:
        image "gui/musicnotes/DME_musicnote_3.png" xalign 0.75:
            at my_transf

transform my_transf:
    on show:
        parallel:
            alpha 0.0
            easeout 0.25 alpha 1.0
        parallel:
            yalign 0.25
            easein 0.55 yalign 0.15
            
    on hide:
        easeout 0.75 alpha 0.0