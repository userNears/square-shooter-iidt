import pygame

class Button:
    def __init__(self, text, font, size, color, x, y, action):
        self.text = text
        self.font = pygame.font.SysFont(font, size)
        self.color = color
        self.x = x
        self.y = y
        self.action = action
        self.txt = self.font.render(self.text, True, self.color)
        self.txt_rect = self.txt.get_rect(center = (self.x, self.y))

    def render(self, screen):
        screen.blit(self.txt, self.txt_rect)
    
    def is_hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.txt_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    
    def interact(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.txt_rect.collidepoint(mouse_pos):
            self.action()