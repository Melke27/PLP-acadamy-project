def process_file():
    filename = input("Enter the filename to read from (e.g., input.txt): ")

    try:
        with open(filename, 'r') as infile:
            content = infile.read()
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
        return
    except IOError:
        print(f"❌ Error: The file '{filename}' could not be read.")
        return

    # Processing content
    upper_content = content.upper()
    word_count = len(content.split())

    try:
        with open('output.txt', 'w') as outfile:
            outfile.write(upper_content)
            outfile.write('\n\n')
            outfile.write(f"Word Count: {word_count}\n")
    except IOError:
        print("❌ Error: Could not write to 'output.txt'.")
        return

    print("✅ Success: 'output.txt' has been created with the modified content!")

if __name__ == '__main__':
    process_file()
