def rect_collision(rect1, rect2):
    return rect1.colliderect(rect2)

def mask_collision(mask1, mask2, offset=(0, 0)):
    return mask1.overlap(mask2, offset) is not None
    
def check_collision(rect1, rect2, mask1=None, mask2=None):
    if not rect_collision(rect1, rect2):
        return 0
    
    if mask1 is None or mask2 is None:
        return True
    
    offset = (
        int(rect2.x - rect1.x),
        int(rect2.y - rect1.y)
    )

    return mask_collision(mask1, mask2, offset)