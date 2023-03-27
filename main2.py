import pygame
import sys
import random


pygame.init()
res = (720, 720)
screen = pygame.display.set_mode(res)

# couleur de police
color = (255, 255, 255)
color2 = (255,0,0)

# bouton clair
color_light = (170, 170, 170)

# bouton noir
color_dark = (100, 100, 100)

# stock la largeur de l'ecran dans une variable
width = screen.get_width()
width_oui = 100

# stock hauteur de l'écran dans une variable
height = screen.get_height()
height_oui = 720

# police de caractère
smallfont = pygame.font.SysFont('Lato', 35)


counter = 0

text = smallfont.render('Non', True, color)
text2 = smallfont.render("Est-ce que la Dream's est la meilleure ASSO ?", True, color)
text3 = smallfont.render('Oui', True, color)
text4 = smallfont.render("", True, color2)

while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            sys.exit()

        if ev.type == pygame.MOUSEBUTTONDOWN:

            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                width=random.randint(0, 1300)
                height=random.randint(0, 1300)
                counter += 1

            if width_oui / 2 <= mouse[0] <= width_oui / 2 + 140 and height_oui / 2 <= mouse[1] <= height_oui / 2 + 40:
                if counter == 0 :
                    text4 = smallfont.render("Evidemment !!!!", True, color2)
                else :
                    text4 = smallfont.render("Comment oses-tu cliquer " + str(counter) + " fois sur 'non' ???", True, color2)

    # couleur ecran
    screen.fill((200, 173, 127))

    # stocker les (x,y) comme des variables dans un tuple
    mouse = pygame.mouse.get_pos()

    # si la souris est sur le bouton, on change la couleur
    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, color_light, [width / 2, height / 2, 140, 40])

    else:
        pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 140, 40])

    if width_oui / 2 <= mouse[0] <= width_oui / 2 + 140 and height_oui / 2 <= mouse[1] <= height_oui / 2 + 40:
        pygame.draw.rect(screen, color_light, [width_oui / 2, height_oui / 2, 140, 40])

    else:
        pygame.draw.rect(screen, color_dark, [width_oui / 2, height_oui / 2, 140, 40])

    # superposer le texte sur l'ecran
    screen.blit(text, (width / 2 + 50, height / 2))
    screen.blit(text2, (100, 100))
    screen.blit(text3, (width_oui / 2 + 50, height_oui / 2))
    screen.blit(text4, (100, 150))
    # mettre a jour l'affichage pygame
    pygame.display.update()