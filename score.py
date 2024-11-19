import pygame
from constants import SCORE_SCALAR
from asteroid import Asteroid

def update_score(asteroid, original_score):
    score_modifier = SCORE_SCALAR / asteroid.scale
    current_score = int(original_score + score_modifier)
    return current_score