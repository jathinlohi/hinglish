import os
import csv

folder_path = r"C:\Users\lenovo\Desktop\Projects\hinglish sentiment\datasets\conversations"  # Update this
output_csv = "extracted_dialogues.csv"

dialogues = []

# Iterate through all .txt files from 0.txt to 1599.txt
for i in range(1600):  # 0 to 1599
    filename = f"{i}.txt"
    file_path = os.path.join(folder_path, filename)

    if os.path.exists(file_path):  # Check if file exists
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                line = line.strip()
                if ":" in line:  # Check if line contains a dialogue
                    dialogues.append([line.split(":", 1)[1].strip()])  # Extract text after ':'

# Save to CSV
with open(output_csv, "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Dialogue"])
    writer.writerows(dialogues)

print(f"✅ Extraction complete. {len(dialogues)} dialogues saved to {output_csv}")
