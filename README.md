# 🗄️ File Organizer (Automation Tool)

This File Organizer Tool is designed to pick up loose files within a folder and distribute them through folders based on
their type.

## ✨ Features
- Organizes files based on their extensions
- Categorizes by Documents, Images, Video and Sound
- Uncategorized files are moved into the `Others` folder
- Ignore hidden files such as `.DS_Store`
- Automatically handles duplicate names using versioning
- Creates only the folders that are needed
- Allows the user to choose which folder to organize
- Provides a summary of what was done

## 🛠️ Technologies
- Python
- pathlib — used for filesystem navigation and file operations

## 📋 How it works
The application follows these steps:

1. The user provides the path of the folder they want to organize.
2. The application validates that the provided path is a valid directory.
3. Files are identified and hidden files are ignored.
4. Each file is assigned to a category based on its extension.
5. The required category folders are created.
6. Duplicate filenames are automatically renamed using version numbers.
7. Files are moved to their corresponding folders.
8. A summary of the operation is displayed in the terminal.

## 📁 Supported Categories
| Category  | Extensions                        |
| --------- | --------------------------------- |
| Documents | `.docx`, `.txt`, `.pdf`           |
| Images    | `.jpg`, `.jpeg`, `.png`, `.gif`   |
| Audio     | `.mp3`, `.wav`                    |
| Video     | `.mp4`, `.mov`                    |
| Others    | Unsupported or unknown extensions |

## 🚀 Getting Started

### Prerequisites

Make sure Python 3 is installed on your system.

### Installation

Clone the repository:

```bash
git clone https://github.com/zegostinho/Auto_File_Organizer_Python
cd file-organizer
```

No additional dependencies are required.

### Usage

Run the application:

```bash
python main.py
```

The application will ask you to provide the path of the folder you want to organize:

```text
Which folder do you wish to organize? Type the folder path
> /Users/yourname/Downloads
```

After the organization is complete, a summary will be displayed:

```text
Organizing files...

✅ 3 files moved to Documents
✅ 2 files moved to Images
✅ 1 file moved to Others

Done! 6 files organized.
```

## 🔢 Duplicate File Handling

When a file with the same name already exists in the destination folder, the application does not overwrite it.

Instead, it automatically creates a versioned filename:

```text
report.pdf
report_v02.pdf
report_v03.pdf
report_v04.pdf
```

This ensures that existing files are preserved.

## 📁 Project Structure

```text
file-organizer/
│
├── main.py
├── README.md
└── .gitignore
```

## 🔮 Future Improvements

Possible future improvements include:

* Add error handling for file operation failures
* Allow users to customize file categories
* Support additional file types
* Add a graphical user interface
* Add logging for organization operations

## 🎯 Purpose

This project was created as a practical Python automation project, focusing on filesystem manipulation, reusable functions, input validation, and handling real-world file organization scenarios.

It was also an opportunity to apply Python concepts to a practical problem rather than simply solving isolated programming exercises.

## 📄 License

This project is for educational and portfolio purposes.
