import pygame

from utils.resourceUtils import resource_path


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
            sfx["channel"].set_volume(vol)

    def load_bgm(self, bgm_path):
        pygame.mixer.music.set_volume(self.game.settings_manager.getSetting("music_volume"))
        pygame.mixer.music.load(resource_path(bgm_path))

    def play_bgm(self):
        pygame.mixer.music.play(-1)

    def pause_bgm(self):
        pygame.mixer.music.pause()

    def resume_bgm(self):
        pygame.mixer.music.unpause()

    def stop_bgm(self):
        pygame.mixer.music.stop()

    def load_sfx(self, sfx_name, sfx_path):
        channel_id = None

        sfx_path = resource_path(sfx_path)

        if self.sfxs.get(sfx_name) is None:
            channel_id = len(self.sfxs)
            pygame.mixer.set_num_channels(channel_id + 1)
            channel = pygame.mixer.Channel(channel_id)
            channel.set_volume(self.game.settings_manager.getSetting("sfx_volume"))
        else:
            channel_id = self.sfxs[sfx_name]["channel_id"]
            channel = self.sfxs[sfx_name]["channel"]

        self.sfxs[sfx_name] = {
            "channel_id": channel_id,
            "channel": channel,
            "sfx": pygame.mixer.Sound(sfx_path)
        }

    def play_sfx(self, sfx_name):
        if sfx_name in self.sfxs and not self.sfxs[sfx_name]["channel"].get_busy():
            self.sfxs[sfx_name]["channel"].play(self.sfxs[sfx_name]["sfx"])

    def clear(self):
        self.sfxs.clear()
        pygame.mixer.set_num_channels(0)
        pygame.mixer.music.unload()
