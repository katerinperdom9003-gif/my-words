#!/usr/bin/env python3
"""Add words to words.json and make their audio. Usage: python3 add_words.py word1 "two words" ...
Needs: pip install --user --break-system-packages gTTS. Then commit and push."""
import json, sys
from gtts import gTTS
words = json.load(open('words.json'))
have = {w['word'].lower() for w in words}
for w in sys.argv[1:]:
    w = w.strip()
    if not w or w.lower() in have: continue
    words.append({"word": w}); have.add(w.lower())
    slug = 'audio/' + '-'.join(w.lower().split())
    gTTS(w, lang='en', tld='us').save(slug + '.mp3')
    gTTS(w, lang='en', tld='us', slow=True).save(slug + '-slow.mp3')
    print('added', w)
json.dump(words, open('words.json', 'w'), indent=2)
