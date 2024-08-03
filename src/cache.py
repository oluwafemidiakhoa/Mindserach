import os
import json
import hashlib
from datetime import datetime, timedelta

CACHE_DIR = 'cache'
CACHE_EXPIRY = timedelta(hours=1)

def _get_cache_path(key):
    hashed_key = hashlib.md5(key.encode()).hexdigest()
    return os.path.join(CACHE_DIR, hashed_key + '.json')

def get_cache(key):
    path = _get_cache_path(key)
    if not os.path.exists(path):
        return None
    with open(path, 'r') as file:
        data = json.load(file)
    if datetime.fromisoformat(data['timestamp']) + CACHE_EXPIRY < datetime.now():
        os.remove(path)
        return None
    return data['value']

def set_cache(key, value):
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)
    data = {
        'timestamp': datetime.now().isoformat(),
        'value': value
    }
    with open(_get_cache_path(key), 'w') as file:
        json.dump(data, file)
