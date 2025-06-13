#!/usr/bin/env python3
import os
import re

try:
    import readline
except ImportError:
    pass

STEGO_REGEX = re.compile(r":::stegofp,([^,]+),([^:]+):::")

def scan_file(path):
    matches = []
    try:
        with open(path, 'r', errors='ignore') as f:
            for lineno, line in enumerate(f, 1):
                found = STEGO_REGEX.search(line)
                if found:
                    fingerprint, tag = found.groups()
                    matches.append((lineno, fingerprint, tag, line.strip()))
    except Exception as e:
        print(f"❌ Error reading {path}: {e}")
    return matches

def scan_dir(target_dir):
    found_any = False
    for root, _, files in os.walk(target_dir):
        for file in files:
            path = os.path.join(root, file)
            matches = scan_file(path)
            if matches:
                found_any = True
                print(f"\n📁 {path}")
                for lineno, fingerprint, tag, line in matches:
                    print(f"  🕵️ Line {lineno}: Fingerprint = '{fingerprint}', Tag = '{tag}'")
                    print(f"     Content: {repr(line)}")
    if not found_any:
        print("\n🚫 No stego fingerprints found.")

def main():
    print("\n📂 What do you want to scan?")
    print("  1) A single file")
    print("  2) An entire folder")
    mode = input("Enter choice [1-2]: ").strip()

    if mode == "1":
        target = input("📄 Enter path to file: ").strip()
        matches = scan_file(target)
        if matches:
            print(f"\n📁 {target}")
            for lineno, fingerprint, tag, line in matches:
                print(f"  🕵️ Line {lineno}: Fingerprint = '{fingerprint}', Tag = '{tag}'")
                print(f"     Content: {repr(line)}")
        else:
            print("\n🚫 No stego fingerprints found.")
    elif mode == "2":
        target = input("📁 Enter path to folder: ").strip()
        print("\n🔍 Scanning folder for embedded stego tags...\n")
        scan_dir(target)
    else:
        print("❌ Invalid option.")

    print("\n✅ Scan complete.")

if __name__ == "__main__":
    main()
