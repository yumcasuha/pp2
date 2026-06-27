import shutil
import glob
import os

txt_files = glob.glob("*.txt")
os.makedirs("texts", exist_ok=True)

for file in txt_files:
    shutil.move(file, os.path.join("texts", file))
print("All .txt files moved to texts folder")

