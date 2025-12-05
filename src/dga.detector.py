import random
import string

def generate_random_domain(length=12):
    """Generate a random domain name (DGA-style)."""
    letters = string.ascii_lowercase
    domain = ''.join(random.choice(letters) for _ in range(length))
    return domain + ".com"

def is_suspicious(domain):
    """Simple rule-based detection for random-looking domains."""
    vowels = "aeiou"
    vowel_count = sum(1 for ch in domain if ch in vowels)
    ratio = vowel_count / len(domain.replace(".com", ""))

    if ratio < 0.2:        # too few vowels → suspicious
        return True
    return False
