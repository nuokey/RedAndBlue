import pygame
import settings

class Cell():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.colors = ['red', 'blue',  'green', 'white']
        self.color_number = 0
    
    def draw(self):
        texture_file = self.colors[self.color_number] + '.png'
        self.image = pygame.image.load(texture_file)
        self.image = pygame.transform.scale(self.image, (settings.window_width // settings.cells_width, settings.window_height // settings.cells_height))

        x = self.x * self.image.get_width()
        y = self.y * self.image.get_height()
        screen.blit(self.image, (x, y))

        if mouse_pressed:
            x = abs(pygame.mouse.get_pos()[0] - self.x * self.image.get_width() - self.image.get_width() // 2)
            y = abs(pygame.mouse.get_pos()[1] - self.y * self.image.get_height() - self.image.get_height() // 2)
            if x < self.image.get_width() // 2 and y < self.image.get_height() // 2:
                self.change()
                print(self.color_number)

    def change(self):
        if self.color_number != len(self.colors) - 1:
            self.color_number += 1
        else:
            self.color_number = 0

def update():
    for i in cells:
        for q in i:
            q.draw()

cell_width = 100
cells = []
for y in range(settings.cells_height):
    cells.append([])
    for x in range(settings.cells_width):
        cells[y].append(Cell(x, y))

size = (settings.window_width, settings.window_height)
pygame.init()
screen = pygame.display.set_mode(size)


clock = pygame.time.Clock()
done = False

while not done:
    clock.tick(60)
    screen.fill((255, 255, 255))
    mouse_pressed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True

    update()

    pygame.display.flip()
pygame.quit()