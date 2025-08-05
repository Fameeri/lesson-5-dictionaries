# Dictionary Looping Practice
# Copy this into your Python file
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 96}

# Task 1: Loop through and print all student names
print("=== Student Names ===")
for name in student_scores.keys():
    print(name)
# Your code here

# Task 2: Loop through and print all scores
print("\n=== All Scores ===")
for score in student_scores.values():
    print(score)
# Your code here

# Task 3: Loop through and print "Name: Score" for each student
print("\n=== Name and Score ===")
for name, score in student_scores.items():
    print(f"{name}: {score}")
# Your code here

# Task 4: Use .get() to safely check scores for students who might not exist
students_to_check = ["Alice", "Bob", "Charlie", "David", "Eve"]
print("\n=== Safe Score Checking ===")
for student in students_to_check:
    print(f"{student}: {student_scores.get(student, 'No record found')}")
# Your code here - use .get() with a default message