import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation

    def update(self, dt):
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SHOOT_SPEED * dt
        self.position += rotated_with_speed_vector

    def draw(self, screen):
         pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)