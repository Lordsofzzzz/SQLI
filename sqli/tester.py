import subprocess

def test_sqli_with_sqlmap(url):
    try:
        # Ensure sqlmap is installed on your system (either in PATH or specify the path)
        sqlmap_path = "sqlmap"  # Change to full path if sqlmap is not in the system PATH

        # Call sqlmap with the constructed URL
        print(f"Testing {url} with sqlmap...")
        result = subprocess.run([sqlmap_path, "-u", url, "--batch", "--level=3", "--risk=3", "--technique=BEUSTQ"],
                                capture_output=True, text=True, timeout=60)

        # Enhance detection logic by checking for common SQLMap vulnerability output keywords
        result_output = result.stdout.lower()

        # Check for potential vulnerabilities by looking for specific keywords in the output
        if any(keyword in result_output for keyword in ["vulnerable", "available", "backdoor", "sqlmap has identified"]):
            print(f"Potential vulnerability detected at {url}")
        elif any(keyword in result_output for keyword in ["error", "unable", "connection failed", "timeout"]):
            print(f"sqlmap error occurred while testing {url}")
        else:
            print(f"sqlmap test completed for {url}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error during sqlmap execution: {e}")
    except subprocess.TimeoutExpired:
        print(f"sqlmap execution timed out while testing {url}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Usage example
test_sqli_with_sqlmap('http://example.com/page?param=value')
