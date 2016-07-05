#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Biblioteca enfocada a la representación de texto
en las ventanas generadas por pygame.
'''

import pygame

import pygame.font

import pygame.event

import pygame.draw

import string

from pygame.locals import *

SNOW = (205, 201, 201)


def get_key():
    '''
    Obtiene la tecla que el usuario ingrese.
    '''
    while True:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        else:
            pass


def display_message(screen, message):
    '''
    Imprime un mensanje en pantalla.
    '''
    font_object = pygame.font.Font(None, 24)
    pygame.draw.rect(screen, SNOW, ((50), (540), 300, 20), 0)
    if len(message) != 0:
        screen.blit(font_object.render(message, 1, (0, 0, 0)), (50, 540))
    pygame.display.flip()


def ask(screen, question):
    '''
    ask(screen, question) --> answer
    '''
    pygame.font.init()
    current_string = []
    display_message(screen, question + ': ' + string.join(current_string, ''))

    while len(current_string) < 3:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey == K_RETURN:
            break
        elif inkey == K_MINUS:
            current_string.append('_')
            display_box(screen, question + ': ' + string.join(current_string, ''))
        elif inkey <= 127:
            current_string.append(chr(inkey))
        display_message(screen, question + ': ' + string.join(current_string, ''))
    return string.join(current_string, '')
