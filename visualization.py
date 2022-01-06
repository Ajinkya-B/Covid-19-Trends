"""
Evaluating the impact of COVID-19 on Canadians’ spending habits: pygame module

This module is responsible for outputting an interactive visualization using pygame.

Copyright and Usage Information
===============================
This file is Copyright (c) 2021 Raiyan Raad.
"""
from datetime import date
import pygame
import graph

# These are the rgb value of the colors we will be using
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

TEAL = (28, 195, 139)
GRASS = (130, 145, 52)

DARK_GREY = (25, 25, 25)
GREY = (82, 82, 82)
G2 = (51, 49, 51)

MID_RED = (255, 68, 102)
LIGHT_RED = (255, 133, 161)
RED = (222, 22, 75)

LIGHT_PURPLE = (219, 0, 182)
PURPLE = (119, 0, 204)

LIGHT_BLUE = (72, 202, 228)
BLUE = (0, 119, 182)

LIGHT_PEACH = (247, 157, 101)
DARK_PEACH = (242, 92, 84)

# Initializes Pygame
pygame.display.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500
SCREEN = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Visualization")

# Used to manage how fast the SCREEN updates
CLOCK = pygame.time.Clock()

# The following creates the text formats, that is outputted on the SCREEN
pygame.font.init()
GRAPH = pygame.font.SysFont('Arial', 35, True, False)
WBACK = pygame.font.SysFont('Calibri', 32, True, False)
OPTION = pygame.font.SysFont('Arial', 30, False, False)
COLORS = pygame.font.SysFont('Open Sans', 28, False, False)
TEXT = pygame.font.SysFont('Arial', 25, True, False)

GRAPH1 = GRAPH.render('Graph', True, WHITE)
ABOUT1 = GRAPH.render('About', True, WHITE)
OPTION1 = OPTION.render('∆', True, WHITE)
COLORS1 = COLORS.render('Themes', True, WHITE)
BACK2 = WBACK.render('<<<', True, WHITE)

# The following create the text for the graphing buttons
GRAPH_OPTION = pygame.font.SysFont('Arial', 24, False, False)
GRAPH_OPTION2 = pygame.font.SysFont('Arial', 15, False, False)
GRAPH_BTN1 = GRAPH_OPTION.render('Covid Cases', True, WHITE)
GRAPH_BTN2 = GRAPH_OPTION.render('CPI', True, WHITE)
GRAPH_BTN3 = GRAPH_OPTION.render('CSI', True, WHITE)
GRAPH_BTN4 = GRAPH_OPTION2.render('Unemployment Rate', True, WHITE)
GRAPH_BTN5 = GRAPH_OPTION.render('Sub - CSI', True, WHITE)
SUBMIT = GRAPH_OPTION.render('Submit', True, WHITE)
ANIMATE = GRAPH_OPTION.render('Animate', True, WHITE)
TEXT1 = GRAPH_OPTION.render('About:', True, WHITE)

PICTURE = pygame.image.load('stonks.gif').convert()
PICTURE = pygame.transform.scale(PICTURE, (331, 251))
ABOUT = pygame.image.load('about_info.png').convert()
ABOUT = pygame.transform.scale(ABOUT, (551, 250))

# The theme_color list stores all the colors for each theme
THEME_COLOR = [[TEAL, GRASS], [MID_RED, WHITE], [LIGHT_RED, RED],
               [PURPLE, LIGHT_PURPLE], [BLUE, LIGHT_BLUE], [DARK_PEACH, LIGHT_PEACH]]
