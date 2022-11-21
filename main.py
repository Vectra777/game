import pygame


pygame.init()
WIDTH, HEIGHT = 900,900
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
WHITE=255, 255, 255
CAPTION=pygame.display.set_caption("game of the year")
CLOCK = pygame.time.Clock()

start = pygame.image.load('start.png')
start = pygame.transform.scale(start, (200,200))
start_rect = start.get_rect()


while True:
    start_rect.center
    CLOCK.tick(60)
    mouse = pygame.mouse.get_pos()
    event = pygame.event.wait()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    WIN.fill(WHITE)
    WIN.blit(start, (200,200))
    
    match event.type:
        
        case pygame.MOUSEBUTTONDOWN:
            
            match event.button:
                
                case 1:
                    if start_rect.collidepoint(pygame.mouse.get_pos()):
                        print("yay")
                case 3:
                    print("right click")
                    
    if start_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
    pygame.display.update()

