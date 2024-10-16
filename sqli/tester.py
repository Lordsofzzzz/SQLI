import requests

def test_sqli(url, param, payload_file):
    try:
        # Open the payload file and read each line
        with open(payload_file, 'r') as file:
            payloads = file.readlines()
        
        for payload in payloads:
            # Strip any leading/trailing whitespace from the payload
            payload = payload.strip()
            
            # Construct the URL with the payload
            test_url = f"{url}?{param}={payload}"
            
            # Send the request
            response = requests.get(test_url)
            
            # Check if the response indicates a potential SQLi vulnerability
            if "error" not in response.text.lower() and "syntax" not in response.text.lower():
                print(f"Potential SQL Injection vulnerability found at {test_url}")
            else:
                print(f"No vulnerability found at {test_url}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except FileNotFoundError:
        print(f"Payload file '{payload_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


test_sqli('http://example.com/page', 'param', 'payloads.txt')