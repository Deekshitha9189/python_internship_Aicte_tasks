import os

folder_path = input("Enter folder path: ")

files = os.listdir(folder_path)

count = 1

for file_name in files:

    file_extension = os.path.splitext(file_name)[1]

    new_name = f"file_{count}{file_extension}"

    old_file = os.path.join(folder_path, file_name)
    new_file = os.path.join(folder_path, new_name)

    os.rename(old_file, new_file)

    print(f"Renamed: {file_name} → {new_name}")

    count += 1

print("\n✅ All files renamed successfully!")