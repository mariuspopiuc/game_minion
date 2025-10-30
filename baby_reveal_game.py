#!/usr/bin/env python3
"""
Baby Reveal Puzzle Game
A fun interactive game with multiple puzzles that reveals a special announcement!
"""

import time
import random
import sys


class Colors:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def clear_screen():
    """Clear the terminal screen"""
    print("\n" * 50)


def print_slowly(text, delay=0.03):
    """Print text character by character for dramatic effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def print_header(text):
    """Print a formatted header"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'=' * 60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.YELLOW}{text.center(60)}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 60}{Colors.END}\n")


def welcome_message():
    """Display welcome message"""
    clear_screen()
    print_header("🎮 MYSTERY PUZZLE CHALLENGE 🎮")
    print(f"{Colors.BOLD}Welcome, brave puzzle solver!{Colors.END}\n")
    print("You are about to embark on an exciting journey...")
    print("Solve all the puzzles to unlock a very special message!\n")
    input(f"{Colors.GREEN}Press Enter to begin...{Colors.END}")


def puzzle_1_word_scramble():
    """Puzzle 1: Unscramble words related to the announcement"""
    clear_screen()
    print_header("PUZZLE 1: Word Scramble")
    
    words = [
        ("YABB", "BABY", "A young child"),
        ("UNNEJ", "JUNE", "The sixth month of the year"),
        ("ILFYMA", "FAMILY", "A group of related people"),
    ]
    
    print("Unscramble these words! Each one is a clue...\n")
    
    for scrambled, answer, hint in words:
        attempts = 0
        while attempts < 3:
            print(f"{Colors.CYAN}Scrambled word: {Colors.BOLD}{scrambled}{Colors.END}")
            print(f"Hint: {hint}")
            guess = input("Your answer: ").strip().upper()
            
            if guess == answer:
                print(f"{Colors.GREEN}✓ Correct! The word is {answer}!{Colors.END}\n")
                time.sleep(1)
                break
            else:
                attempts += 1
                if attempts < 3:
                    print(f"{Colors.RED}✗ Not quite. Try again! ({3 - attempts} attempts left){Colors.END}\n")
                else:
                    print(f"{Colors.YELLOW}The answer was: {answer}{Colors.END}\n")
                    time.sleep(1)
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 Puzzle 1 Complete!{Colors.END}")
    input(f"{Colors.GREEN}Press Enter to continue...{Colors.END}")
    return True


def puzzle_2_math_riddle():
    """Puzzle 2: Math riddles"""
    clear_screen()
    print_header("PUZZLE 2: Number Mysteries")
    
    riddles = [
        ("How many months are in half a year?", "6", ["six"]),
        ("What number comes after 2025?", "2026", []),
        ("If you add 3 + 6, what do you get? (This is when something special happens!)", "9", ["nine"]),
    ]
    
    print("Solve these number riddles!\n")
    
    for riddle, answer, alt_answers in riddles:
        attempts = 0
        while attempts < 3:
            print(f"{Colors.CYAN}{riddle}{Colors.END}")
            guess = input("Your answer: ").strip().lower()
            
            if guess == answer.lower() or guess in alt_answers:
                print(f"{Colors.GREEN}✓ Correct!{Colors.END}\n")
                time.sleep(1)
                break
            else:
                attempts += 1
                if attempts < 3:
                    print(f"{Colors.RED}✗ Try again! ({3 - attempts} attempts left){Colors.END}\n")
                else:
                    print(f"{Colors.YELLOW}The answer was: {answer}{Colors.END}\n")
                    time.sleep(1)
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 Puzzle 2 Complete!{Colors.END}")
    input(f"{Colors.GREEN}Press Enter to continue...{Colors.END}")
    return True


def puzzle_3_pattern():
    """Puzzle 3: Pattern recognition"""
    clear_screen()
    print_header("PUZZLE 3: Pattern Detective")
    
    print("What comes next in these sequences?\n")
    
    sequences = [
        ("January, February, March, April, May, ___?", "JUNE", "june"),
        ("2023, 2024, 2025, ___?", "2026", "2026"),
        ("Spring, Summer, Fall, Winter, ___?", "SPRING", "spring"),
    ]
    
    for question, answer, alt_answer in sequences:
        attempts = 0
        while attempts < 3:
            print(f"{Colors.CYAN}{question}{Colors.END}")
            guess = input("Your answer: ").strip()
            
            if guess.upper() == answer or guess.lower() == alt_answer:
                print(f"{Colors.GREEN}✓ Perfect!{Colors.END}\n")
                time.sleep(1)
                break
            else:
                attempts += 1
                if attempts < 3:
                    print(f"{Colors.RED}✗ Not quite right! ({3 - attempts} attempts left){Colors.END}\n")
                else:
                    print(f"{Colors.YELLOW}The answer was: {answer}{Colors.END}\n")
                    time.sleep(1)
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 Puzzle 3 Complete!{Colors.END}")
    input(f"{Colors.GREEN}Press Enter to continue...{Colors.END}")
    return True


def puzzle_4_trivia():
    """Puzzle 4: Trivia questions"""
    clear_screen()
    print_header("PUZZLE 4: Quick Trivia")
    
    questions = [
        {
            "question": "What do you call a very young child?",
            "options": ["A) Toddler", "B) Baby", "C) Teen", "D) Adult"],
            "answer": "B"
        },
        {
            "question": "In which month does summer begin in the Northern Hemisphere?",
            "options": ["A) May", "B) June", "C) July", "D) August"],
            "answer": "B"
        },
        {
            "question": "What year comes after 2025?",
            "options": ["A) 2024", "B) 2025", "C) 2026", "D) 2027"],
            "answer": "C"
        },
    ]
    
    print("Answer these trivia questions!\n")
    
    for i, q in enumerate(questions, 1):
        print(f"{Colors.YELLOW}Question {i}:{Colors.END} {q['question']}")
        for option in q['options']:
            print(f"  {option}")
        
        attempts = 0
        while attempts < 2:
            answer = input("\nYour answer (A/B/C/D): ").strip().upper()
            
            if answer == q['answer']:
                print(f"{Colors.GREEN}✓ Excellent!{Colors.END}\n")
                time.sleep(1)
                break
            else:
                attempts += 1
                if attempts < 2:
                    print(f"{Colors.RED}✗ Try again!{Colors.END}")
                else:
                    print(f"{Colors.YELLOW}The answer was: {q['answer']}{Colors.END}\n")
                    time.sleep(1)
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 Puzzle 4 Complete!{Colors.END}")
    input(f"{Colors.GREEN}Press Enter to continue...{Colors.END}")
    return True


def final_reveal():
    """The big reveal!"""
    clear_screen()
    print_header("🎊 CONGRATULATIONS! 🎊")
    
    print(f"{Colors.BOLD}You've solved all the puzzles!{Colors.END}")
    print("\nNow it's time to reveal the special message...\n")
    time.sleep(2)
    
    print(f"{Colors.YELLOW}Decoding...{Colors.END}")
    time.sleep(1)
    print(f"{Colors.YELLOW}Decoding...{Colors.END}")
    time.sleep(1)
    print(f"{Colors.YELLOW}Decoding...{Colors.END}")
    time.sleep(1)
    
    clear_screen()
    
    # The big announcement!
    announcement = [
        "",
        "╔═══════════════════════════════════════════════════════════╗",
        "║                                                           ║",
        "║                  🍼  SPECIAL ANNOUNCEMENT  🍼             ║",
        "║                                                           ║",
        "║              A NEW BABY IS ON THE WAY! 👶                ║",
        "║                                                           ║",
        "║                  Expected Arrival:                        ║",
        "║                  EARLY JUNE 2026                          ║",
        "║                                                           ║",
        "║            Get ready for a new adventure! 💕              ║",
        "║                                                           ║",
        "╚═══════════════════════════════════════════════════════════╝",
        "",
    ]
    
    for line in announcement:
        print(f"{Colors.BOLD}{Colors.CYAN}{line}{Colors.END}")
        time.sleep(0.3)
    
    print("\n")
    print_slowly("🎉 🎊 🎈 🎁 👶 💝 🌟 ✨ 💫 🎉 🎊 🎈", 0.1)
    print("\n")
    
    print(f"{Colors.GREEN}{Colors.BOLD}Thank you for playing!{Colors.END}")
    print(f"{Colors.YELLOW}We hope you're as excited as we are!{Colors.END}\n")


def main():
    """Main game flow"""
    welcome_message()
    
    # Run all puzzles
    puzzle_1_word_scramble()
    puzzle_2_math_riddle()
    puzzle_3_pattern()
    puzzle_4_trivia()
    
    # Final reveal
    final_reveal()


if __name__ == "__main__":
    main()
