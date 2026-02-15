"""
ASCII Art Module for Snowman Game

This module contains the visual representations of the snowman in various states
of melting. Each stage represents the snowman's condition based on the number
of incorrect guesses made by the player.

The STAGES list contains ASCII art drawings that progressively show the snowman
melting from a complete figure to completely melted.
"""


# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman (no mistakes yet)
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting (1 mistake)
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains (2 mistakes)
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted (3 mistakes - game over)
     """
      ___  
     /___\\ 
     """
 ]