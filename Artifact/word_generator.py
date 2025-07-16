import random

# Step 1: Generate the random word
alphabet = ['a', 'b', 'c']
word = [random.choice(alphabet) for _ in range(100)]

# Step 2: Write the word to a text file with space-separated letters
filename = 'random_word.txt'
with open(filename, 'w') as f:
    f.write(' '.join(word))

print("Random word written to", filename)