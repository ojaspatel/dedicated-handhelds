"""
Creator: Ojas Patel
Description: Script to simulate using an LED matrix as primary visual output
"""

import sys
from string import ascii_lowercase
import pygame
from pygame.locals import *

pygame.init()

#create window and background
screen_size = width, height = 640, 480
screen = pygame.display.set_mode(screen_size)
background = pygame.Surface((screen_size))

class ColorPalette:
    """
    Collection of objects/functions that support color changing of LED matrix
    """
    def __init__(self):
        self.active_color = (255, 255, 255)
        self.colors = [
            ['white', (255, 255, 255)],
            ['red', (255, 0, 00)],
            ['orange', (255, 127, 0)],
            ['yellow', (255, 255, 0)],
            ['green', (0, 255, 0)],
            ['blue', (0, 0, 255)],
            ['indigo', (75, 0, 130)],
            ['violet', (148, 0, 211)]
        ]
        self.color_palette = {}
        self.set_color = None
    def create_palette(self):
        for color, xpos in zip(self.colors, range(20, 230+1, 30)):
            self.color_palette[color[0]] = [color[1], pygame.draw.circle(background, color[1], (xpos, 460), 10)]

    def set_active_color(self):
        for color in self.color_palette.keys():
            if self.color_palette[color][1].collidepoint(pygame.mouse.get_pos()) and event.type == MOUSEBUTTONDOWN:
                self.active_color = self.color_palette[color][0]
                self.set_color = self.active_color
                print("active color: ", self.set_color)
                test_object = pygame.draw.circle(background, self.active_color, (20, 20), 10)
        return self.active_color

class LED:
    """
    Collection of functions create a grid of circles that represent an LED matrix and initiate color-change behavior
    """
    def __init__(self, change_color):
        self.led_grid = {}
        self.color_palette = change_color


    def create_led_grid(self):
        x_origin, y_origin = 145, 65
        for letter, coord in zip(ascii_lowercase[0:8], range(8)):
            x = x_origin + (coord * 50)
            self.led_grid[letter + '1'] = [pygame.draw.circle(background, (self.color_palette.active_color), (x, y_origin), 20), x, y_origin]
            for coord in range(1, 8):
                y = y_origin + (coord * 50)
                self.led_grid[letter + str(coord+1)] = [pygame.draw.circle(background, (self.color_palette.active_color), (x, y), 20), x, y]
        print(self.led_grid)

    def toggle_led(self):
        for led in self.led_grid.keys():
            if self.led_grid[led][0].collidepoint(pygame.mouse.get_pos()) and event.type == MOUSEBUTTONDOWN:
                self.led_grid[led][0] = pygame.draw.circle(background, (self.color_palette.active_color), (self.led_grid[led][1], self.led_grid[led][2]), 20)

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    #You neeed to define you object to enable def __init__()
    color_palette = ColorPalette()
    led = LED(color_palette)
    #initiate color palette and LED matrix
    color_palette.create_palette()
    led.create_led_grid()
    #core loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        color_palette.set_color = color_palette.set_active_color()
        #print(color_palette.set_color)
        led.toggle_led()
        screen.blit(background, (0, 0))
        pygame.display.update()
