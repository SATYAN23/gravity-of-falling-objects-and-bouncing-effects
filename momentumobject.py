import pygame
import math
import os
import pygame_gui
from pygame_gui.core import ObjectID
import pygame_widgets
from pygame_widgets.button import Button
import decimal
pygame.init()

i_icon = os.getcwd() + './sem.png'
icon = pygame.image.load(i_icon)
pygame.display.set_icon(icon)
pygame.display.set_caption('falling object')

window = pygame.display.set_mode((1400, 700))
font = pygame.font.SysFont('Segoe UI', 20)

red = '#8B0000'
gray = '#dcdcdc'
black = '#101010'
blue = '#00008B'

clock = pygame.time.Clock() 

theme = '.\entry_line.json'
btheme = 'button.json'
manager = pygame_gui.UIManager((500, 500), theme)
manager.get_theme().load_theme(theme)

text_input = pygame_gui.elements.UITextEntryLine(
     relative_rect = pygame.Rect((100, 150), (100, 25)),
     placeholder_text = 'enter ADG',
     manager = manager, object_id = ObjectID(class_id = 'text_entry_line',
                                             object_id = '#main_text_entry1'))
text_input = pygame_gui.elements.UITextEntryLine(
     relative_rect = pygame.Rect((100, 200), (100, 25)),
     placeholder_text = 'enter %M1',
     manager = manager, object_id = ObjectID(class_id = 'text_entry_line',
                                             object_id = '#main_text_entry2'))
text_input = pygame_gui.elements.UITextEntryLine(
     relative_rect = pygame.Rect((200, 200), (100, 25)),
     placeholder_text = 'enter %M2',
     manager = manager, object_id = ObjectID(class_id = 'text_entry_line',
                                             object_id = '#main_text_entry6'))
text_input = pygame_gui.elements.UITextEntryLine(
     relative_rect = pygame.Rect((100, 250), (100, 25)),
     placeholder_text = 'enter Hei',
     manager = manager, object_id = ObjectID(class_id = 'text_entry_line',
                                             object_id = '#main_text_entry3'))
text_input = pygame_gui.elements.UITextEntryLine(
     relative_rect = pygame.Rect((100, 100), (100, 25)),
     placeholder_text = 'enter m1',
     manager = manager, object_id = ObjectID(class_id = 'text_entry_line',
                                             object_id = '#main_text_entry4'))
text_input = pygame_gui.elements.UITextEntryLine(
     relative_rect = pygame.Rect((200, 100), (100, 25)),
     placeholder_text = 'enter m2',
     manager = manager, object_id = ObjectID(class_id = 'text_entry_line',
                                             object_id = '#main_text_entry5'))
manager.get_theme().load_theme(btheme)
button = pygame_gui.elements.ui_button.UIButton(
    relative_rect = pygame.Rect((100, 300), (100, 25)),
    text = 'OK', manager = manager, object_id = ObjectID(class_id = 'button',
                                             object_id = 'text_button'))

def momentum(gravity, height, momentumPercentage1, momentumPercentage2, mass1, mass2):
    runningmomentum = True
    xc1 = 470
    xc2 = 940
    yc = 650 - height #height from object dropped
    t = 1
    v = math.sqrt(2 * gravity * height) #acceleration due to gravity
    pi1 = mass1 * v
    pi2 = mass2 * v
    pf1 = (momentumPercentage1 * pi1) / 100 #momentum residue percentage
    pf2 = (momentumPercentage2 * pi2) / 100
    v1 = pf1 / mass1
    v2 = pf2 / mass2
    d1 = (v1 * v1) / (2 * gravity)
    d2 = (v2 * v2) / (2 * gravity)
    ycf1 = 650 - d1
    ycd1 = 650
    ycf2 = 650 - d2
    ycd2 = 650
    while runningmomentum:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runningmomentum = False
        window.fill(gray)
        if yc < 650:
            yc += 1
        pygame.draw.circle(window, red, (xc1, yc - 21), 20)
        pygame.draw.circle(window, blue, (xc2, yc - 21), 20)
        if yc == 650 and ycd1 >= ycf1:
            ycd1 -= 1
        if yc == 650 and ycd2 >= ycf2:
            ycd2 -= 1
        drawred = font.render(str(round(decimal.Decimal(d1), 2)), True, red)
        window.blit(drawred, (1280, ycf1 - 20))
        drawblue = font.render(str(round(decimal.Decimal(d2), 2)), True, blue)
        window.blit(drawblue, (1280, ycf2 - 20))
        drawblue = font.render('MAX BOUNCE', True, black)
        window.blit(drawblue, (1215, 100))
        drawblue = font.render('FINAL POSITION', True, black)
        window.blit(drawblue, (1200, 620))    
        pygame.draw.circle(window, red, (xc1, ycd1 - 21), 20)
        pygame.draw.line(window, red, (50, ycf1 - 1), (1270, ycf1 - 1), 2)
        pygame.draw.circle(window, blue, (xc2, ycd2 - 21), 20)
        pygame.draw.line(window, blue, (50, ycf2 - 1), (1270, ycf2 - 1), 2)
        pygame.draw.line(window, black, (50, 650), (1350, 650), 4)
        pygame.draw.line(window, black, (1350, 650), (1350, 50), 4)
        pygame.display.update()
def parameters():
    runningparameters = True
    gravity = 9.8
    height = 500
    momentumPercentage1 = 25
    momentumPercentage2 = 25
    mass1 = 700
    mass2 = 800
    while runningparameters:
        window.fill(gray)
        pygame.draw.line(window, black, (50, 650), (1350, 650), 4)
        pygame.draw.line(window, black, (1350, 650), (1350, 50), 4)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runningparameters = False
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry1'):
                gravity = float(event.text)
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry3'):
                height = int(event.text)
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry2'):
                momentumPercentage1 = int(event.text)
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry6'):
                momentumPercentage2 = int(event.text)
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry4'):
                mass1 = int(event.text)
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry5'):
                mass2 = int(event.text)    
            manager.process_events(event)    
            if (event.type == pygame_gui.UI_BUTTON_PRESSED and
                event.ui_object_id == 'text_button'):
                pygame_widgets.update(event)
                momentum(gravity, height, momentumPercentage1, momentumPercentage2, mass1, mass2)
        manager.update(clock.tick(60)/1000)    
        manager.draw_ui(window)
        pygame.display.update()
parameters()
pygame.quit()
