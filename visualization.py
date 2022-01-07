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


def display_theme_color(pos: tuple[int, int], theme_num: int) -> int:
    """
    Returns the proper theme color based on the mouse position
    when the user clicks the mouse button.
    """
    theme_number = theme_num

    if 30 <= pos[0] <= 60 and 130 <= pos[1] <= 160:
        theme_number = 0
    elif 75 <= pos[0] <= 105 and 130 <= pos[1] <= 160:
        theme_number = 1
    elif 120 <= pos[0] <= 150 and 130 <= pos[1] <= 160:
        theme_number = 2
    elif 30 <= pos[0] <= 60 and 178 <= pos[1] <= 218:
        theme_number = 3
    elif 75 <= pos[0] <= 105 and 178 <= pos[1] <= 218:
        theme_number = 4
    elif 120 <= pos[0] <= 150 and 178 <= pos[1] <= 218:
        theme_number = 5

    return theme_number


def page_changer(pos: tuple[int, int], page_num: int, option: bool) -> tuple[int, bool]:
    """
    Returns the updated page number based on the mouse position
    when the user clicks the mouse button.
    """
    page_number = page_num
    update_option = option

    if page_number == 0:
        # This will transition to the about page
        if 175 <= pos[0] <= 425 and 270 <= pos[1] <= 345:
            page_number = 1
            # This will transition to the graph page
        elif 175 <= pos[0] <= 425 and 120 <= pos[1] <= 195:
            page_number = 2

            # This is responsible for making the option gui visible
        elif 25 <= pos[0] <= 53 and 34 <= pos[1] <= 62:
            if update_option:
                update_option = False
            else:
                update_option = True

    return (page_number, update_option)


def mouse_click(pos: tuple[int, int], page: int, option_gui: bool, theme_number: int,
                categories: list) -> tuple[tuple[int, int], int, bool, int, list]:
    """
    This function handles the mouse click event for all thew pages and updates
    the variables accordingly using other helper functions.
    """
    position = pos
    page_num = page
    option = option_gui
    theme = theme_number
    category_list = categories
    if page_num == 0:
        # This will update the page number and the option_gui condition
        page_num, option = page_changer(position, page_num, option)

        # The following will change the theme color
        if option:
            theme = display_theme_color(position, theme)

    elif page == 1:
        if 35 <= pos[0] <= 100 and 440 <= pos[1] <= 467:
            page_num = 0

    elif page == 2:
        if 47 <= pos[0] <= 211 and 65 <= pos[1] <= 109:
            category_changer('covid_cases', category_list)

        elif 47 <= pos[0] <= 211 and 145 <= pos[1] <= 189:
            category_changer('cpi', category_list)

        elif 47 <= pos[0] <= 211 and 225 <= pos[1] <= 269:
            category_changer('csi', category_list)

        elif 47 <= pos[0] <= 211 and 305 <= pos[1] <= 349:
            category_changer('unemployment_rate', category_list)

        elif 47 <= pos[0] <= 211 and 385 <= pos[1] <= 429:  # bar graph code
            start_dt = START_DATE
            end_dt = END_DATE
            filtered_data = graph.get_filtered_data(start_dt, end_dt)
            graph.csi_bar_chart(filtered_data)

        elif 250 <= pos[0] <= 400 and 390 <= pos[1] <= 460 and category_list != []:
            # submit_clicked = 1
            start_dt = START_DATE
            end_dt = END_DATE
            filtered_data = graph.get_filtered_data(start_dt, end_dt)
            graph.line_graph(filtered_data, category_list)

        elif 430 <= pos[0] <= 580 and 390 <= pos[1] <= 460 and category_list != []:
            # animate_clicked = 1
            start_dt = START_DATE
            end_dt = END_DATE
            filtered_data = graph.get_filtered_data(start_dt, end_dt)
            graph.animated_graph(filtered_data, category_list)

    return (position, page_num, option, theme, category_list)


def category_changer(category: str, category_list: list) -> list:
    """
    Returns the updated category list based on the existing
    items in the category list.
    """
    if category not in category_list:
        category_list.append(category)
    else:
        category_list.remove(category)

    return category_list


def theme_selector(number: int) -> None:
    """
    This function displays which theme color is selected currently
    """
    if number == 0:
        pygame.draw.rect(SCREEN, WHITE, [30, 130, 30, 30], 2)
    elif number == 1:
        pygame.draw.rect(SCREEN, WHITE, [75, 130, 30, 30], 2)
    elif number == 2:
        pygame.draw.rect(SCREEN, WHITE, [120, 130, 30, 30], 2)
    elif number == 3:
        pygame.draw.rect(SCREEN, WHITE, [30, 178, 30, 30], 2)
    elif number == 4:
        pygame.draw.rect(SCREEN, WHITE, [75, 178, 30, 30], 2)
    elif number == 5:
        pygame.draw.rect(SCREEN, WHITE, [120, 178, 30, 30], 2)


def page_one_buttons(pos: tuple[int, int], theme_number: int) -> None:
    """
    This function draws the graph and about button in the first page.
    """
    y_value = [120, 270]
    for i in y_value:
        if 175 <= pos[0] <= 425 and i <= pos[1] <= i + 75:
            pygame.draw.rect(SCREEN, THEME_COLOR[theme_number][1], [170, i - 5, 260, 85], 1)
            pygame.draw.rect(SCREEN, G2, [175, i, 250, 75], 0)
        else:
            pygame.draw.rect(SCREEN, THEME_COLOR[theme_number][0], [170, i - 5, 260, 85], 1)
            pygame.draw.rect(SCREEN, GREY, [175, i, 250, 75], 0)


def draw_option_gui(draw: bool, theme_number: int) -> None:
    """
    This function draws the option button and option gui in the first page.
    """
    if draw:
        pygame.draw.rect(SCREEN, G2, [0, 0, 200, 500], 0)
        pygame.draw.rect(SCREEN, THEME_COLOR[theme_number][0], [-2, -2, 200, 504], 4)

        # These will create different theme option
        SCREEN.blit(COLORS1, [20, 90])
        pygame.draw.rect(SCREEN, DARK_GREY, [15, 120, 160, 100], 0)

        # Row 1 for colors
        pygame.draw.rect(SCREEN, TEAL, [30, 130, 30, 30], 0)
        pygame.draw.rect(SCREEN, MID_RED, [75, 130, 30, 30], 0)
        pygame.draw.rect(SCREEN, LIGHT_RED, [120, 130, 30, 30], 0)

        # Row 2 for colors
        pygame.draw.rect(SCREEN, PURPLE, [30, 178, 30, 30], 0)
        pygame.draw.rect(SCREEN, BLUE, [75, 178, 30, 30], 0)
        pygame.draw.rect(SCREEN, DARK_PEACH, [120, 178, 30, 30], 0)

        theme_selector(theme_number)  
