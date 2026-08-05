TIMEOUT = 5
THREADS = 10
USER_AGENT = "SmartDirBuster/1.0"
WORDLIST_PATH = "wordlists/common.txt"
REPORT_FOLDER = "reports"
REPORT_FILE = "scan_report.csv"
VALID_STATUS_CODES = [
    200,
    204,
    301,
    302,
    307,
    308,
    401,
    403
]
SHOW_404 = False
ALLOW_REDIRECTS = False
VERIFY_SSL = True
HTTP_METHOD = "GET"