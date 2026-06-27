names = ["Alina", "Ivan", "Sasha"]
scores = [95, 88, 76]

for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

value = "123"
print("Type:", type(value))
print("To int:", int(value))
print("To str:", str(456))

