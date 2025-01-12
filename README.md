# Official Library for VerifyRight

## Installation

You can install the library using pip:

```bash
pip install git+https://github.com/email-verifier/verifier-py.git
```

Alternatively, you can clone the repository:

```bash
git clone https://github.com/email-verifier/verifier-py.git
```

## Usage

The library provides two main functions:

- `verify(email, access_token)`: Returns a boolean indicating whether the email is valid.
- `verifyRequest(email, access_token)`: Returns the full API response as a dictionary.

### Example

```python
import verifier

# Replace 'API_TOKEN' with your actual API token
email = 'email@example.com'
access_token = 'API_TOKEN'

# Simple verification
if verifier.verify(email, access_token):
    print("Hurray! Email is right!")
else:
    print("Oh! Email is not real")

# Full API response
response = verifier.verifyRequest(email, access_token)
if response:
    print("Full API response:", response)
else:
    print("Failed to verify email.")
```

### Error Handling

The library uses Python's built-in logging module to log errors. You can configure the logging level to control the verbosity of the logs. By default, it logs errors to the console.

### Logging Configuration

To change the logging level, you can modify the logging configuration in your application:

```python
import logging

logging.basicConfig(level=logging.DEBUG)  # Set to DEBUG to see all logs
```

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

### License

This project is licensed under the MIT License.