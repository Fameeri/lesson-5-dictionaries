# Copy this into your Python file

# Student Library Management System
print("=== STUDENT LIBRARY MANAGEMENT SYSTEM ===")

# Starting data structure
students = {
    "student001": {
        "name": "Alice", 
        "grade": 10,
        "subjects": {"math", "science", "english"},
        "seat": (2, 3)  # row, column tuple
    },
    "student002": {
        "name": "Bob",
        "grade": 10, 
        "subjects": {"math", "history", "art"},
        "seat": (1, 2)
    }
}

print("Initial student data:")
for student_id, data in students.items():
    print(f"{student_id}: {data}")

# Task 1: Add a new student
print(f"\n=== Task 1: Adding New Student ===")
students[f"student003"] = {
    "name": "Charlie", "grade": 11, "subjects": {"science", "english", "history"}, "seat": (2,1)
}

print("student003 added:", students["student003"])


# Task 2: Find all unique subjects being taught
print(f"\n=== Task 2: All Subjects ===")
all_subjects = set()
for student in students.value():
    all_subjects.update(student["subjects"])
print(f"All subjects taught: {all_subjects}")

# Task 3: Find students taking both math and science
print(f"\n=== Task 3: Math AND Science Students ===")
math_and_science_students = []
for student_id, student in students.items():
    if "math" in student["subjects"] and "science" in students["subjects"]:
        math_and_science_students.append(student["name"])
print(f"Students taking both math and science: {math_and_science_students}")

# Task 4: Calculate average grade
print(f"\n=== Task 4: Average Grade ===")
total_grade = 0
student_count = 0
for student in students.values():
    total_grade += student["grade"]
    student_count += 1
average_grade = total_grade / student_count
print(f"Average grade: {average_grade:.1f}")

# Task 5: Find students in the same row
print(f"\n=== Task 5: Students in Same Row ===")
rows = {}
for student_id, student in students.items():
    row = student["seat"][0]
    if row not in rows:
        rows[row] = []
    rows[row].append(student["name"])
for row, names in rows.items():
    
# Group students by row number (first part of seat tuple)
# Your code here
# Print which students share rows

# Bonus Task 6: Subject popularity analysis
print(f"\n=== Bonus: Subject Popularity ===")
# Count how many students take each subject
subject_count = {}
# Your code here
# Print subjects ordered by popularity

# Bonus Task 7: Seating chart
print(f"\n=== Bonus: Seating Chart ===")
# Create a visual representation of where students sit
# Your code here
# Show a simple grid with student names in their positions

# Challenge: Add functionality to:
# - Move a student to a new seat
# - Find available seats
# - Add/remove subjects for a student
# - Find study group recommendations (students with common subjects)