import requests

# Define the login API endpoint
url = "https://lemonadepayments.com/api/login"  # Replace with the actual API endpoint

# Test data for valid and invalid credentials
valid_credentials = {
    "username": "sharon_user_valid",
    "password": "sharon_password_valid"
}

invalid_credentials = {
    "username": "sharon_user_invalid",
    "password": "sharon_password_invalid"
}

def test_login_api():
    print("Testing Login API...")

    # Test case 1: Valid credentials
    print("Test Case 1: Valid Credentials")
    response = requests.post(url, json=valid_credentials)
    if response.status_code == 200 and "token" in response.json():
        print("Test Passed: Valid credentials authenticated successfully.")
    else:
        print("Test Failed: Valid credentials were not authenticated.")
        print(f"Response Code: {response.status_code}, Response Body: {response.text}")

    # Test case 2: Invalid credentials
    print("\nTest Case 2: Invalid Credentials")
    response = requests.post(url, json=invalid_credentials)
    if response.status_code == 401:
        print("Test Passed: Invalid credentials correctly rejected.")
    else:
        print("Test Failed: Unexpected response for invalid credentials.")
        print(f"Response Code: {response.status_code}, Response Body: {response.text}")

# Execute the tests
if __name__ == "__main__":
    test_login_api()
