import json
import os
import requests

# File paths
LINKS_FILE = "public/links.json"
OUTPUT_DIR = "public/pages"

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Function to fetch and save a webpage
def fetch_and_save_page(url, index):
    try:
        response = requests.get(url, timeout=10)  # Fetch the webpage
        response.raise_for_status()  # Raise an error for HTTP issues

        # Save the page content to a file
        filename = os.path.join(OUTPUT_DIR, f"page_{index}.html")
        with open(filename, "w", encoding="utf-8") as file:
            file.write(response.text)
        print(f"Saved: {url} -> {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {url}: {e}")

# Main script
def main():
    # Load links from links.json
    try:
        with open(LINKS_FILE, "r", encoding="utf-8") as file:
            links = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading links.json: {e}")
        return

    # Fetch and save each webpage
    for index, url in enumerate(links, start=1):
        fetch_and_save_page(url, index)

if __name__ == "__main__":
    main()
