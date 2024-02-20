from entity import Entity
import pygame
import math


class Asteroid(Entity):

    def __init__(self, screen, x, y, speed, angle, size=20):
        super().__init__(screen, x, y)
        self.speed_x = speed * math.cos(angle)
        self.speed_y = speed * math.cos(angle)
        self.size = size
        self.SCREEN_WIDTH = screen.get_width()
        self.SCREEN_HEIGHT = screen.get_height()
        self.max_speed = 10

    def update(self, dt):

        dx = self.speed_x * dt * self.TARGET_FPS
        dy = self.speed_y * dt * self.TARGET_FPS
        self.x += dx
        self.y += dy
        self.x %= self.SCREEN_WIDTH
        self.y %= self.SCREEN_HEIGHT

    def draw(self):

        for y in range(-1, 2):
            for x in range(-1, 2):
                offset_x = x * self.SCREEN_WIDTH
                offset_y = y * self.SCREEN_HEIGHT

                circle_center = (self.x + offset_x, self.y + offset_y)
                pygame.draw.circle(self.screen, (255, 0, 0), circle_center, self.size)