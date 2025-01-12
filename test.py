import verifier

def test_verify():
    # Test with a valid email and token
    if verifier.verify('email@example.com', 'VALID_API_TOKEN'):
        print("Test passed: Valid email and token")
    else:
        print("Test failed: Valid email and token")

    # Test with an invalid email
    if not verifier.verify('invalid_email@example.com', 'VALID_API_TOKEN'):
        print("Test passed: Invalid email")
    else:
        print("Test failed: Invalid email")

    # Test with an invalid token
    if not verifier.verify('email@example.com', 'INVALID_API_TOKEN'):
        print("Test passed: Invalid token")
    else:
        print("Test failed: Invalid token")

def test_verifyRequest():
    # Test with a valid email and token
    response = verifier.verifyRequest('email@example.com', 'VALID_API_TOKEN')
    if response:
        print("Test passed: Valid email and token")
    else:
        print("Test failed: Valid email and token")

    # Test with an invalid email
    response = verifier.verifyRequest('invalid_email@example.com', 'VALID_API_TOKEN')
    if response is None:
        print("Test passed: Invalid email")
    else:
        print("Test failed: Invalid email")

    # Test with an invalid token
    response = verifier.verifyRequest('email@example.com', 'INVALID_API_TOKEN')
    if response is None:
        print("Test passed: Invalid token")
    else:
        print("Test failed: Invalid token")

if __name__ == "__main__":
    test_verify()
    test_verifyRequest()
