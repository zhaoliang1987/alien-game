class Settings:
    """存储游戏《外星人》有的所有设置的类"""

    def __init__(self):
        """定义游戏名称"""
        self.game_title = "Alien Invasion"

        """设置界面背景色"""
        self.bg_color = (230, 230, 230)

        """设置屏幕宽度"""
        self.screen_width = 1200

        """设置屏幕高度"""
        self.screen_height = 800

        """飞船移动速度"""
        self.ship_speed = 1.5

        self.alien_speed = 1.0

        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        '''允许子弹存在屏幕的最大数目'''
        self.bullets_allowed = 30
