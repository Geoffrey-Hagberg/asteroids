import pygame
from enum import Enum
from constants import BIOME_THRESHOLD, Z1_COLOR, Z2_COLOR, Z3_COLOR

class Biome(Enum):
    START = 1
    TEST = 2

def update_biome(current_score, current_biome):
    # if current_score >= (BIOME_THRESHOLD * current_biome.value):
    return current_biome
def biome_colors(entity_type, current_biome):
    match current_biome:
        case Biome.START:
            return start_colors(entity_type)
        case Biome.TEST:
            pass
def start_colors(entity_type):
    if entity_type == "UI":
        ui_color = "orange"
        return ui_color
    if entity_type == "asteroid":
        z1_color = Z1_COLOR
        z2_color = Z2_COLOR
        z3_color = Z3_COLOR
        return z1_color, z2_color, z3_color