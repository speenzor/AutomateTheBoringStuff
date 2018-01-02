#! usr/bin/env python3
#Chapter 11 Challenge: 2048
#Opens Safari to play 2048 by going up, right, down, left until Game Over, then stops.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Safari()
browser.get('https://gabrielecirulli.github.io/2048/')
game = browser.find_element_by_class_name('title')
#gameover = browser.find_element_by_class_name('game-message game-over')
while True:
    game.send_keys(Keys.UP)
    game.send_keys(Keys.RIGHT)
    game.send_keys(Keys.DOWN)
    game.send_keys(Keys.LEFT)
    try:
        gameover = browser.find_element_by_class_name('game-message game-over')
        if gameover != '':
            break
    except:
        continue
