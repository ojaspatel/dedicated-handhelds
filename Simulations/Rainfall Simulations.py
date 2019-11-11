"""
Creator: Ojas Patel, Carlos Fernandez
Description: Script to simulate using an LED matrix as primary visual output
"""

import sys
from string import ascii_lowercase
import pygame
from pygame.locals import *
import time

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

    def create_palette(self):
        for color, xpos in zip(self.colors, range(20, 230+1, 30)):
            self.color_palette[color[0]] = [color[1], pygame.draw.circle(background, color[1], (xpos, 460), 10)]

    def set_active_color():
        for color in self.color_palette.keys():
            if self.color_palette[color][1].collidepoint(pygame.mouse.get_pos()) and event.type == MOUSEBUTTONDOWN:
                self.active_color = self.color_palette[color][0]
                test_object = pygame.draw.circle(background, self.active_color, (20, 20), 10)

    def set_color_drop():
        self.active_color = self.color_palette[color][2]
        test_object = pygame.draw.circle(background, self.active_color, (20, 20), 10)


class LED:
    """
    Collection of functions create a grid of circles that represent an LED matrix and initiate color-change behavior
    """
    def __init__(self):
        self.led_grid = {}
        self.led_num = 8

    def create_led_grid(self):
        x_origin, y_origin = 145, 65
        for letter, coord in zip(ascii_lowercase[0:self.led_num], range(self.led_num)):
            x = x_origin + (coord * 50)
            self.led_grid[letter + '1'] = [pygame.draw.circle(background, (ColorPalette().active_color), (x, y_origin), 20), False, x, y_origin]
            for coord in range(1, self.led_num):
                y = y_origin + (coord * 50)
                self.led_grid[letter + str(coord+1)] = [pygame.draw.circle(background, (ColorPalette().active_color), (x, y), 20), False, x, y]
        print(self.led_grid)

    def toggle_led(self):
        for led in self.led_grid.values():
            if led[0].collidepoint(pygame.mouse.get_pos()) and event.type == MOUSEBUTTONDOWN:
                led[1] = True
        for led in LED.led_grid.keys():
            if self.led_grid[led][1] == True:
                self.led_grid[led][0] = pygame.draw.circle(background, (ColorPalette.active_color), (self.led_grid[led][2], self.led_grid[led][3]), 20)
                self.led_grid[led][1] = False

    def rain_drop(self):
        x_origin, y_origin = 145, 65
        for letter, coord in zip(ascii_lowercase[0:self.led_num], range(self.led_num)):
            y = y_origin + (coord * 50)
            self.led_grid[letter + '1'] = [pygame.draw.circle(background, (0, 0, 255), (x_origin, y), 20), False, x_origin, y]
            pygame.display.update()
            clock.tick(15)
            screen.blit(background, (0, 0))
            self.led_grid[letter + '1'] = [pygame.draw.circle(background, (255, 255, 255), (x_origin, y), 20), False, x_origin, y]
            pygame.display.update()
            clock.tick(15)

    def rain_simulation(self):
        x_origin, y_origin = 145, 65
        x2 = x_origin + (2*50) # two
        x3 = x_origin + (4*50)
        x4 = x_origin + (6*50)

        x5 = x_origin + (1*50)
        x6 = x_origin + (3*50)
        x7 = x_origin + (5*50)
        x8 = x_origin + (7*50)
        for letter, coord in zip(ascii_lowercase[0:self.led_num], range(self.led_num)):
            y = y_origin + (coord * 50)

            #print(letter, coord)
            self.led_grid[letter + '1'] = [pygame.draw.circle(background, (0, 0, 255), (x_origin, y), 20), False, x_origin, y]
            self.led_grid[letter + '1'] = [pygame.draw.circle(background, (0, 0, 255), (x2, y), 20), False, x2, y]
            self.led_grid[letter + '1'] = [pygame.draw.circle(background, (0, 0, 255), (x3, y), 20), False, x3, y]
            self.led_grid[letter + '1'] = [pygame.draw.circle(background, (0, 0, 255), (x4, y), 20), False, x4, y]
            if coord >= 1:
                new_coord = coord-1
                y_lag = y_origin +(new_coord *50)
                self.led_grid[letter + '1'] = [pygame.draw.circle(background, (0, 0, 255), (x5, y_lag), 20), False, x5, y_lag]
                self.led_grid[letter + '1'] = [pygame.draw.circle(background, (0, 0, 255), (x6, y_lag), 20), False, x6, y_lag]
                self.led_grid[letter + '1'] = [pygame.draw.circle(background, (0, 0, 255), (x7, y_lag), 20), False, x7, y_lag]
                self.led_grid[letter + '1'] = [pygame.draw.circle(background, (0, 0, 255), (x8, y_lag), 20), False, x8, y_lag]

            pygame.display.update()
            clock.tick(10)
            screen.blit(background, (0, 0))
            self.led_grid[letter + '1'] = [pygame.draw.circle(background, (255, 255, 255), (x_origin, y), 20), False, x_origin, y]
            self.led_grid[letter + '1'] = [pygame.draw.circle(background, (255, 255, 255), (x2, y), 20), False, x2, y]
            self.led_grid[letter + '1'] = [pygame.draw.circle(background, (255, 255, 255), (x3, y), 20), False, x3, y]
            self.led_grid[letter + '1'] = [pygame.draw.circle(background, (255, 255, 255), (x4, y), 20), False, x4, y]

            if coord >= 1:
                self.led_grid[letter + '1'] = [pygame.draw.circle(background, (255, 255, 255), (x5, y_lag), 20), False, x5, y_lag]
                self.led_grid[letter + '1'] = [pygame.draw.circle(background, (255, 255, 255), (x6, y_lag), 20), False, x6, y_lag]
                self.led_grid[letter + '1'] = [pygame.draw.circle(background, (255, 255, 255), (x7, y_lag), 20), False, x7, y_lag]
                self.led_grid[letter + '1'] = [pygame.draw.circle(background, (255, 255, 255), (x8, y_lag), 20), False, x8, y_lag]

            pygame.display.update()
            clock.tick(10)




if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    #create window and background
    screen_size = width, height = 640, 480
    #screen_size = width, height = 1020, 960
    screen = pygame.display.set_mode(screen_size)
    background = pygame.Surface((screen_size))
    LED = LED()
    LED.create_led_grid()
    #core loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        LED.rain_simulation()
