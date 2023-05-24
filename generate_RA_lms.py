'''
Result Analysis Generation Code for CULMS
University: Chitkara 
Add the file and relevant column number in which there are marks 
Note: 0-39 also outputs the absent students, delete them manually.
Developer: Puneet Bawa
'''
import csv

total_marks=40 #change the total marks

def count_students(csv_file, column_index):
    # Dictionary to store the count for each percentage range
    count = {
        "0-39": 0,
        "40-49": 0,
        "50-59": 0,
        "60-69": 0,
        "70-79": 0,
        "80-89": 0,
        "90-100": 0
    }

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row

        for row in reader:
            percentage = (int(row[column_index])/total_marks)*100

            if percentage >= 0 and percentage <= 39:
                count["0-39"] += 1
            elif percentage >= 40 and percentage <= 49:
                count["40-49"] += 1
            elif percentage >= 50 and percentage <= 59:
                count["50-59"] += 1
            elif percentage >= 60 and percentage <= 69:
                count["60-69"] += 1
            elif percentage >= 70 and percentage <= 79:
                count["70-79"] += 1
            elif percentage >= 80 and percentage <= 89:
                count["80-89"] += 1
            elif percentage >= 90 and percentage <= 100:
                count["90-100"] += 1

    return count

# Example usage
csv_file = '/kaggle/input/grades/Core JAVA_GradesExport_2023-05-24-05-55.csv'  # Replace with your CSV file path
column_index = 1  # Replace with the column index containing the percentages

result = count_students(csv_file, column_index)
for key, value in result.items():
    print(f"{key}: {value} students")
