import pygame,sys
from const import *
from game import GAME

class MAIN:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('chess')
        self.game = GAME()
        self.dragger = self.game.dragger


    def mainloop(self):
        game = self.game
        screen = self.screen
        while True:
            game.show_bg(screen)
            game.show_pieces(screen)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                
                elif event.type == pygame.MOUSEMOTION:
                    pass

                #click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
                #quite
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()




            
            pygame.display.update()

main = MAIN()
main.mainloop()