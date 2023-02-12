
with open('/usr/share/dict/words', 'r') as f:
    words = f.read().splitlines()                # careful of memory usage

words.sort(key=len, reverse=True)

print(words[:5]) 
