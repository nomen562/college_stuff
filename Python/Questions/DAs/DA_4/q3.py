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
word_to_be_replaced_s = input("Enter word to be replaced for single instance>")
replaced_word_s = input("Word to be replaced for that word>")
word_to_be_replaced_m = input("Enter word to be replaced for multiple instances>")
replaced_word_m = input("Word to be replaced for that word>")
file_path = "./college_stuff/Python/Questions/DAs/DA_4/example.txt"
total_words = count_words(file_path)
if total_words is not None:
    print(f"Total number of words in the file: {total_words}")

replace_word_single_occurrence(file_path, word_to_be_replaced_s, replaced_word_s)
replace_word_all_occurrences(file_path, word_to_be_replaced_m, replaced_word_m)
