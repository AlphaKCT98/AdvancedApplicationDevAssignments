
# Program Name: Assignment3.py
# Course: IT3883/Section W02
# Student Name: Keyvon Thompson
# Assignment Number: Lab4
# Due Date: 03/22/2025
# Purpose: This program converts miles per gallon (mpg) to kilometers
#          per liter (km/l) via a console-based interface.
# Purpose: This program prompts the user for input, sends it over a TCP socket
#          to Program B, then receives and prints the uppercase string returned.
# List Specific resources used to complete the assignment:
#    - Python Socket documentation: https://docs.python.org/3/library/socket.html

import socket

def main():
    # Hard-coded IP and port; must match Program B
    host = '127.0.0.1'
    port = 45000

    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to Program B
        s.connect((host, port))
        
        # Prompt user for a string to send
        user_input = input("Enter a string to send to Program B: ")
        
        # Send that string over the socket (encode to bytes)
        s.sendall(user_input.encode('utf-8'))
        
        # Receive up to 1024 bytes back from Program B
        data = s.recv(1024)
        
        # Decode the data back to a string
        response = data.decode('utf-8')
        
        print("Program B responded with:", response)

if __name__ == "__main__":
    main()
