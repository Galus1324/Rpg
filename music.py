from pygame import mixer

# for  sound
mixer.init()
mixer.set_num_channels(2)

typing_sound = mixer.Sound("music/sound.mp3")
village_music = mixer.Sound("music/village_music.mp3")
jungle_music = mixer.Sound("music/jungle_music.mp3")
final_boss_music = mixer.Sound("music/final_boss.mp3")
epic_fight_music = mixer.Sound("music/epic_fight_music.mp3")
dungeon_music = mixer.Sound("music/dungeon_music.mp3")

channel1 = mixer.Channel(0)
channel2 = mixer.Channel(1)

channel1.set_volume(0.2)
channel2.set_volume(0.5)

def play_sound(sound, channel):
    channel.play(sound, loops=-1)