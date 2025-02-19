import string


def count_character_frequency(text):
    """
    Takes a string and returns a dictionary with the frequency of each character.
    Only alphabetic characters are included, and they are case-insensitive.
    """
    char_count = {}  # Dictionary to store alphabetic character frequency
    for char in text.lower():  # Convert all characters to lowercase
        if char in string.ascii_lowercase:  # Only count alphabetic characters
            if char in char_count:
                char_count[char] += 1  # Increment the count
            else:
                char_count[char] = 1  # Initialize the count
    return char_count


def generate_report(word_count, char_frequency):
    """
    Creates a formatted report based on the word count and character data.
    Each character is wrapped in single quotes.
    """
    report = []
    report.append(f"Word Count: {word_count}")
    report.append("Character Counts (Alphabet Only):")

    # Sort characters alphabetically for a clean display
    for char, count in sorted(char_frequency.items()):
        report.append(f"    '{char}': {count}")

    return "\n".join(report)


def main():
    # Open the book and read its content
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        # Count the total number of words
        words = file_contents.split()
        word_count = len(words)

        # Count the frequency of alphabetic characters
        char_frequency = count_character_frequency(file_contents)

        # Generate and print the report
        report = generate_report(word_count, char_frequency)
        print(report)


# Entry point for the script
if __name__ == "__main__":
    main()
