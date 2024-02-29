import requests
from env import token
from log_init import logger


with requests.Session() as session:
    users = session.get('https://192.168.180.3/api/v4/users', headers={'PRIVATE-TOKEN': token}, verify=False)
    for user in users.json():
        if not user['is_admin']:
            block = session.post(f'https://192.168.180.3/api/v4/users/{user["id"]}/block',
                                 headers={'PRIVATE-TOKEN': token},
                                 verify=False)
            logger.debug(f'{user['username']} - {block.json()}')
        else:
            logger.debug(f'{user['username']} - admin')




