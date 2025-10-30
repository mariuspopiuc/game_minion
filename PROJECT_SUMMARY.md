# Baby Reveal Puzzle Game - Project Summary

## Overview
This repository contains an interactive puzzle game designed to reveal a special baby announcement. The game features 4 unique puzzles that progressively hint at the final reveal.

## Game Features

### 🎮 Interactive Gameplay
- Terminal-based game with colorful ANSI output
- User-friendly prompts and feedback
- Multiple attempts allowed for each puzzle
- Progressive difficulty building to the reveal

### 🧩 Four Unique Puzzles

#### Puzzle 1: Word Scramble
Unscramble words related to the announcement:
- YABB → BABY
- UNNEJ → JUNE  
- ILFYMA → FAMILY

#### Puzzle 2: Math Riddles
Solve number-based riddles:
- Months in half a year → 6
- Year after 2025 → 2026
- Sum of 3 + 6 → 9 (September/month when baby was conceived)

#### Puzzle 3: Pattern Recognition
Complete the sequences:
- Months: Jan, Feb, Mar, Apr, May → JUNE
- Years: 2023, 2024, 2025 → 2026
- Seasons: Spring, Summer, Fall, Winter → SPRING

#### Puzzle 4: Trivia Quiz
Multiple choice questions about babies and dates:
- What is a very young child called?
- When does summer begin?
- What year comes after 2025?

### 🎊 The Grand Reveal

After solving all puzzles, players are treated to a beautiful announcement:

```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║                  🍼  SPECIAL ANNOUNCEMENT  🍼             ║
║                                                           ║
║              A NEW BABY IS ON THE WAY! 👶                ║
║                                                           ║
║                  Expected Arrival:                        ║
║                  EARLY JUNE 2026                          ║
║                                                           ║
║            Get ready for a new adventure! 💕              ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

## Files in This Repository

- **baby_reveal_game.py** - Main game file (executable)
- **README.md** - User guide and instructions
- **WALKTHROUGH.md** - Complete solutions to all puzzles
- **demo_reveal.py** - Quick demo of the final reveal
- **test_game.py** - Automated testing script
- **run_game_preview.sh** - Preview script showing game overview
- **.gitignore** - Excludes Python cache files

## How to Use

### Play the Game
```bash
python3 baby_reveal_game.py
```

### See Just the Reveal
```bash
python3 demo_reveal.py
```

### View Game Overview
```bash
./run_game_preview.sh
```

## Technical Details

- **Language**: Python 3.6+
- **Dependencies**: None (standard library only)
- **Platform**: Cross-platform (Linux, macOS, Windows)
- **Display**: Best in terminals supporting ANSI colors

## Design Philosophy

The game was designed with several key principles:

1. **Progressive Hints**: Each puzzle subtly hints at the announcement
2. **Engaging Experience**: Interactive and fun, not frustrating
3. **Beautiful Reveal**: The announcement is presented with care and celebration
4. **No Spoilers**: The reveal isn't obvious until all puzzles are solved
5. **Accessibility**: Simple to run, no complex dependencies

## Puzzle Design

All puzzles cleverly incorporate elements of the announcement:
- **BABY** - The central theme
- **JUNE** - The expected month
- **2026** - The expected year
- **FAMILY** - What's growing
- **6** - June is the 6th month
- **9** - Approximate conception month (9 months before June)

The puzzles gradually reveal these elements, building anticipation for the final announcement.

## Special Touches

- 🎨 Colorful terminal output with ANSI codes
- ⏱️ Dramatic delays and animations
- 💬 Encouraging feedback messages
- 🎉 Celebratory final reveal
- 🎯 Multiple attempts to reduce frustration
- 📝 Clear instructions and hints

---

**Created with ❤️ for a very special announcement**

*Baby due: Early June 2026* 👶
