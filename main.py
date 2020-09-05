basic.show_icon(IconNames.HEART)

def on_forever():
    basic.show_icon(IconNames.HEART)
    basic.pause(500)
    basic.clear_screen()
    basic.pause(500)
basic.forever(on_forever)
