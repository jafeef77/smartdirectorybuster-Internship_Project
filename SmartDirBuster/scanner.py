# ==========================================
# SmartDirBuster
# Scanner Module
# ==========================================

from concurrent.futures import ThreadPoolExecutor, as_completed

from wordlist import load_wordlist
from worker import scan_directory
from reporter import save_report
from config import THREADS, VALID_STATUS_CODES, SHOW_404


def start_scan(target_url):

    print("=" * 60)
    print("Scanner Started")
    print("=" * 60)

    # Load wordlist
    directories = load_wordlist()

    if not directories:
        print("[ERROR] No directories found in wordlist.")
        return

    print(f"\n[+] Loaded {len(directories)} directories")
    print(f"[+] Using {THREADS} Threads")
    print("\nStarting Scan...\n")

    results = []

    # Create Thread Pool
    with ThreadPoolExecutor(max_workers=THREADS) as executor:

        futures = {
            executor.submit(scan_directory, target_url, directory): directory
            for directory in directories
        }

        for future in as_completed(futures):

            result = future.result()

            status = result["status"]

            # Save every result
            results.append(result)

            # Display results
            if isinstance(status, int):

                if status == 404 and not SHOW_404:
                    continue

                if status in VALID_STATUS_CODES:
                    print(f"[{status}] {result['url']}")

            else:
                print(f"[{status}] {result['url']}")

    print("\nScan Completed!")

    print(f"Directories Tested : {len(directories)}")
    print(f"Results Saved      : {len(results)}")

    save_report(results)