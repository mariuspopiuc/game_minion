#!/usr/bin/env python3
"""
Demo script to show the baby announcement reveal
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(__file__))

from baby_reveal_game import final_reveal, Colors, print_header

def demo():
    """Show a quick demo of the final reveal"""
    print_header("🎮 BABY REVEAL GAME DEMO 🎮")
    print(f"{Colors.BOLD}This is what players will see after solving all puzzles:{Colors.END}\n")
    input("Press Enter to see the reveal...")
    final_reveal()

if __name__ == "__main__":
    demo()
