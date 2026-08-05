import csv
import os
REPORT_FOLDER = "reports"
REPORT_FILE = "scan_report.csv"
def save_report(results):
    """
    Saves scan results into a CSV file.
    """
    os.makedirs(REPORT_FOLDER, exist_ok=True)
    report_path = os.path.join(REPORT_FOLDER, REPORT_FILE)
    try:
        with open(report_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["URL", "Status Code"])
            for result in results:
                writer.writerow([
                    result["url"],
                    result["status"]
                ])
        print(f"\n[+] Report saved successfully!")
        print(f"[+] Location: {report_path}")
    except Exception as e:
        print(f"[ERROR] Failed to save report: {e}")