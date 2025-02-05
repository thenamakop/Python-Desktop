import random

# Define lists of words for each category
nouns = ["dog", "cat", "tree", "house"]
verbs = ["run", "jump", "swim", "fly"]
adjectives = ["big", "small", "green", "red"]

# Prompt the user to enter the number of Mad Libs to generate
num_mad_libs = int(input("Enter the number of Mad Libs to generate: "))

for _ in range(num_mad_libs):
    # Randomly select a word from each category
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    adjective = random.choice(adjectives)

    # Create a Mad Lib template
    mad_lib = f"Once upon a time, in a {adjective} land, there lived a {noun}. The {noun} was known for its {adjective} {noun} that could {verb} anything. One day, the {noun} decided to {verb} the {adjective} {noun}."

    # Print the completed Mad Lib
    print(mad_lib)