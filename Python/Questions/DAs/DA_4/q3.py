def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def replace_word_single_occurrence(file_path, target_word, replacement):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            new_content = content.replace(target_word, replacement, 1)  # Replace only the first occurrence
        with open(file_path, 'w') as file:
            file.write(new_content)
        print(f"Successfully replaced the first occurrence of '{target_word}' with '{replacement}'.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

def replace_word_all_occurrences(file_path, target_word, replacement):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            new_content = content.replace(target_word, replacement)
        with open(file_path, 'w') as file:
            file.write(new_content)
        print(f"Successfully replaced all occurrences of '{target_word}' with '{replacement}'.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

# Example usage:
file_path = "example.txt"
total_words = count_words(file_path)
if total_words is not None:
    print(f"Total number of words in the file: {total_words}")

replace_word_single_occurrence(file_path, 'apple', 'orange')
replace_word_all_occurrences(file_path, 'banana', 'grape')
