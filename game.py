import pygame
import sys
import config # Import the config Module

import random
import shapes


def init_game():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constanst from config
    pygame.display.set_caption(config.TITLE)
    return screen

font_style = pygame.font.SysFont('Arial', 40)
header = font_style.render('Main Menu', True, config.BLUE)

button_length = 200
button_height = 50
button_x = 300
button_y = 125
button1 = pygame.Rect(200,200,button_length,button_height)
button2 = pygame.Rect(200,270,button_length,button_height)
button3 = pygame.Rect(200,340,button_length,button_height)

button1_text = font_style.render("PLAY", True, config.BLACK)
button2_text = font_style.render("OPTIONS", True, config.BLACK)
button3_text = font_style.render("EXIT", True, config.BLACK)

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()

                if button1.collidepoint(mouse_pos):
                    print("Now playing the game!")
                elif button2.collidepoint(mouse_pos):
                    print("Game options!")
                elif button3.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True


def draw_text(screen, text,font,text_col,x,y):
    image = font.render(text,True,text_col)
    screen.blit(image,(x,y))

def draw_rectangle(screen, color, x, y, width, height):
    pygame.draw.rect(screen,color,x,y,width,height)

def draw_circle(screen,x,y,radius,color,thickness):
    pygame.draw.circle(screen,color,(x,y),radius, thickness)

def main():
    screen = init_game()
    running = True
    clock = pygame.time.Clock() # Initialize the clock her
    
    # font_style = pygame.font.SysFont('Arial', 40)
    # header = font_style.render('Main Menu', True, config.BLUE)

    # button_length = 200
    # button_height = 50
    # button_x = 300
    # button_y = 125
    # button1 = pygame.Rect(200,200,button_length,button_height)
    # button2 = pygame.Rect(200,270,button_length,button_height)
    # button3 = pygame.Rect(200,340,button_length,button_height)

    # button1_text = font_style.render("PLAY", True, config.BLACK)
    # button2_text = font_style.render("OPTIONS", True, config.BLACK)
    # button3_text = font_style.render("EXIT", True, config.BLACK)

    

    


    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config

        screen.blit(header, (215,150))

        pygame.draw.rect(screen, config.GREEN, button1)
        pygame.draw.rect(screen, config.GREEN, button2)
        pygame.draw.rect(screen, config.GREEN, button3)

        screen.blit(button1_text, (button1.x + (button_length - button1_text.get_width())) // 2, button1.y + (button_height - button1_text.get_height()) // 2)

        screen.blit(button2_text, (button2.x + (button_length - button2_text.get_width())) // 2, button2.y + (button_height - button2_text.get_height()) // 2)

        screen.blit(button3_text, (button3.x + (button_length - button3_text.get_width())) // 2, button3.y + (button_height - button3_text.get_height()) // 2)
        


        # circle_color = config.RED

        # draw_circle(screen,535,520, 40, circle_color, 0)
        # draw_text(screen, "button", text_font, config.BLACK, 500,500)

         
        
        pygame.display.flip()

        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS) # use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()