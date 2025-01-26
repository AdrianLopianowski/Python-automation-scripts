from PyPDF2 import PdfReader, PdfWriter

def process_single_pages(input_text):
    """Processes input for single pages into a list."""
    if not input_text.strip():
        return []
    return [int(page.strip()) - 1 for page in input_text.split(",") if page.strip().isdigit()]

def process_ranges(input_text):
    """Processes input for page ranges into a list."""
    if not input_text.strip():
        return []
    ranges = input_text.split(",")
    pages = []
    for r in ranges:
        if "-" in r:
            try:
                start, end = map(int, r.split("-"))
                pages.extend(range(start - 1, end)) 
            except ValueError:
                print(f"Invalid range: {r}")
        else:
            print(f"Invalid range: {r}")
    return pages

def main():
    # Load the input PDF
    input_file = input("Enter the name of the input PDF file (e.g., input.pdf): ").strip()
    output_file = input("Enter the name of the output PDF file (e.g., output.pdf): ").strip()

    try:
        reader = PdfReader(input_file)
    except FileNotFoundError:
        print("The PDF file was not found. Please make sure the name is correct.")
        return
    except Exception as e:
        print(f"An error occurred while opening the file: {e}")
        return

    print(f"The PDF file contains {len(reader.pages)} pages.")
    
    # Get single pages
    single_pages = input("Enter single page numbers (e.g., 1, 5, 8): ").strip()
    selected_single_pages = process_single_pages(single_pages)

    # Get page ranges
    ranges = input("Enter page ranges (e.g., 27-36, 51-82): ").strip()
    selected_ranges = process_ranges(ranges)

    # Combine all selected pages
    selected_pages = sorted(set(selected_single_pages + selected_ranges))
    print(f"Selected pages: {[page + 1 for page in selected_pages]}")  

    if not selected_pages:
        print("No pages were selected. Exiting.")
        return

    # Create the new PDF file
    writer = PdfWriter()
    try:
        for page_num in selected_pages:
            if 0 <= page_num < len(reader.pages):
                writer.add_page(reader.pages[page_num])
            else:
                print(f"Warning: Page {page_num + 1} is out of range.")

        with open(output_file, "wb") as output_pdf:
            writer.write(output_pdf)

        print(f"The new PDF file has been saved as: {output_file}")

    except Exception as e:
        print(f"An error occurred while creating the PDF file: {e}")

if __name__ == "__main__":
    main()
