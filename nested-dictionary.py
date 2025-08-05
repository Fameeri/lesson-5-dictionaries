# Nested Dictionary Building
# Copy this into your Python file

# Task 1: Build this inventory structure
inventory = {
    "electronics": {
        "laptop": {"price": 999, "stock": 5},
        "phone": {"price": 699, "stock": 12}
    },
    "books": {
        "python_guide": {"price": 49, "stock": 8}
    }
}

# Task 2: Access and print the laptop price
print("Laptop price:", inventory["electronics"]["laptop"]["price"])  # Fill in the access code

# Task 3: Update the phone stock to 10
inventory["electronics"]["phone"]["stock"] = 10
# Your code here

# Task 4: Add a new book: "web_development" with price 39 and stock 15
inventory["books"]["web-development"] = {"price": 39, "stock": 15}
# Your code here

# Task 5: Add a new category "clothing" with item "t_shirt" (price: 25, stock: 20)
inventory["clothing"] = {
    "t_chirt": {"price": 25, "stock": 20}
}
# Your code here

# Task 6: Print the entire updated inventory
print("\nFull inventory:")
print(inventory)
# Your code here (hint: you can just print the whole dictionary)

# Bonus: Calculate total value of all laptop inventory (price × stock)
laptop_value = inventory["electronics"]["laptop"]["price"] * inventory["electronics"]["laptop"]["stock"]
print("\nTotal value of laptop inventory:", laptop_value)
# Your code here