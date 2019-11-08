"""
Creator: Ojas Patel
Description: Script to simulate using an LED matrix as primary visual output
"""

import sys
from string import ascii_lowercase
import pygame
from pygame.locals import *
import time

pygame.init()
clock = pygame.time.Clock()

#create window and background
screen_size = width, height = 640, 480
screen = pygame.display.set_mode(screen_size)
background = pygame.Surface((screen_size))
LED_NUM = 8


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

    def set_color_drop():
        ColorPalette.active_color = ColorPalette.color_palette[color][2]
        test_object = pygame.draw.circle(background, ColorPalette.active_color, (20, 20), 10)


class LED:
    """
    Collection of functions create a grid of circles that represent an LED matrix and initiate color-change behavior
    """
    led_grid = {}

    def create_led_grid():
        x_origin, y_origin = 145, 65
        for letter, coord in zip(ascii_lowercase[0:8], range(LED_NUM)):
            x = x_origin + (coord * 50)
            LED.led_grid[letter + '1'] = [pygame.draw.circle(background, (ColorPalette.active_color), (x, y_origin), 20), False, x, y_origin]
            for coord in range(1, LED_NUM):
                y = y_origin + (coord * 50)
                LED.led_grid[letter + str(coord+1)] = [pygame.draw.circle(background, (ColorPalette.active_color), (x, y), 20), False, x, y]

    def toggle_led():
        for led in LED.led_grid.values():
            if led[0].collidepoint(pygame.mouse.get_pos()) and event.type == MOUSEBUTTONDOWN:
                led[1] = True
        for led in LED.led_grid.keys():
            if LED.led_grid[led][1] == True:
                LED.led_grid[led][0] = pygame.draw.circle(background, (ColorPalette.active_color), (LED.led_grid[led][2], LED.led_grid[led][3]), 20)
                LED.led_grid[led][1] = False

    def rain_drop():
        x_origin, y_origin = 145, 65
        for letter, coord in zip(ascii_lowercase[0:8], range(LED_NUM)):
            y = y_origin + (coord * 50)
            LED.led_grid[letter + '1'] = [pygame.draw.circle(background, (0, 0, 255), (x_origin, y), 20), False, x_origin, y]
            #LED.led_grid[letter + '2'] = [pygame.draw.circle(background, (255, 255, 255), (x, y_origin), 20), False, x, y_origin]
            pygame.display.update()
            clock.tick(15)
            screen.blit(background, (0, 0))
            LED.led_grid[letter + '1'] = [pygame.draw.circle(background, (255, 255, 255), (x_origin, y), 20), False, x_origin, y]
            pygame.display.update()
            clock.tick(15)
            #clock.tick(15)
            #screen.blit(background, (0, 0))
#initiate color palette and LED matrix

if __name__ == '__main__':
    ColorPalette.create_palette()
    LED.create_led_grid()
    #core loop
    while True:
        #clock.tick(1000)
        #screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        #ColorPalette.set_active_color()
        #LED.toggle_led
        LED.rain_drop()
        #pygame.display.update()
