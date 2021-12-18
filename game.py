# This game is not owned by any of the problemsetters, it belongs to Akshar Singh
# for queries regarding the game(how he made it and how it works and all) contact him

import os 
import cfg
import game
import sys
import pygame
import random
from modules import *
from PIL.ImageChops import screen


def initGame():

    pygame.init()
    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption('catch coins')

    game_images = {}
    for key, value in cfg.IMAGE_PATHS.items():
        if isinstance(value, list):
            images = []
            for item in value: images.append(pygame.image.load(item))
            game_images[key] = images
        else:
            game_images[key] = pygame.image.load(value)
            
    game_sounds = {}
    for key, value in cfg.AUDIO_PATHS.items():
        if key == 'bgm': continue
        game_sounds[key] = pygame.mixer.Sound(value)

    return screen, game_images, game_sounds


def main():
    
    screen, game_images, game_sounds = initGame()

    pygame.mixer.music.load(cfg.AUDIO_PATHS['bgm'])
    pygame.mixer.music.play(-1, 0.0)

    font = pygame.font.Font(cfg.FONT_PATH, 40)

    hero = Hero(game_images['hero'], position=(375, 520))

    food_sprites_group = pygame.sprite.Group()
    generate_food_freq = random.randint(10, 20)
    generate_food_count = 0

    score = 1000
    highest_score = 0 if not os.path.exists(cfg.HIGHEST_SCORE_RECORD_FILEPATH) else int(open(cfg.HIGHEST_SCORE_RECORD_FILEPATH).read())

    clock = pygame.time.Clock()
    
    
    while True: 
        
        screen.fill(0)
        screen.blit(game_images['background'], (0,0))
        
        
        countdown_text = 'Count down: ' + str((90000 - pygame.time.get_ticks()) // 60000) + ":" + str((90000 - pygame.time.get_ticks()) // 1000 % 60).zfill(2)
        countdown_text = font.render(countdown_text, True, (150,0,0))
        countdown_rect = countdown_text.get_rect()
        countdown_rect.topright = [cfg.SCREENSIZE[0]-30, 5]
        screen.blit(countdown_text, countdown_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
                
        key_pressed = pygame.key.get_pressed()
        
        if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            hero.move(cfg.SCREENSIZE, 'left')
        if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            hero.move(cfg.SCREENSIZE, 'right')
            
        
        generate_food_count += 1
        if generate_food_count > generate_food_freq:
            generate_food_freq = random.randint(10, 20)
            generate_food_count = 0
            food = Food(game_images, random.choice(['gold',] * 10), cfg.SCREENSIZE)
            food_sprites_group.add(food)
        
        for food in food_sprites_group:
            if food.update(): food_sprites_group.remove(food)
        
        for food in food_sprites_group:
            if pygame.sprite.collide_mask(food, hero):
                game_sounds['get'].play()
                food_sprites_group.remove(food)
                score += food.score
                if score > highest_score: highest_score = score
        
        hero.draw(screen)
        
        food_sprites_group.draw(screen)
        
        score_text = f'Score: {score}, Highest: {highest_score}'
        score_text = font.render(score_text, True, (150,0,0))
        score_rect = score_text.get_rect()
        score_rect.topleft = [5, 5]
        screen.blit(score_text, score_rect)
        
        if pygame.time.get_ticks() >= 90000:
            break
        
        pygame.display.flip()
        clock.tick(cfg.FPS)
    
        
    fp = open(cfg.HIGHEST_SCORE_RECORD_FILEPATH, 'w')
    fp.write(str(highest_score))
    fp.close()
    
    return showEndInterface(screen, cfg, score, highest_score,game)



if __name__ == '__main__':
    while main():
            pass
        
        

            
            
            
# Credits for the game: Akshar Singh            
            
