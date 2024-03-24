def write_to_file(file_name):
    try:
        with open(file_name, 'w') as file:
            file.write("This is line 1.\n")
            file.write("12345\n")
            file.write("Another line here.\n")
        print("File created and written successfully!")
    except FileNotFoundError:
        print("File not found or path is incorrect.")
    except PermissionError:
        print("Permission denied to create/write to the file.")
    finally:
        print("File creation process completed.")


def read_and_display(file_name):
    try:
        with open(file_name, 'r') as file:
            print("Contents of the file:")
            print(file.read())
    except FileNotFoundError:
        print("File not found or path is incorrect.")
    except PermissionError:
        print("Permission denied to read the file.")
    finally:
        print("File reading process completed.")


def append_to_file(file_name):
    try:
        with open(file_name, 'a') as file:
            file.write("Line appended 1.\n")
            file.write("67890\n")
            file.write("Yet another line appended.\n")
        print("File appended successfully!")
    except FileNotFoundError:
        print("File not found or path is incorrect.")
    except PermissionError:
        print("Permission denied to append to the file.")
    finally:
        print("File appending process completed.")


# File creation
write_to_file("my_file.txt")

# File reading and display
read_and_display("my_file.txt")

# File appending
append_to_file("my_file.txt")
