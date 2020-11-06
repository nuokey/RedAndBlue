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
        image = pygame.image.load(texture_file)
        x = self.x * 100
        y = self.y * 100
        screen.blit(image, (x, y))

        if mouse_pressed:
            x = abs(pygame.mouse.get_pos()[0] - self.x * image.get_width() - image.get_width() // 2)
            y = abs(pygame.mouse.get_pos()[1] - self.y * image.get_height() - image.get_height() // 2)
            if x < image.get_width() // 2 and y < image.get_height() // 2:
                self.change()

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

size = (settings.cells_width * 100, settings.cells_height * 100)
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