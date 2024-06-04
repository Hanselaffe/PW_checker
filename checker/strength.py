import re

def check_strength(password):
    length = len(password)
    uppercase = bool(re.search(r'[A-Z]', password))
    lowercase = bool(re.search(r'[a-z]', password))
    digits = bool(re.search(r'\d', password))
    special_chars = bool(re.search(r'[\W_]', password))
    
    score = 0
    if length >= 8:
        score += 1
    if uppercase:
        score += 1
    if lowercase:
        score += 1
    if digits:
        score += 1
    if special_chars:
        score += 1
    
    return {
        'length': length,
        'uppercase': 'Yes' if uppercase else 'No',
        'lowercase': 'Yes' if lowercase else 'No',
        'digits': 'Yes' if digits else 'No',
        'special_chars': 'Yes' if special_chars else 'No',
        'score': score
    }
