# Program Name: Assignment5.py
# Course: IT3883/Section W02
# Student Name: Keyvon Thompson
# Assignment Number: Lab3
# Due Date: 04/11/2025
# Purpose: Demonstrates creation of a SQLite database, insertion of temperature data,
#          and calculation of average temperatures for Sunday and Thursday.
# List Specific resources used:
#   - Official Python documentation on sqlite3
#   - StackOverflow for syntax references

import sqlite3

def main():
    # 1. Create (or connect to) the SQLite database
    conn = sqlite3.connect('temperatures.db')
    cursor = conn.cursor()
    
    # 2. Create the table (if it doesn’t already exist)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Temperature_Readings (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Day_Of_Week TEXT,
            Temperature_Value REAL
        );
    ''')
    
    # 3. Read the input file and insert data into the table
    #    Assume the input file is named "temperature_data.txt"
    #    and each line is of the form: DayOfWeek,Temperature
    #    For example:
    #      Sunday 85.5
    #      Monday 78.2
    #      ...
    input_file = "Assignment5input.txt"
    with open(input_file, 'r') as file:    
        for line in file:
            line = line.strip()
            if not line:
                # Skip empty lines
                continue
        
            # Split by whitespace instead of by comma
            parts = line.split()
            if len(parts) < 2:
                print(f"Skipping line: {line} (not enough parts)")
                continue
        
            day = parts[0]         # e.g. "Friday"
            temp_str = parts[1]    # e.g. "83.4"
        
            # Convert temperature to float
            try:
                temperature = float(temp_str)
            except ValueError:
                print(f"Skipping line: {line} (couldn't parse float)")
                continue
        
            # Insert into the database
            cursor.execute('''
               INSERT INTO Temperature_Readings (Day_Of_Week, Temperature_Value)
                VALUES (?, ?)
            ''', (day, temperature))

    
    # Commit the inserts
    conn.commit()
    
    # 4. Execute the SQL commands to compute average temperature for Sunday and Thursday
    #    and print the results to the console.
    # Average for Sunday
    cursor.execute('''
        SELECT AVG(Temperature_Value) 
        FROM Temperature_Readings
        WHERE Day_Of_Week = 'Sunday'
    ''')
    avg_sunday = cursor.fetchone()[0]  # fetchone() returns a tuple, get the first element
    
    # Average for Thursday
    cursor.execute('''
        SELECT AVG(Temperature_Value) 
        FROM Temperature_Readings
        WHERE Day_Of_Week = 'Thursday'
    ''')
    avg_thursday = cursor.fetchone()[0]
    
    # Print out results
    print("Average temperature for Sunday:", avg_sunday if avg_sunday else "No data")
    print("Average temperature for Thursday:", avg_thursday if avg_thursday else "No data")
    
    # Close the database connection
    conn.close()


if __name__ == "__main__":
    main()
