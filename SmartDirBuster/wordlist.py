import os
WORDLIST_PATH = os.path.join("wordlists", "big.txt")
def load_wordlist():
    """
    Reads the wordlist file and returns
    all valid directory names as a list.
    """
    directories = []
    try:
        with open(WORDLIST_PATH, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                # Ignore blank lines
                if line:
                    directories.append(line)

        print(f"[+] Loaded {len(directories)} directories from wordlist.")
    except FileNotFoundError:
        print(f"[ERROR] Wordlist not found: {WORDLIST_PATH}")
        return []
    except Exception as e:
        print(f"[ERROR] {e}")
        return []
    return directories