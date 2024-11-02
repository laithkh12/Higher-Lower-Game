# 📊 Higher Lower Game

Welcome to the **Higher Lower Game**! In this game, users compare the popularity of famous personalities, brands, and organizations based on their social media followers. The user has to guess who has more followers and can play for as long as they keep guessing correctly!

## 🎮 How to Play

1. Run the program, and a random account will be selected as **Account A**.
2. Another random account will be selected as **Account B**.
3. You’ll see descriptions of both accounts (their name, profession, and country).
4. **Guess** which account has **more followers** by typing "A" or "B".
5. If you're correct, your score increases, and you move to the next round, with **Account B** becoming the new **Account A**.
6. The game continues until you guess incorrectly, at which point your final score is displayed.

## 🖥️ Code Overview

### main.py

The main file of the project, responsible for:

- Displaying the game’s logo and user prompts.
- Managing the game's state, including generating random accounts and checking answers.
- Keeping track of the user's score.

### art.py

Contains ASCII art used to display the game’s logo and the **vs** symbol between two accounts.

```plaintext
 __  ___       __             
/ / / (_)___ _/ /_  ___  _____
/ /_/ / / __ '/ __ \/ _ \/ ___/
/ __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
  / /  /____/_      _____  _____
 / /   / __ \ | /| / / _ \/ ___/
/ /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/  
```

## game_data.py
Contains a list of dictionaries where each dictionary represents an account with details including:
  - name: Name of the person or organization.
  - follower_count: Number of social media followers.
  - description: Short description of who they are or what they do.
  - country: Country they are from.

## 💻 Usage
To start the game, run:
```python
python main.py
```

## 🌟 Features
- Randomized Accounts: Each round, two accounts are selected randomly to keep the game unpredictable.
- Score Keeping: The score increases with each correct guess.
- Clear Screen: The screen clears between rounds for a smooth gameplay experience.

## 🛠️ Requirements
- Python 3.x

## 📝 Sample Output
```python
Compare A: Cristiano Ronaldo, a Footballer, from Portugal
_vs_
Against B: Taylor Swift, a Musician, from United States

Who has more followers? 'A' or 'B': a
Correct! Current score: 1
```

## 🎉 Conclusion
Test your intuition on social media followings! Play the Higher Lower Game and see how many rounds you can complete! 🎉
