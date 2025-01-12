import requests
#
# If you don't want a library for python
# response = requests.get('https://verifier.meetchopra.com/verify/{{email_address}}?token=access_token')


def verify(email, access_token):
    params = (
        ('token', access_token),
    )

    response = requests.get('https://verifier.meetchopra.com/verify/' + email, params=params)

    try:
        data = response.json()
    except:
        return False

    return data['status']

def verifyRequest(email, access_token):
    params = (
        ('token', access_token),
    )
    
    response = requests.get('https://verifier.meetchopra.com/verify/'+ email, params=params)

    try:
        data = response.json()
    except:
        return False

    return data
