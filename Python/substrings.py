records = [
    "Vani Gupta, University of Hyderabad",
    "Elon Musk, Tesla",
    "Bill Gates, Microsoft",
    "Steve Jobs, Apple"
]

# Method 1
name = "Vani"
for record in records:
    if record.find(name) >= 0:
        print(record)

# Method 2
name = "Musk"
for record in records:
    if name in record:
        print(record)
