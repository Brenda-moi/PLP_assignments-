# Ask the user for the filename
filename = input("Enter the name of the file to read: ")

try:
    # Try to open and read the file
    with open(filename, 'r') as file:
        content = file.read()

    # Modify the content (e.g., make it uppercase)
    modified_content = content.upper()

    # Write the modified content to a new file
    new_filename = "modified_" + filename
    with open(new_filename, 'w') as new_file:
        new_file.write(modified_content)

    print(f"✅ Modified content written to '{new_filename}'.")

except FileNotFoundError:
    print("❌ Error: The file was not found.")
except IOError:
    print("❌ Error: Unable to read or write the file.")
