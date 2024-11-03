import pygame
pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
GOAL_WIDTH = 500
GOAL_HEIGHT = 250   
BALL_RADIUS = 50
KEEPER_WIDTH = 300      
KEEPER_HEIGHT = 200
FPS = 100  
WHITE = (255, 255, 255)
background_img = pygame.image.load('background.png')  
goalpost_img = pygame.image.load('goalpost.png')
goalkeeper_img = pygame.image.load('onana.png')
football_img = pygame.image.load('football.png')
penalty_taker_img = pygame.image.load('antony.png')
save_img = pygame.image.load('save.png')  
pygame.mixer.music.load('background_music.mp3.MPEG')  
goalpost_img = pygame.transform.scale(goalpost_img, (GOAL_WIDTH, GOAL_HEIGHT))
goalkeeper_img = pygame.transform.scale(goalkeeper_img, (KEEPER_WIDTH, KEEPER_HEIGHT))
football_img = pygame.transform.scale(football_img, (BALL_RADIUS * 2, BALL_RADIUS * 2))
penalty_taker_img = pygame.transform.scale(penalty_taker_img, (KEEPER_WIDTH, KEEPER_HEIGHT))
save_img = pygame.transform.scale(save_img, (300, 200))  
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Penalty Shootout Game")
def draw_goal():
    screen.blit(goalpost_img, (SCREEN_WIDTH // 2 - GOAL_WIDTH // 2, 1))
def main():
    clock = pygame.time.Clock()
    running = True
    ball_x = SCREEN_WIDTH // 2
    ball_y = SCREEN_HEIGHT - 100
    keeper_x = SCREEN_WIDTH // 2  
    score = 0
    ball_moving = False  
    show_save_image = False  
    save_image_timer = 0  
    pygame.mixer.music.play(-1)  
    target_y = 50  
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  
                    ball_x = min(SCREEN_WIDTH - BALL_RADIUS, ball_x + GOAL_WIDTH // 5)
                    ball_moving = True  
                elif event.key == pygame.K_l:  
                    ball_x = max(BALL_RADIUS, ball_x - GOAL_WIDTH // 5)
                    ball_moving = True  
                elif event.key == pygame.K_c:  
                    ball_x = SCREEN_WIDTH // 2
                    ball_moving = True  
        if ball_moving and ball_y > target_y:
            ball_y -= 5  
        if ball_x < keeper_x + KEEPER_WIDTH // 2:
            keeper_x -= 2  
        elif ball_x > keeper_x + KEEPER_WIDTH // 2:
            keeper_x += 2  
        keeper_x = max(SCREEN_WIDTH // 2 - GOAL_WIDTH // 2, min(keeper_x, SCREEN_WIDTH // 2 + GOAL_WIDTH // 2 - KEEPER_WIDTH))
        screen.blit(background_img, (0, 0))
        draw_goal()
        screen.blit(penalty_taker_img, (SCREEN_WIDTH // 2 - KEEPER_WIDTH // 2, SCREEN_HEIGHT - 150))
        screen.blit(football_img, (ball_x - BALL_RADIUS, ball_y - BALL_RADIUS))
        screen.blit(goalkeeper_img, (keeper_x, 50))
        if (keeper_x < ball_x < keeper_x + KEEPER_WIDTH) and (50 < ball_y < 50 + KEEPER_HEIGHT):
            print("Saved by the goalkeeper!")
            show_save_image = True  
            ball_moving = False 
            ball_x = SCREEN_WIDTH // 2
            ball_y = SCREEN_HEIGHT - 100
            save_image_timer = 60
        elif (SCREEN_WIDTH // 2 - GOAL_WIDTH // 2 < ball_x < SCREEN_WIDTH // 2 + GOAL_WIDTH // 2) and ball_y <= 50:
            print("Goal!")
            score += 1
            goal_sound.play()  
            ball_x = SCREEN_WIDTH // 2
            ball_y = SCREEN_HEIGHT - 100
            ball_moving = False  
            show_save_image = False
        if show_save_image:
            screen.blit(save_img, (SCREEN_WIDTH // 2 - 150, 100))  
            save_image_timer -= 1  
            if save_image_timer <= 0:
                show_save_image = False  
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(text, (10, 10))
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
if __name__ == "__main__":
    main()



