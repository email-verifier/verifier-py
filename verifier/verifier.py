import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def verify(email, access_token):
    params = (
        ('token', access_token),
    )

    try:
        response = requests.get('https://verifyright.co/verify/' + email, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data['status']
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return False
    except ValueError:
        logging.error("Failed to parse JSON response")
        return False

def verifyRequest(email, access_token):
    params = (
        ('token', access_token),
    )
    
    try:
        response = requests.get('https://verifyright.co/verify/' + email, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return None
    except ValueError:
        logging.error("Failed to parse JSON response")
        return None
