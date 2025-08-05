empty_dict = {}
contacts = {
    "Alice": "555-0123", "Bob": "555-1234", "Charlie": "555-1235"
}

user = dict(name="Alice", age=25, city="New York")
from_list = dict([("a", 1), ("b", 2)])

print(contacts)
print(user)
print(from_list)

print(contacts["Alice"])

print(contacts.get("Alice"))
print(contacts.get("Dave"))
print(contacts.get("Dave", "Not found"))

print(contacts.keys())
print(contacts.values())
print(contacts.items())

print("\nMethod 1 - keys only:")
for name in contacts:
    print(f"{name}: {contacts[name]}")
    
print("\nMethod 2 - values only:")
for phone in contacts.value():
    print(f"phone number: {phone}")
    
print("\nMethod 3 - loop over key_value pairs")
for name, phone in contacts.items():
    print(f"{name}'s phone: {phone}")
    
print("\nMethod 4: with numbering")
for i, (name, phone) in enumerate(contacts.items(), 1):
    print(f"{i}. {name}: {phone}")
    
grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
students = ["Alice", "Bob", "Charlie", "David", "Eve"]

print("\nUsing .get() and defaults in loops")
for student in students:
    grade = grades.get(student, "No grade recorded")
    print(f"{student}: {grade}")
    
print("\nUsainf .setfault() to add missing entries:")
for student in students:
    grade = grades.setdefault(student, 0)
    print(f"{student}: {grade}")
print(f"Updated grades: {grades}")

contacts["David"] = "555-0126"
contacts["Alice"] = 555-9999
contacts["Bob"] = 555-8475
del contacts["Bob"]
popped = contacts.pop("Carlie", "Not Found")
print(popped)

contacts = {
    "Alice": {"phone": "555-0123", "email": "aliece@example.com", "address": {
        "street": "123 Main St", "city": "pythin city", "zip": "12345"
    }
}, "Bob": {
    "phone": "555-1234", "email": "bob@example.com", "address": {
        "street": "123 Couth St", "city": "python town", "zip": "12354"
    }
}
}

print(contacts["alice"]["phone"])
print(contacts["Alice"]["address"]["city"])

alice_info = contacts.get("Alice",{})
alice_phone = alice_info.get("phone", "No phone number")
alice_city = contacts.get("Alice", {}).get("address", {}).get("city", "No city")

print(alice_city)

contacts["Alice"]["address"]["country"] = "USA"
contacts["emergency_contact"] = {"name": "Mom", "phone": "555-1111"}

contacts["Bob"]