import requests

def check_https_headers(target):
    headers_to_check = ['Strict-Transport-Security', 'X-Content-Type-Options', 'Content-Security-Policy']
    try:
        response = requests.get(f"http://{target}", timeout=5)
        missing_headers = [header for header in headers_to_check if header not in response.headers]
        return missing_headers
    except Exception as e:
        return [f"Error checking headers: {str(e)}"]
