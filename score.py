import pygame
import os
from constants import SCORE_SCALAR, SCORE_PATH
from asteroid import Asteroid

def set_up_score(path):
    directory = os.path.dirname(path)
    if not os.path.exists(path):
        if not os.path.exists(directory):
            os.mkdir(directory)
        with open(path, "w") as score_file:
            score_file.write("0")
def update_score(asteroid, original_score):
    score_modifier = SCORE_SCALAR / asteroid.scale
    current_score = int(original_score + score_modifier)
    return current_score
def save_score(score):
    with open(SCORE_PATH, "w") as high_score_file:
        high_score_file.write(f"{score}")
def retrieve_score():
    with open(SCORE_PATH) as high_score_file:
        previous_high_score = int(high_score_file.read())
        return previous_high_score
def check_score(current_score):
    previous_high_score = retrieve_score()
    if current_score >= previous_high_score:
        save_score(current_score)
        print(f"New high score of {current_score}!")
    else:
        print(f"Final score of {current_score}. Your high score is {previous_high_score}.")