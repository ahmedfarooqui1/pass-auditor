import math
import re
import sys

def calculate_entropy(password):
    if not password:
        return 0.0
    pool_size = 0
    if re.search(r'[a-z]', password): pool_size += 26
    if re.search(r'[A-Z]', password): pool_size += 26
    if re.search(r'[0-9]', password): pool_size += 10
    if re.search(r'[^a-zA-Z0-9]', password): pool_size += 32
    if pool_size == 0: return 0.0
    return round(len(password) * math.log2(pool_size), 2)

def evaluate_strength(password):
    score = 0
    feedback = []
    if len(password) >= 12: score += 2
    elif len(password) >= 8: score += 1
    else: feedback.append("Password is too short (<8 chars).")
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password): score += 1
    else: feedback.append("Add both uppercase and lowercase letters.")
    if re.search(r'[0-9]', password): score += 1
    else: feedback.append("Add numbers.")
    if re.search(r'[^a-zA-Z0-9]', password): score += 1
    else: feedback.append("Add special symbols.")
    
    entropy = calculate_entropy(password)
    print(f"[*] Length: {len(password)} | Entropy: {entropy} bits")
    if entropy > 60: print("[+] Status: HIGHLY SECURE")
    elif entropy > 40: print("[~] Status: MODERATE")
    else: print("[-] Status: WEAK")
    for tip in feedback: print(f"    - {tip}")

if __name__ == "__main__":
    pwd = sys.argv[1] if len(sys.argv) > 1 else input("Enter password: ")
    evaluate_strength(pwd)
