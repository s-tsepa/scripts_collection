import os
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, error as ID3Error

def fix_encoding(text):
    """
    Fixes encoding issues in the given text by attempting to decode and re-encode it.
    """
    try:
        # Try to decode as Windows-1252 (common misencoding for UTF-8)
        fixed_text = text.encode('windows-1252').decode('utf-8')
        return fixed_text
    except (UnicodeEncodeError, UnicodeDecodeError):
        # If decoding fails, return the original text
        return text

def fix_mp3_tags(directory):
    """
    Recursively scans a directory for MP3 files and fixes encoding issues in their ID3 tags.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.mp3'):
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")

                try:
                    # Load the ID3 tags
                    audio = EasyID3(file_path)
                    tags_changed = False

                    # Fix encoding for each tag
                    for tag in audio:
                        original_value = audio[tag][0]
                        print(original_value)
                        fixed_value = fix_encoding(original_value)
                        print(fixed_value)
                        if fixed_value != original_value:
                            print(f"  Fixed encoding for tag '{tag}': {original_value} -> {fixed_value}")
                            audio[tag] = fixed_value
                            tags_changed = True

                    # Save the changes if any tags were fixed
                    if tags_changed:
                        audio.save()
                        print("  Tags updated.")
                    else:
                        print("  No encoding issues found.")

                except ID3Error as e:
                    print(f"  Error reading ID3 tags: {e}")
                except Exception as e:
                    print(f"  Unexpected error: {e}")

if __name__ == "__main__":
    # Specify the directory to scan
    directory = input("Enter the directory path to scan for MP3 files: ").strip()

    if os.path.isdir(directory):
        fix_mp3_tags(directory)
        print("Encoding fix process completed.")
    else:
        print("Invalid directory path.")
