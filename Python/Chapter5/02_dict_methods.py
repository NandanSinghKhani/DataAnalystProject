marks = {
    "Ravi": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Ravi"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Ravi": 99, "Renuka": 100})
# print(marks)

print(marks.get("Ravi2")) # Prints None
print(marks["Ravi2"]) # Returns an error