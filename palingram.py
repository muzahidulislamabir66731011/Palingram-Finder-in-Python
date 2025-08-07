def load_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            words = {line.strip() for line in f if line.strip()}
        return words
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return set()
    except Exception as e:
        print(f"An error occurred: {e}")
        return set()


def find_palindromic_pairs(word_set: set) -> set:
    word_list = list(word_set)
    palindromic_pairs = set()

    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            word1 = word_list[i]
            word2 = word_list[j]
            combined = word1 + word2
            left, right = 0, len(combined) - 1
            is_pal = True
            while left < right:
                if combined[left] != combined[right]:
                    is_pal = False
                    break
                left += 1
                right -= 1
            if is_pal:
                palindromic_pairs.add((word1, word2))

    return palindromic_pairs


def main():
    filename = input("Enter the word list filename (e.g., proto.txt): ").strip()
    words = load_words(filename)

    if not words:
        print("No words loaded. Exiting.")
        return
    
    palindromes = find_palindromic_pairs(words)
    while True:
        format_choice = input("Enter 1 (words), 2 (combined palindromes), or 3 (both): ").strip()
        if format_choice in {"1", "2", "3"}:
            break
        print("Invalid choice. Please enter 1, 2, or 3.")

    combined_list = [w1 + w2 for w1, w2 in sorted(palindromes)]

    unique_words = set()
    for w1, w2 in palindromes:
        unique_words.add(w1)
        unique_words.add(w2)
    unique_words = sorted(unique_words)

    if format_choice == "1":
        for w in unique_words:
            print(w)
    elif format_choice == "2":
        for combined in combined_list:
            print(combined)
    elif format_choice == "3":
        for combined in combined_list:
            print(combined)
        print("\nBelow are the palindrome words:\n")
        for w in unique_words:
            print(w)

    save_choice = input("\nDo you want to save the palindromic words to a text file? (yes/no): ").strip().lower()
    if save_choice == "yes":
        filename = input("Enter the filename (e.g., palindromes.txt): ").strip()
        with open(filename, 'w', encoding='utf-8') as f:
            if format_choice == "1":
                for w in unique_words:
                    f.write(w + "\n")
            elif format_choice == "2":
                for combined in combined_list:
                    f.write(combined + "\n")
            elif format_choice == "3":
                for combined in combined_list:
                    f.write(combined + "\n")
                f.write("\nBelow are the palindrome words:\n\n")
                for w in unique_words:
                    f.write(w + "\n")
        print(f"\nSaved palindromic words to '{filename}'")
    else:
        print("\nNot saved.")

if __name__ == "__main__":
    main()
