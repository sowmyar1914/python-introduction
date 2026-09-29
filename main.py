import random

quotes = [
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("It always seems impossible until it's done.", "Nelson Mandela"),
    ("The future depends on what you do today.", "Mahatma Gandhi"),
    ("Dream big and dare to fail.", "Norman Vaughan"),
    ("Do what you can, with what you have, where you are.", "Theodore Roosevelt"),
    ("Act as if what you do makes a difference. It does.", "William James"),
    ("Start where you are. Use what you have. Do what you can.", "Arthur Ashe"),
    ("Success is not final, failure is not fatal.", "Winston Churchill"),
    ("You are never too old to set another goal or dream a new dream.", "C. S. Lewis"),
]

quote, author = random.choice(quotes)

print(f'"{quote}" — {author}')
