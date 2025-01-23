# Program Name: Assignment1.py  (use the name the program is saved as)
# Course: IT3883/Section W02
# Student Name: Keyvon Thompson
# Assignment Number: Lab#1
# Due Date: 01/27/2025
# Purpose: This program implements a text-based menu that allows users to:
#          1) Append data to an input buffer
#          2) Clear the buffer
#          3) Display the buffer
#          4) Exit the program
#          The menu repeats until the user chooses to exit.
#
# List of resources used:
#  - Official Python documentation: https://docs.python.org/3/
#  - Class slides/notes from IT3883

def main():
    """
    This function runs a loop that continuously displays the menu
    until the user chooses to exit (option 4).
    """
    input_buffer = ""  # Will store user-entered data

    while True:
        # Display the menu options
        print("\n----- MAIN MENU -----")
        print("1) Append data to the input buffer")
        print("2) Clear the input buffer")
        print("3) Display the input buffer")
        print("4) Exit the program")

        choice = input("Enter your choice (1-4): ").strip()

        # Option 1: Append data
        if choice == "1":
            user_data = input("Enter the string you want to append: ")
            # If we already have data, add a space (or newline) before appending
            if input_buffer:
                input_buffer += " " + user_data
            else:
                input_buffer = user_data
            print("Data appended successfully.")

        # Option 2: Clear the input buffer
        elif choice == "2":
            input_buffer = ""  # Reset/clear the stored data
            print("Input buffer cleared.")

        # Option 3: Display the input buffer
        elif choice == "3":
            if input_buffer:
                print(f"\nCurrent input buffer: {input_buffer}")
            else:
                print("\nThe input buffer is currently empty.")

        # Option 4: Exit the program
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            # Handle any invalid menu choice
            print("Invalid choice! Please select 1, 2, 3, or 4.")

# This will ensure the main function is run when the script is executed directly.
if __name__ == "__main__":
    main()
