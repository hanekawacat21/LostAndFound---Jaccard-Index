import re 
from typing import Set

def preprocess_text(raw_text: str, stopwords: Set[str]) -> Set[str]:
    cleaned = re.sub(r"[^a-z0-9]+", " ", raw_text.lower())
    words = cleaned.split()
    tokens = set()
    for word in words: 
        if word not in stopwords:
            tokens.add(word)

    
    for w1,w2 in zip(words, words[1:]):
        if w1 not in stopwords and w2 not in stopwords: 
            tokens.add(f"{w1}_{w2}")      

    return tokens

        
