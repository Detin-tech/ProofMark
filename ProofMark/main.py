#!/usr/bin/env python3
import os
import shutil
import readline

SUPPORTED_EXTS = {'.txt', '.md', '.py', '.sh', '.html', '.js', '.json', '.yaml', '.yml'}
CODE_EXTS = {'.py', '.sh', '.js', '.json', '.yaml', '.yml', '.html'}
ZWSP = '\u200b'

def insert_stego(content, stego_tag, mode='zwsp', interval=10, ext=None):
    lines = content.splitlines()
    out = []
    for i, line in enumerate(lines):
        if i % interval == 0:
            insertion_mode = mode
            if mode == 'zwsp' and ext in CODE_EXTS:
                insertion_mode = 'comment'
            if insertion_mode == 'zwsp':
                line += ZWSP + stego_tag
            elif insertion_mode == 'comment':
                stripped = line.strip()
                if stripped.startswith('#'):
                    line += f"  # {stego_tag}"
                elif stripped.startswith('//'):
                    line += f"  // {stego_tag}"
                elif '<!--' in line or '-->' in line:
                    line += f" <!-- {stego_tag} -->"
                else:
                    line += f"  # {stego_tag}"
        out.append(line)
    return '\n'.join(out)

def stego_dir(input_dir, output_dir, stego_tag, mode='zwsp', interval=10):
    for root, _, files in os.walk(input_dir):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext.lower() in SUPPORTED_EXTS:
                in_path = os.path.join(root, file)
                rel_path = os.path.relpath(in_path, input_dir)
                out_path = os.path.join(output_dir, rel_path)
                os.makedirs(os.path.dirname(out_path), exist_ok=True)

                with open(in_path, 'r', errors='ignore') as f:
                    content = f.read()

                new_content = insert_stego(content, stego_tag, mode, interval, ext.lower())
                with open(out_path, 'w') as f:
                    f.write(new_content)

def main():
    input_dir = input("📂 Enter path to input folder: ").strip()
    fingerprint = input("🧬 Enter your fingerprint or ID (e.g. DocGrabber:Ben2025): ").strip()
    stego_tag = f":::stegofp,{fingerprint},build01:::"

    print("\n🔧 Select stego mode:")
    print("  1) Zero-width (invisible)")
    print("  2) Comment-based (visible in code)")
    mode_map = {'1': 'zwsp', '2': 'comment'}
    mode_choice = input("Enter choice [1]: ").strip()
    mode = mode_map.get(mode_choice, 'zwsp')

    interval = input("🔁 Line interval for insertion [default: 10]: ").strip()
    interval = int(interval) if interval.isdigit() else 10

    output_dir = input_dir.rstrip("/\\") + "_stego"
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    print(f"\n🛠️ Processing files with tag: {stego_tag}")
    stego_dir(input_dir, output_dir, stego_tag, mode, interval)
    print(f"✅ Stego complete. Output written to: {output_dir}")

if __name__ == "__main__":
    main()

