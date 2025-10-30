#!/usr/bin/env python3
"""
Automated test for the baby reveal game
Tests all puzzles and verifies the game runs to completion
"""

import subprocess
import sys

def test_game():
    """Test the game with automated inputs"""
    
    # Provide inputs for all puzzles
    # Each line represents an answer to a prompt
    inputs = [
        "",           # Press Enter to begin
        "BABY",       # Puzzle 1 - Word 1
        "JUNE",       # Puzzle 1 - Word 2
        "FAMILY",     # Puzzle 1 - Word 3
        "",           # Press Enter to continue
        "6",          # Puzzle 2 - Question 1
        "2026",       # Puzzle 2 - Question 2
        "9",          # Puzzle 2 - Question 3
        "",           # Press Enter to continue
        "JUNE",       # Puzzle 3 - Question 1
        "2026",       # Puzzle 3 - Question 2
        "SPRING",     # Puzzle 3 - Question 3
        "",           # Press Enter to continue
        "B",          # Puzzle 4 - Question 1
        "B",          # Puzzle 4 - Question 2
        "C",          # Puzzle 4 - Question 3
        "",           # Press Enter to continue (final reveal)
    ]
    
    input_string = "\n".join(inputs)
    
    try:
        result = subprocess.run(
            ["python3", "baby_reveal_game.py"],
            input=input_string,
            capture_output=True,
            text=True,
            timeout=10
        )
        
        output = result.stdout
        
        # Check for success indicators
        success_indicators = [
            "BABY",
            "JUNE",
            "2026",
            "SPECIAL ANNOUNCEMENT",
            "NEW BABY IS ON THE WAY",
            "EARLY JUNE 2026",
            "Puzzle 1 Complete",
            "Puzzle 2 Complete",
            "Puzzle 3 Complete",
            "Puzzle 4 Complete",
        ]
        
        print("Testing Baby Reveal Game...")
        print("=" * 60)
        
        all_found = True
        for indicator in success_indicators:
            if indicator in output:
                print(f"✓ Found: {indicator}")
            else:
                print(f"✗ Missing: {indicator}")
                all_found = False
        
        print("=" * 60)
        
        if all_found and result.returncode == 0:
            print("\n✓ All tests passed! Game works correctly.")
            return True
        else:
            print(f"\n✗ Some tests failed. Return code: {result.returncode}")
            if result.stderr:
                print(f"Errors: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("✗ Test timed out")
        return False
    except Exception as e:
        print(f"✗ Test error: {e}")
        return False


if __name__ == "__main__":
    success = test_game()
    sys.exit(0 if success else 1)
