def make_sentence(word, part_of_speech):
    """Generate a sentence based on the word and its part of speech."""
    if part_of_speech == 0:
        # Noun sentence template
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        # Verb sentence template
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        # Adjective sentence template
        print(f"Looking out my window, the sky is big and {word}!")

def main():
    # Ask the user for a word and part of speech type
    word = input("Please type a noun, verb, or adjective: ")
    part_of_speech = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
    
    # Call the make_sentence function with the user's input
    make_sentence(word, part_of_speech)

if __name__ == '__main__':
    main()
