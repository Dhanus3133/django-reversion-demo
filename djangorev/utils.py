import base64
from strawberry_django_plus import gql

def decode_id_from_gql_id(gql_id: gql.ID):
    return int(base64.b64decode(gql_id).decode().split(":")[1])
