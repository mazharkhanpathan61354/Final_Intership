# password_analyzer.py

import zxcvbn
from zxcvbn import zxcvbn as zxcvbn_check
import argparse
import os

# Leetspeak replacements
LEET_DICT = {'a': ['@', '4'], 'e': ['3'], 'i': ['1', '!'], 'o': ['0'], 's': ['$', '5'], 't': ['7']}

def password_strength(password):
    result = zxcvbn_check(password)
    score = result['score']
    feedback = result['feedback']
    return score, feedback

def generate_custom_wordlist(base_words, years=range(2000, 2026)):
    wordlist = set()

    for word in base_words:
        wordlist.add(word)
        for year in years:
            wordlist.add(f"{word}{year}")
            wordlist.add(f"{year}{word}")

        for c in word:
            if c in LEET_DICT:
                for l in LEET_DICT[c]:
                    wordlist.add(word.replace(c, l))

    return sorted(wordlist)

def save_wordlist(wordlist, filename='custom_wordlist.txt'):
    with open(filename, 'w') as file:
        for word in wordlist:
            file.write(word + '\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Password Strength Checker and Custom Wordlist Generator")
    parser.add_argument('--password', type=str, help="Password to evaluate")
    parser.add_argument('--generate', nargs='+', help="Base words for wordlist generation (e.g. name birthdate petname)")
    args = parser.parse_args()

    if args.password:
        score, feedback = password_strength(args.password)
        print(f"Strength Score (0-4): {score}")
        if feedback['warning']:
            print("Warning:", feedback['warning'])
        if feedback['suggestions']:
            print("Suggestions:", ' '.join(feedback['suggestions']))

    if args.generate:
        words = args.generate
        wordlist = generate_custom_wordlist(words)
        save_wordlist(wordlist)
        print(f"Custom wordlist saved to 'custom_wordlist.txt' with {len(wordlist)} entries.")
