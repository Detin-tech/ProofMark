#!/bin/bash

echo ""
echo "🕵️  Stego Utility: Proof-of-Clone Chain-of-Custody Tool"
echo "--------------------------------------------------------"
echo "1) Embed Stego Fingerprint (tag files)"
echo "2) Detect Stego Fingerprint (scan files)"
read -rp "Select option [1-2]: " choice

case "$choice" in
  1)
    python3 main.py
    ;;
  2)
    python3 stegodetect.py
    ;;
  *)
    echo "❌ Invalid selection. Exiting."
    exit 1
    ;;
esac

