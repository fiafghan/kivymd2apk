from kivy.core.audio import SoundLoader


def play_sound (sound_file):
    click_sound = SoundLoader.load(sound_file)
    click_sound.play()
