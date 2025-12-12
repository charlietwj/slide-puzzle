import pygame

class Game:

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self) -> None:
        pass

    def draw(self) -> None:
        self.screen.fill((0, 0, 0))
        
        pygame.display.flip()

    def run(self) -> None:
        self.running = True
    
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
