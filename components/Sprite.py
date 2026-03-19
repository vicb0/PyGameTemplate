from pygame import transform


class Sprite:
    def __init__(self, image, duration):
        self.image = image
        self.duration = duration


class SpriteAnimation:
    def __init__(self, sprites):
        self.sprites = sprites
        self.curr_index = 0
        self.timer = 0

    def update(self, dt):
        self.timer += dt
        updated = False

        while self.timer >= self.sprites[self.curr_index].duration:
            self.timer -= self.sprites[self.curr_index].duration
            self.curr_index = (self.curr_index + 1) % len(self.sprites)
            updated = True
        
        if updated:
            return self.get_curr_sprite()
        
        return None

    def get_curr_sprite(self):
        return self.sprites[self.curr_index].image

    def reset(self):
        self.timer = 0
        self.curr_index = 0


class SpritesGroupManager:
    def __init__(self):
        self.states = dict()
        self.curr_anim = None

    def add(self, name, sprites, store_flipped_x=False, store_flipped_y=False, store_flipped_xy=False):
        self.states[name] = {
            "normal": SpriteAnimation(sprites)
        }

        def flip(sprites, flip_x, flip_y):
            new = []
            for sprite in sprites:
                new.append(
                    Sprite(
                        transform.flip(sprite.image, flip_x, flip_y),
                        sprite.duration
                    )
                )
            return new

        if store_flipped_x:
            self.states[name]["flip_x"] = SpriteAnimation(flip(sprites, True, False))
        if store_flipped_y:
            self.states[name]["flip_y"] = SpriteAnimation(flip(sprites, False, True))
        if store_flipped_xy:
            self.states[name]["flip_xy"] = SpriteAnimation(flip(sprites, True, True))

    def set_state(self, name, flip_x=False, flip_y=False):
        flip = "normal"

        if self.states.get(name) is None:
            raise Exception(f"Sprite State {name} not found")
        
        if flip_x and flip_y:
            if self.states[name].get("flip_xy") is None:
                raise Exception(f"Sprite State {name} does not have flip_xy")
            flip = "flip_xy"
        elif flip_x:
            if self.states[name].get("flip_x") is None:
                raise Exception(f"Sprite State {name} does not have flip_x")
            flip = "flip_x"
        elif flip_y:
            if self.states[name].get("flip_y") is None:
                raise Exception(f"Sprite State {name} does not have flip_y")
            flip = "flip_y"

        new_anim = self.states[name][flip]

        if self.curr_anim != new_anim:
            self.curr_anim = new_anim
            self.curr_anim.reset()

    def only_if_has_state(func):
        def wrapper(self, *args, **kwargs):
            if self.curr_anim is None:
                raise Exception("No animation state set")
            return func(self, *args, **kwargs)
        return wrapper

    @only_if_has_state
    def update(self, dt):
        return self.curr_anim.update(dt)

    @only_if_has_state
    def get_curr_sprite(self):
        return self.curr_anim.get_curr_sprite()
