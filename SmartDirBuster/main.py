from scanner import start_scan
def banner():
    print("=" * 50)
    print("        SmartDirBuster v1.0")
    print("     Directory Enumeration Tool")
    print("=" * 50)
def get_target_url():
    while True:
        url = input("\nEnter Target URL (Example: http://localhost:8000): ").strip()

        if url.startswith("http://") or url.startswith("https://"):
            return url
        else:
            print("\n[!] Invalid URL")
            print("    URL must start with http:// or https://")
def main():
    banner()

    target_url = get_target_url()

    print("\nTarget URL :", target_url)

    print("\nStarting Scan...\n")

    start_scan(target_url)


if __name__ == "__main__":
    main()