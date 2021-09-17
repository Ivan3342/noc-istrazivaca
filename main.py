def btnA():
    music.start_melody(music.built_in_melody(Melodies.POWER_UP))

def btnB():
    music.start_melody(music.built_in_melody(Melodies.POWER_DOWN))

input.on_button_pressed(Button.A, btnA)
input.on_button_pressed(Button.B, btnB)