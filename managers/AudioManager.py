import pygame


class AudioManager:
    def __init__(self, game):
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.init()

        self.game = game
        self.sfxs = dict()

    def set_music_volume(self, vol):
        pygame.mixer.music.set_volume(vol)

    def set_sfx_volume(self, vol):
        for sfx in self.sfxs.values():
            sfx.set_volume(vol)

    def load_bgm(self, bgm):
        pygame.mixer.music.load(bgm)

    def play_bgm(self):
        pygame.mixer.music.play(-1)

    def pause_bgm(self):
        pygame.mixer.music.pause()

    def resume_bgm(self):
        pygame.mixer.music.unpause()

    def stop_bgm(self):
        pygame.mixer.music.stop()

    def load_sfx(self, sfx_name, sfx_path):
        self.sfxs[sfx_name] = pygame.mixer.Sound(sfx_path)

    def play_sfx(self, sfx_name):
        if sfx_name in self.sfxs:
            self.sfxs[sfx_name].play()

    def clear(self):
        pygame.mixer.music.unload()
        self.sfxs.clear()
