from pathlib import Path

category = {
    "Documents": [".docx", ".txt", ".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Audio": [".mp3", ".wav"],
    "Video": [".mp4", ".mov"]
}


def find_destination(file, file_category, dir_path):
    destination_cat = dir_path / "Others"

    for cat, ext in file_category.items():
        if file.suffix in ext:
            destination_cat = dir_path / cat
            break
    return destination_cat

def resolve_folder_conflicts(files, destinations):
    renamed_files = {}
    for d in set(destinations.values()):
        for f in files:
            if f.stem == d.name:
                old_path = f.parent / f.name
                new_path = f.parent / (f.stem + "_file" + f.suffix)
                f.rename(new_path)
                renamed_files[old_path] = new_path

    return renamed_files


def create_folders(folder_destinations):
    for d in set(folder_destinations.values()):
        d.mkdir(exist_ok=True)


def get_unique_name(file, destination_folder):
    if (destination_folder / file.name).exists():

        version = 2

        while True:
            version_exists = False
            version_name = f"{file.stem}_v{version:02d}"

            for existing_file in destination_folder.iterdir():
                if existing_file.stem.startswith(version_name):
                    version_exists = True
                    break

            if not version_exists:
                new_name = version_name + file.suffix
                break

            version += 1
        return new_name
    else:
        return file.name


def organize_files(folder_path, categories):
    files = [file for file in folder_path.iterdir() if file.is_file() and not file.name.startswith(".")]
    total_files = len(files)

    # Verify each file's category
    destinations = {}
    file_counts = {}
    for file in files:
        destination = find_destination(file, categories, folder_path)
        destinations[file] = destination

        if destination.name not in file_counts:
            file_counts[destination.name] = 0
        file_counts[destination.name] += 1

    # Resolve name conflicts for folder creation
    renamed_files = resolve_folder_conflicts(files, destinations)
    for i, file in enumerate(files):
        if file in renamed_files:
            files[i] = renamed_files[file]

    for old_path, new_path in renamed_files.items():
        destination = destinations.pop(old_path)
        destinations[new_path] = destination


    # Create the necessary folders
    create_folders(destinations)


    # Move files to the right folder
    for file in files:
        destination = destinations[file]

        # Rename files with the same name
        new_file_name = get_unique_name(file, destination)
        if new_file_name == file.name:
            file.move_into(destination)
        else:
            file.rename(destination / new_file_name)

    return total_files, file_counts

path = Path(input("Which folder do you wish to organize? Type the folder path:\n> "))

while not path.is_dir():
    print("That folder doesn't exist. Please type a valid folder path.")
    path = Path(input("Which folder do you wish to organize? Type the folder path\n> "))


print("Organizing files...\n")
organized_files, num_files = organize_files(path, category)

for key, value in num_files.items():
    if value == 1:
        print(f"✅ {value} file moved to {key}")
    else:
        print(f"✅ {value} files moved to {key}")

print(f"\nDone! {organized_files} files organized.")
