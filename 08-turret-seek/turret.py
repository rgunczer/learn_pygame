import random
import pygame
from math import atan2, pi, radians, sin, cos, degrees
from pygame import Vector2
from pygame.transform import rotozoom


class Turret:
    def __init__(self, base, gun, pos):
        self.base = base
        self.gun = gun

        # reference to the original image to preserve the quality
        self.orig_image = self.gun
        self.rect = self.gun.get_rect(center=pos)
        self.pos = Vector2(pos)  # original center position/pivot point.
        self.offset = Vector2(0, -16)
        self.angle = random.randint(0, 360)
        self.angular_velocity = 0.0075 * 3

    def rotateGunImage(self): # https://stackoverflow.com/questions/15098900/how-to-set-the-pivot-point-center-of-rotation-for-pygame-transform-rotate
        """Rotate the image of the sprite around a pivot point"""

        # rotate image
        self.image = rotozoom(self.orig_image, -self.angle, 1)

        # rotate offset vector
        offset_rotated = self.offset.rotate(self.angle)

        # create a new rect with the center of the sprite + the offset
        self.rect = self.image.get_rect(center=self.pos + offset_rotated)


    def seekTarget(self, target):
        diff_x = target.x - self.pos.x
        diff_y = target.y - self.pos.y

        rotation = -90.0

        angle = radians(self.angle + rotation)

        desiredAngle = atan2(diff_y, diff_x)
        angleDiff = desiredAngle - angle

        # normalize angle to [-PI,PI] range. This ensures that the turret turns the shortest way.
        while angleDiff < -pi:
            angleDiff += 2 * pi

        while angleDiff >= pi:
            angleDiff -= 2 * pi

        if angleDiff > 0.0:
            angle += self.angular_velocity

        if angleDiff < 0.0:
            angle -= self.angular_velocity


        self.angle = degrees(angle) - rotation

        self.rotateGunImage()


    def draw(self, screen):
        screen.blit(self.base, (self.pos.x - self.base.get_width() // 2, self.pos.y - self.base.get_height() // 2))
        screen.blit(self.image, self.rect)
        pygame.draw.circle(screen, (0, 255, 0), self.pos, 4)
