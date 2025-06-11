🕵️ ProofMark​

A no-nonsense tool for developers and creators to embed invisible fingerprint tags into their files — and detect them later. Think chain of custody for your code and content.

🚀 Features
Embed hidden fingerprint IDs into code/docs (.md, .py, .txt, etc.)
Supports both invisible (zero-width) and visible (comment-based) modes
Detects stego tags across cloned/stolen repos or zip dumps
Fully offline, no dependencies, no telemetry
🔧 Usage
Step 1: Start
./start.sh​:::stegofp,PassMark:Ben2025,build01:::

----------------------------------------------------------------------

Embedding Format
The tool embeds the tag using this format:

:::stegofp,<YOUR-ID>,build01:::
Example:

// :::stegofp,DocGrabber:Ben2025,build01:::​:::stegofp,PassMark:Ben2025,build01:::
This tag can be invisible (\u200b) or placed in code comments.

🧬 Why Use This?
Because GitHub logs can be faked. Commits can be rewritten. But fingerprinted content travels.
If someone copies your repo and reposts it, you’ll know — and you’ll have proof.

⚠️ Disclaimer
This is a tool, not a license enforcer. It won’t sue people for you — but it’ll give you the evidence you need when they steal your shit.
