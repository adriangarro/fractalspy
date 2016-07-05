#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
fractals
'''

import message

import pygame as pg

from os import environ

from pygame.locals import *

from pygame.color import THECOLORS

from math import sin, cos, radians

__author__ = 'E. Adrián Garro Sánchez (2014088081)'
__copyright__ = 'Copyright 2015, Tecnológico de Costa Rica'

WIDTH = 800
HEIGHT = 600

environ['SDL_VIDEO_CENTERED'] = '1'  # centra la ventana.


def tree(calls=64, zoom=0):
    '''
    Función recursiva que despliega en pantalla
    un árbol de seis ramas.
    '''
    screen = pg.display.set_mode(
        (WIDTH, HEIGHT),
        DOUBLEBUF | HWSURFACE,
        32
    )
    pg.display.set_caption('Árbol')
    screen.fill(THECOLORS['tan'])

    def sketch(screen, x1, y1, length, angle, calls, rgb):
        '''
        Ángulo de rotación.
        '''
        omega = radians(-angle)
        '''
        Traslada desde el centro hasta las últimos líneas del
        punto final.
        '''
        x2 = x1 + cos(omega) * length
        y2 = y1 + sin(omega) * length
        '''
        Traslada al centro de la pantalla y dibuja.
        '''
        pg.draw.aaline(
            screen,
            rgb,
            (x1 + 400, y1 + 300),
            (x2 + 400, y2 + 300)
        )
        '''
        Altera el color.
        '''
        green_delta = - 20  # change in green
        red_delta = - 50  # change in red
        blue_delta = 20  # change in blue

        red = rgb[0] + red_delta
        if red < 0:
            red = 0
        if red > 255:
            red = 255
        green = rgb[1] + green_delta
        if green < 0:
            green = 0
        if green > 255:
            green = 255
        blue = rgb[2] + blue_delta
        if blue < 0:
            blue = 0
        if blue > 255:
            blue = 255
        rgb = (red, green, blue)
        '''
        Trazos recursivos (ramas del árbol).
        '''
        if calls:
            calls //= 2
            length //= 2
            sketch(
                screen,
                x2,
                y2,
                int(length),
                angle + 20,
                calls,
                rgb
            )
            sketch(
                screen,
                x2,
                y2,
                int(length),
                angle + 65,
                calls,
                rgb
            )
            sketch(
                screen,
                x2,
                y2,
                int(length),
                angle + 120,
                calls,
                rgb
            )
            sketch(
                screen,
                x2,
                y2,
                int(length),
                angle - 20,
                calls,
                rgb
            )
            sketch(
                screen,
                x2,
                y2,
                int(length),
                angle - 65,
                calls,
                rgb
            )
            sketch(
                screen,
                x2,
                y2,
                int(length),
                angle - 120,
                calls,
                rgb
            )
    sketch(
        screen,
        10 + zoom,
        270 + zoom,
        250 + zoom, 90,
        calls,
        THECOLORS['white']
    )
    pg.display.flip()
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                main()
                return None
            '''
            Zoom in - out
            '''
            if event.type == KEYDOWN:
                if event.key == pg.K_z:
                    tree(calls, 400)
                if event.key == pg.K_x:
                    tree(calls)


def sierpinski(calls=64, zoom=0):
    '''
    Función recursiva que despliega en pantalla
    el triángulo de Sierpinski.
    '''
    screen = pg.display.set_mode(
        (WIDTH, HEIGHT),
        DOUBLEBUF | HWSURFACE,
        32
    )
    pg.display.set_caption('Triángulo de Sierpinski')
    screen.fill(THECOLORS['skyblue'])
    '''
    Triangle's Vertices.
    '''
    point1 = (400, 10 - zoom)
    point2 = (100 - zoom, 590)
    point3 = (700 + zoom, 590)

    def midpoint(vertex1, vertex2):
        '''
        Función que calcula punto medio entre dos
        vértices de un triángulo.
        '''
        return (
            (vertex1[0] + vertex2[0]) // 2,
            (vertex1[1] + vertex2[1]) // 2
        )

    def triangles(vertex_a, vertex_b, vertex_c, calls, rgb):
        '''
        Función recursiva interna.
        '''
        pg.draw.aaline(
            screen,
            rgb,
            midpoint(vertex_a, vertex_b),
            midpoint(vertex_b, vertex_c),
            2
        )
        pg.draw.aaline(
            screen,
            rgb,
            midpoint(vertex_b, vertex_c),
            midpoint(vertex_c, vertex_a),
            2
        )
        pg.draw.aaline(
            screen,
            rgb,
            midpoint(vertex_c, vertex_a),
            midpoint(vertex_a, vertex_b),
            2
        )
        '''
        Altera el color.
        '''
        green_delta = - 20  # change in green
        red_delta = - 50  # change in red
        blue_delta = 20  # change in blue

        red = rgb[0] + red_delta
        if red < 0:
            red = 0
        if red > 255:
            red = 255
        green = rgb[1] + green_delta
        if green < 0:
            green = 0
        if green > 255:
            green = 255
        blue = rgb[2] + blue_delta
        if blue < 0:
            blue = 0
        if blue > 255:
            blue = 255
        rgb = (red, green, blue)
        '''
        Trazos recursivos (triángulos internos).
        '''
        if calls:
            calls //= 2
            triangles(
                vertex_a,
                midpoint(vertex_a, vertex_b),
                midpoint(vertex_a, vertex_c),
                calls, rgb
            )
            triangles(
                vertex_b,
                midpoint(vertex_b, vertex_a),
                midpoint(vertex_b, vertex_c),
                calls,
                rgb
            )
            triangles(
                vertex_c,
                midpoint(vertex_c, vertex_b),
                midpoint(vertex_c, vertex_a),
                calls, rgb
            )
    '''
    Triángulo principal.
    '''
    pg.draw.aaline(
        screen,
        THECOLORS['navy'],
        point1,
        point2,
    )
    pg.draw.aaline(
        screen,
        THECOLORS['navy'],
        point2,
        point3,
    )
    pg.draw.aaline(
        screen,
        THECOLORS['navy'],
        point3,
        point1,
    )
    '''
    Triángulos internos.
    '''
    triangles(
        point1,
        point2,
        point3,
        calls,
        THECOLORS['firebrick']
    )
    pg.display.flip()
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                main()
                return None
            '''
            Zoom in - out
            '''
            if event.type == KEYDOWN:
                if event.key == pg.K_z:
                    sierpinski(calls, 800)
                if event.key == pg.K_x:
                    sierpinski(calls)


def koch(calls=63, zoom=0):
    '''
    Función recursiva que despliega en pantalla
    el copo de nieve de Koch.
    '''
    screen = pg.display.set_mode(
        (WIDTH, HEIGHT),
        DOUBLEBUF | HWSURFACE,
        32
    )
    screen.fill(THECOLORS['snow3'])
    pg.display.set_caption('Copo de nieve de Von Koch')
    point = (150, 450)
    lenght = 500 + zoom

    def cordinates(lenght, angle, point):
        '''
        Función recursiva que indica las coordenas
        para trazar el copo de nieve de Koch.
        '''
        angle = radians(angle)
        return (
            point[0] + cos(angle) * lenght,
            point[1] - sin(angle) * lenght
        )

    def line(lenght, angle, point, calls, rgb):
        '''
        Función recursiva que establece las líneas del
        copo de nieve de koch.
        '''
        if not calls:
            coordinate = cordinates(lenght, angle, point)
            pg.draw.aaline(
                screen,
                rgb,
                point,
                coordinate,
            )
            '''
            Altera el color.
            '''
            green_delta = - 20  # change in green
            red_delta = - 50  # change in red
            blue_delta = 20  # change in blue

            red = rgb[0] + red_delta
            if red < 0:
                red = 0
            if red > 255:
                red = 255
            green = rgb[1] + green_delta
            if green < 0:
                green = 0
            if green > 255:
                green = 255
            blue = rgb[2] + blue_delta
            if blue < 0:
                blue = 0
            if blue > 255:
                blue = 255
            rgb = (red, green, blue)
            # pg.display.flip() to see draw
            return coordinate
        else:
            calls //= 2
            lenght //= 3
            line1 = line(
                lenght,
                angle,
                point,
                calls,
                rgb
            )
            line2 = line(
                lenght,
                angle - 60,
                line1,
                calls,
                rgb
            )
            line3 = line(
                lenght,
                angle + 60,
                line2,
                calls,
                rgb
            )
            line4 = line(
                lenght,
                angle,
                line3,
                calls,
                rgb
            )
            return line4

    def curves(lenght, calls, rgb):
        '''
        Función recursiva que establece las curvas del
        copo de nieve de Koch para proceder a dibujarlos
        en pantalla.
        '''
        calls //= 2
        # screen.fill(THECOLORS['snow']) optional: refresh display
        alpha = line(
            lenght,
            0,
            point,
            calls,
            rgb
        )
        beta = line(
            lenght,
            120,
            alpha,
            calls,
            rgb
        )
        gamma = line(
            lenght,
            240,
            beta,
            calls,
            rgb
        )
        return gamma

    '''
    Centinela.
    '''
    if calls > 63:
        calls = 63

    curves(  # optional: add cycle to see draws
        lenght,
        calls,
        THECOLORS['midnightblue']
    )
    pg.display.flip()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                main()
                return None
            '''
            Zoom in - out
            '''
            if event.type == KEYDOWN:
                if event.key == pg.K_z:
                    koch(calls, 800)
                if event.key == pg.K_x:
                    koch(calls)


def parallel_circuit(calls=64, zoom=0):
    '''
    Función recursiva que despliega en pantalla un
    fractal compuesto por líneas perpendiculares tales
    que asemejan un circuito en paralelo.
    '''
    screen = pg.display.set_mode(
        (WIDTH, HEIGHT),
        DOUBLEBUF | HWSURFACE,
        32
    )

    pg.display.set_caption('Circuito en Paralelo')

    screen.fill(THECOLORS['lightseagreen'])

    def draw(x, y, length, high, calls, rgb):
        '''
        Se procede a dibujar las líneas perpendiculares.
        '''
        pg.draw.aaline(
            screen,
            rgb,
            (x + length * 0.25, high // 2 + y),
            (x + length * 0.75, high // 2 + y),
        )
        pg.draw.line(
            screen,
            rgb,
            (x + length * 0.25, (high * 0.5) // 2 + y),
            (x + length * 0.25, (high * 1.5) // 2 + y),
        )
        pg.draw.line(
            screen,
            rgb,
            (x + length * .75, (high * 0.5) // 2 + y),
            (x + length * .75, (high * 1.5) // 2 + y),
        )
        '''
        Altera el color.
        '''
        green_delta = - 20  # change in green
        red_delta = - 50  # change in red
        blue_delta = 20  # change in blue

        red = rgb[0] + red_delta
        if red < 0:
            red = 0
        if red > 255:
            red = 255
        green = rgb[1] + green_delta
        if green < 0:
            green = 0
        if green > 255:
            green = 255
        blue = rgb[2] + blue_delta
        if blue < 0:
            blue = 0
        if blue > 255:
            blue = 255
        rgb = (red, green, blue)
        if calls:
            calls //= 2
            length //= 2
            high //= 2
            '''
            Arriba izquierda.
            '''
            draw(
                x,
                y,
                length,
                high,
                calls,
                rgb
            )
            '''
            Arriba derecha.
            '''
            draw(
                x + length,
                y,
                length,
                high,
                calls,
                rgb
            )
            '''
            Abajo izquierda.
            '''
            draw(
                x,
                y + length,
                length,
                high,
                calls,
                rgb
            )
            '''
            Abajo derecha.
            '''
            draw(
                x + length,
                y + length,
                length,
                high,
                calls,
                rgb
            )
    draw(
        50 - zoom,
        0 - zoom,
        700 + zoom,
        700 + zoom,
        calls,
        THECOLORS['lightgray']
    )
    pg.display.flip()
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                main()
                return None
            '''
            Zoom in - out
            '''
            if event.type == KEYDOWN:
                if event.key == pg.K_z:
                    parallel_circuit(calls, 800)
                if event.key == pg.K_x:
                    parallel_circuit(calls)


def menu(
    screen,
    background,
    tree_image,
    sierpinski_image,
    koch_image,
    parallel_circuit_image
):
    '''
    Función que controla el menú principal.
    '''
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                return None
                pg.quit()
            '''
            Previsualización de fractales.
            '''
            if event.type == MOUSEMOTION:
                x, y = event.pos
                if x in range(50, 250) and y in range(25, 80):
                    screen.blit(tree_image, (370, 150))
                    pg.display.update()
                elif x in range(50, 250) and y in range(140, 225):
                    screen.blit(sierpinski_image, (370, 150))
                    pg.display.update()
                elif x in range(50, 250) and y in range(280, 350):
                    screen.blit(koch_image, (370, 150))
                    pg.display.update()
                elif x in range(50, 250) and y in range(420, 480):
                    screen.blit(parallel_circuit_image, (370, 150))
                    pg.display.update()
                else:
                    screen.blit(background, (0, 0))
                    pg.display.update()
            '''
            Selección de fractales.
            '''
            if event.type == MOUSEBUTTONDOWN:
                x1, y1 = event.pos
                '''
                Árbol.
                '''
                if x1 in range(50, 250) and y1 in range(25, 80):
                    while True:
                        try:
                            calls = int(
                                message.ask(
                                    screen,
                                    'Por favor ingrese la profundidad'
                                ))
                            break
                        except ValueError:
                            pass
                    tree(calls)
                '''
                Triángulo de Sierpinski.
                '''
                if x1 in range(50, 250) and y1 in range(140, 225):
                    while True:
                        try:
                            calls = int(
                                message.ask(
                                    screen,
                                    'Por favor ingrese la profundidad'
                                ))
                            break
                        except ValueError:
                            pass
                    sierpinski(calls)
                '''
                Copo de nieve de Von Koch.
                '''
                if x1 in range(50, 250) and y1 in range(280, 350):
                    while True:
                        try:
                            calls = int(
                                message.ask(
                                    screen,
                                    'Por favor ingrese la profundidad'
                                ))
                            break
                        except ValueError:
                            pass
                    koch(calls)
                '''
                Fractal 4.
                '''
                if x1 in range(50, 250) and y1 in range(420, 480):
                    while True:
                        try:
                            calls = int(
                                message.ask(
                                    screen,
                                    'Por favor ingrese la profundidad'
                                ))
                            break
                        except ValueError:
                            pass
                    parallel_circuit(calls)


def main():
    pg.init()
    screen = pg.display.set_mode(
        (WIDTH, HEIGHT),
        DOUBLEBUF | HWSURFACE,
        32
    )
    pg.display.set_caption('Fractales')

    '''
    Carga de imágenes.
    '''
    background = pg.image.load('background.png')
    background = background.convert_alpha()

    tree_image = pg.image.load('tree.png')
    tree_image = tree_image.convert_alpha()

    sierpinski_image = pg.image.load('sierpinski.png')
    sierpinski_image = sierpinski_image.convert_alpha()

    koch_image = pg.image.load('koch.png')
    koch_image = koch_image.convert_alpha()

    parallel_circuit_image = pg.image.load('parallel_circuit.png')
    parallel_circuit_image = parallel_circuit_image.convert_alpha()

    '''
    Actualizar pantalla.
    '''
    screen.blit(background, (0, 0))

    '''
    Refresca la pantalla con lo que se ha dibujado.
    '''
    pg.display.flip()

    menu(
        screen,
        background,
        tree_image,
        sierpinski_image,
        koch_image,
        parallel_circuit_image
    )

if __name__ == "__main__":
    main()
