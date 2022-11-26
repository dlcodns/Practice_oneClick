import pygame
import sys
from pygame.locals import*
from rule import*

bg_color = (255,255,255)

window_width = 400
window_height = 300

fps = 60
fps_clock = pygame.time.Clock()

def main():
    pygame.init()
    surface = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("test")
    surface.fill(bg_color)
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
    pygame.quit()
    
main()