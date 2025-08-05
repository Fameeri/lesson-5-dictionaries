# Copy this into your Python file

# === Scenario 1: Social Network Analysis ===
print("=== SOCIAL NETWORK ANALYSIS ===")

# Given: Friend lists for Alice and Bob
alice_friends = {"Bob", "Charlie", "David", "Eve"}
bob_friends = {"Alice", "Charlie", "Frank", "Grace"}

print(f"Alice's friends: {alice_friends}")
print(f"Bob's friends: {bob_friends}")

# Task 1: Find mutual friends between Alice and Bob
mutual_friends = # Your code here
print(f"Mutual friends: {mutual_friends}")

# Task 2: Find friend suggestions for Alice (Bob's friends who aren't Alice's friends, excluding Alice herself)
suggestions_for_alice = # Your code here
print(f"Friend suggestions for Alice: {suggestions_for_alice}")

# Task 3: Calculate the total size of their combined social network (including Alice and Bob)
total_network = # Your code here
total_network_size = len(total_network)
print(f"Total network size: {total_network_size}")

# Task 4: Find people who are friends with exactly one of them
exclusive_friends = # Your code here
print(f"Exclusive friends: {exclusive_friends}")

print("\n" + "="*50)

# === Scenario 2: Inventory Management ===
print("=== INVENTORY MANAGEMENT ===")

# Given: Store inventory data
in_stock = {"laptop", "mouse", "keyboard", "monitor", "speakers"}
on_order = {"laptop", "webcam", "headphones", "monitor"}
back_ordered = {"tablet", "smartphone", "laptop"}

print(f"In stock: {in_stock}")
print(f"On order: {on_order}")
print(f"Back ordered: {back_ordered}")

# Task 1: Find items that will be available soon (in stock OR on order)
available_soon = # Your code here
print(f"Available soon: {available_soon}")

# Task 2: Find potentially overstocked items (in stock AND on order)
overstocked = # Your code here
print(f"Potentially overstocked: {overstocked}")

# Task 3: Find items that need to be ordered urgently (back-ordered but NOT on order)
need_to_order = # Your code here
print(f"Need to order urgently: {need_to_order}")

# Task 4: Find items that are completely unavailable (back-ordered but NOT in stock)
unavailable = # Your code here
print(f"Completely unavailable: {unavailable}")

# Bonus: Create a priority ordering list based on back-ordered items
print(f"\n=== PRIORITY ANALYSIS ===")
# Which back-ordered items should we prioritize? (Hint: consider what's not on order)