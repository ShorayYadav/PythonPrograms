import os

# Specify the directory path
directory = '/'

try:
    # Get the list of files and directories
    contents = os.listdir(directory)

    print("\nContents of the directory:")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("Error: Directory not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print("An error occurred:", e)