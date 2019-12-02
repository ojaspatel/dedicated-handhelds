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
    active_color = (255, 255, 255)
    colors = [
        ['white', (255, 255, 255)],
        ['red', (255, 0, 00)],
        ['orange', (255, 127, 0)],
        ['yellow', (255, 255, 0)],
        ['green', (0, 255, 0)],
        ['blue', (0, 0, 255)],
        ['indigo', (75, 0, 130)],
        ['violet', (148, 0, 211)]
    ]
    color_palette = {}

    def create_palette():
        for color, xpos in zip(ColorPalette.colors, range(20, 230+1, 30)):
            ColorPalette.color_palette[color[0]] = [color[1], pygame.draw.circle(background, color[1], (xpos, 460), 10)]

    def set_active_color():
        for color in ColorPalette.color_palette.keys():
            if ColorPalette.color_palette[color][1].collidepoint(pygame.mouse.get_pos()) and event.type == MOUSEBUTTONDOWN:
                ColorPalette.active_color = ColorPalette.color_palette[color][0]
                test_object = pygame.draw.circle(background, ColorPalette.active_color, (20, 20), 10)
            

class LED:
    """
    Collection of functions create a grid of circles that represent an LED matrix and initiate color-change behavior
    """
    led_grid = {}

    def create_led_grid():
        x_origin, y_origin = 145, 65
        for letter, coord in zip(ascii_lowercase[0:8], range(8)):
            x = x_origin + (coord * 50)
            LED.led_grid[letter + '1'] = [pygame.draw.circle(background, (ColorPalette.active_color), (x, y_origin), 20), x, y_origin]
            for coord in range(1, 8):
                y = y_origin + (coord * 50)
                LED.led_grid[letter + str(coord+1)] = [pygame.draw.circle(background, (ColorPalette.active_color), (x, y), 20), x, y]

    def toggle_led():
        for led in LED.led_grid.keys():
            if LED.led_grid[led][0].collidepoint(pygame.mouse.get_pos()) and event.type == MOUSEBUTTONDOWN:
                LED.led_grid[led][0] = pygame.draw.circle(background, (ColorPalette.active_color), (LED.led_grid[led][1], LED.led_grid[led][2]), 20)


#initiate color palette and LED matrix
ColorPalette.create_palette()
LED.create_led_grid()

#core loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    ColorPalette.set_active_color()
    LED.toggle_led()
    screen.blit(background, (0, 0))
    pygame.display.update()

