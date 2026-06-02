import pygame


class Button:
    def __init__(self, x, y, width, height, text, font,
                 color, hover_color, text_color):

        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()

        current_color = self.color

        if self.rect.collidepoint(mouse_pos):
            current_color = self.hover_color

        pygame.draw.rect(surface, current_color, self.rect)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)

        text_surface = self.font.render(self.text, True, self.text_color)

        text_rect = text_surface.get_rect(center=self.rect.center)

        surface.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)