def count_words(text):
    """
    Count the number of words in the input text.
    :param text: str
    :return: int - number of words
    """
    words = text.split()  # Split text into words using whitespace
    return len(words)

def main():
    print("Welcome to the Word Counter Program!")
    
    # Prompt user input
    user_input = input("Please enter a sentence or paragraph: ").strip()
    
    # Error Handling: Check if input is empty
    if not user_input:
        print("Error: No input provided. Please enter some text.")
        return
    
    # Count words
    word_count = count_words(user_input)
    
    # Output Display
    print(f"\nWord Count: {word_count}")

# Run the main function
if __name__ == "__main__":
    main()
