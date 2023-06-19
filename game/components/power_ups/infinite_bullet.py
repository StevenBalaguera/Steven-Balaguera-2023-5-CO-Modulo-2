from game.components.power_ups.power_up import PowerUp
from game.utils.constants import GIFT, BULLET_TYPE

class MaxBullet(PowerUp):
    def __init__(self):
        super().__init__(GIFT, BULLET_TYPE)