import json
import urllib.request
from jose import jwk, jwt
from jose.utils import base64url_decode
# Load AWS config
USER_POOL_ID = 'eu-west-2_uhta1UGB8'
APP_CLIENT_ID = '2nc4152vpivm81j2qfapb9u75f'
REGION = 'eu-west-2'
POOL_URL = f'https://cognito-idp.{REGION}.amazonaws.com/{USER_POOL_ID}'

# Download and cache JWKs
jwks_url = f'{POOL_URL}/.well-known/jwks.json'
with urllib.request.urlopen(jwks_url) as f:
    response = f.read()
keys = json.loads(response.decode('utf-8'))['keys']

def verify_jwt_token(token):
    headers = jwt.get_unverified_headers(token)
    kid = headers['kid']

    # Find matching public key
    key_index = next((i for i, k in enumerate(keys) if k['kid'] == kid), -1)
    if key_index == -1:
        raise Exception('Public key not found.')

    public_key = jwk.construct(keys[key_index])
    message, encoded_signature = str(token).rsplit('.', 1)
    decoded_signature = base64url_decode(encoded_signature.encode('utf-8'))

    if not public_key.verify(message.encode("utf8"), decoded_signature):
        raise Exception('Signature verification failed.')

    claims = jwt.get_unverified_claims(token)

    # Accept both ID and Access tokens
    if 'aud' in claims:
        if claims['aud'] != APP_CLIENT_ID:
            raise Exception('Token was not issued for this audience.')
    elif 'client_id' in claims:
        if claims['client_id'] != APP_CLIENT_ID:
            raise Exception('Token was not issued for this client.')
    else:
        raise Exception("Token missing both 'aud' and 'client_id'. Invalid token.")

    return claims