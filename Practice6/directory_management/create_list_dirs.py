import os

os.makedirs("nested/dir/example", exist_ok=True)

print("Current directory content:")
for item in os.listdir("."):
    print(item)

