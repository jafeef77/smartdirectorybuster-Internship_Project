import requests
TIMEOUT = 5
HEADERS = {
    "User-Agent": "SmartDirBuster/1.0"
}
def scan_directory(target_url, directory):
    """
    Scans a single directory and returns
    the URL and HTTP status code.
    """
    target_url = target_url.rstrip("/")
    url = f"{target_url}/{directory}"
    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=TIMEOUT,
            allow_redirects=False
        )
        return {
            "url": url,
            "status": response.status_code
        }
    except requests.exceptions.Timeout:
        return {
            "url": url,
            "status": "TIMEOUT"
        }
    except requests.exceptions.ConnectionError:
        return {
            "url": url,
            "status": "CONNECTION ERROR"
        }
    except requests.exceptions.RequestException as e:
        return {
            "url": url,
            "status": f"ERROR: {e}"
        }