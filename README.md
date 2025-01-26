# Automation Scripts Collection

This repository contains a collection of Python scripts designed to automate various tasks. Each script is self-contained and focuses on a specific task, making it easy to use or adapt for different purposes.

## Scripts Included

### 1. `pdf_page_extractor.py`
- **Purpose:** Extracts specific pages or ranges of pages from a PDF based on user input and generates a new PDF containing the selected pages.
- **Use Case:** Quickly isolate important sections of a large PDF document.
- **Highlights:**
  - Supports single pages (e.g., `1, 3, 5`) and page ranges (e.g., `10-15`).
  - Handles invalid inputs gracefully with warnings.
- **How to Run:**
  ```bash
  python pdf_page_extractor.py
  ```

### 2. `AutoFileSorter.py`
- **Purpose:** Automatically organizes files in the downloads folder into subdirectories based on file type.
- **Use Case:** Keep your downloads folder organized without manual sorting.
- **Highlights:**
  - Recognizes a wide range of file types, including documents, images, videos, audio, and code files.
  - Creates subdirectories dynamically if they don’t already exist.
- **How to Run:**
  ```bash
  python AutoFileSorter.py
  ```

### 3. `Backup_Script.py`
- **Purpose:** Creates a backup of a specified directory and stores it in a timestamped folder.
- **Use Case:** Regularly back up important files or folders to ensure data safety.
- **Highlights:**
  - Allows users to specify both the source directory and backup destination.
  - Uses timestamps for backup folder names to prevent overwriting.
- **How to Run:**
  ```bash
  python Backup_Script.py
  ```

### 4. `Job_offers.py`
- **Purpose:** Scrapes job listings from students.pl, compiles a list of internships, and sends new internship opportunities via email.
- **Use Case:** Stay updated on internship opportunities without manually checking the website.
- **Highlights:**
  - Stores job offers in a JSON file to track previously found listings.
  - Sends email notifications for new listings using SMTP.
- **Requirements:**
  - Install dependencies: `pip install requests beautifulsoup4 python-dotenv`
  - Configure environment variables in a `.env` file for email functionality.
- **How to Run:**
  ```bash
  python Job_offers.py
  ```

## Usage Instructions
1. Clone the repository to your local machine.
2. Navigate to the script you wish to use.
3. Run the script using Python and follow the prompts.

```bash
python script_name.py
```

## Contribution
Feel free to contribute by adding new scripts or improving the existing ones. Create a pull request or open an issue to suggest enhancements.
