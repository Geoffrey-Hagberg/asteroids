import pygame
from enum import Enum
from constants import BIOME_THRESHOLD

class Biome(Enum):
    STANDARD = 1
    HARDENED = 2

def update_biome(current_score, current_biome):
    if (current_score >= (BIOME_THRESHOLD * current_biome.value)) and (current_biome.value < max(biome.value for biome in Biome)):
        next_biome = Biome(current_biome.value + 1)
        current_biome = next_biome
    return current_biome

def biome_colors(entity_type, current_biome):
    match current_biome:
        case Biome.STANDARD:
            return standard_colors(entity_type)
        case Biome.HARDENED:
            return hardened_colors(entity_type)

def standard_colors(entity_type):
    match entity_type:
        case "UI":
            ui_color = (255, 255, 255)
            return ui_color
        case "asteroid":
            z1_color = (255, 255, 255)
            z2_color = (185, 185, 185)
            z3_color = (105, 105, 105)
            return z1_color, z2_color, z3_color

def hardened_colors(entity_type):
    match entity_type:
        case "UI":
            ui_color = (255, 160, 0)
            return ui_color
        case "asteroid":
            z1_color = (160, 100, 60)
            z2_color = (160, 80, 45)
            z3_color = (160, 60, 30)
            return z1_color, z2_color, z3_color
        case "cracked_asteroid":
            z1_color = (200, 0, 0)
            z2_color = (180, 15, 15)
            z3_color = (160, 30, 30)
            return z1_color, z2_color, z3_color