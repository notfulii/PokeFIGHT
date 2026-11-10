import hashlib
import hmac
import json
import os
import secrets
import settings


def load_users():
    if not os.path.exists(settings.USERS_FILE):
        return {}

    with open(settings.USERS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_users(users):
    folder = os.path.dirname(settings.USERS_FILE)
    os.makedirs(folder, exist_ok=True)

    with open(settings.USERS_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=2)


def hash_password(password, salt):
    password_bytes = password.encode("utf-8")
    salt_bytes = bytes.fromhex(salt)
    hashed = hashlib.pbkdf2_hmac("sha256", password_bytes, salt_bytes, settings.PASSWORD_HASH_ITERATIONS)
    return hashed.hex()


def register(username, password):
    username = username.strip()
    if username == "" or password.strip() == "":
        return False

    users = load_users()
    if username in users:
        return False

    salt = secrets.token_hex(settings.SALT_SIZE)
    users[username] = {"salt": salt, "hash": hash_password(password, salt)}
    save_users(users)
    return True


def login(username, password):
    users = load_users()
    if username not in users:
        return False

    user = users[username]
    typed_hash = hash_password(password, user["salt"])
    return hmac.compare_digest(typed_hash, user["hash"])
