"""
This program reads in a file containing information about all of the 
students in the class, and contains several functions to help analyze
this data.
"""
def read_students(filename):
    """
    Reads in the students stored in the given filename.  Assumes that
    the data is stored, one line per student, where each line is:
    lastname,firstname,classyear.
    Inputs: filename (string)
    Returns: roster (list of lists containing all of the students)
    """
    students = []
    student_file = open("/Users/maxwellkumbong/Documents/CS21/Python /Projects/Find/students_file.csv", "r")
    for line in student_file:
        student = line.strip().split(",")
        student[2] = int(student[2])
        students.append(student)
    student_file.close()
    return students

def count_year(roster, year):
    """
    This function counts the number of students in the given roster
    with the given class year.
    Inputs: List of students (where each student is a list of last name,
            first name, and class year), year (int)
    Returns: count (int)
    """
    count = 0
    for student in roster:
        if student[2] == year:
            count = count + 1
    return count

def find_name(roster, search):
    """
    Print out all roster entries where the first name matches the search term.
    No return value. Only prints the matches

    Optional extensions:
    1. Allow partial matches (e.g. "Rich" matches "Richard")
    2. Allow case-insensitive matches (e.g. "richard" matches "Richard")
    3. Allow both partial and case-insenstive (e.g. "CHA" matches "Richard")
    """
    for student in roster:
        if search.lower() in student[1].lower():
            print("Matched: %s %s '%d" % (student[1], student[0], student[2]))


def main():
    roster = read_students("students.csv")
    print("Roster contains %d students" % (len(roster)))
    for year in range(2023, 2027):
        count = count_year(roster, year)
        print("There are %d students with class year %d" % (count, year))
    
    name = input("Enter a first name to search for: ")
    find_name(roster, name)

main()
