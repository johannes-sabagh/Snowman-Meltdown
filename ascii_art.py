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

    # Stage 1: Bottom starts shrinking
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
      :    
    """,

    # Stage 2: Lower body mostly gone
    """
      ___  
     /___\\ 
     (o o) 
      :    
      :    
    """,

    # Stage 3: Only one body segment left
    """
      ___  
     /___\\ 
     (o o) 
      :    
    """,

    # Stage 4: Body gone, head only
    """
      ___  
     /___\\ 
     (o o) 
    """,

    # Stage 5: Face starts melting
    """
      ___  
     /___\\ 
     (o .) 
    """,

    # Stage 6: Almost melted
    """
      ___  
     /___\\ 
     ( . ) 
    """,

    # Stage 7: Completely melted (game over)
    """
      ___  
     /___\\ 
    """
]