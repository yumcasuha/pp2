import shutil
import os

with open("sample.txt", "a", encoding="utf-8") as f:
    f.write("Third line\n")

shutil.copy("sample.txt", "backup_sample.txt")
print("File copied to backup_sample.txt")

if os.path.exists("backup_sample.txt"):
    os.remove("backup_sample.txt")
    print("File backup_sample.txt deleted")

