import datetime
from typing import Any, Dict, Optional
import bcrypt
import jwt

def get_password_hash(password: str) -> str:
    """
    Hashes a password using bcrypt.
    """
    pwd_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd_bytes, salt)
    return hashed.decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a plain password against a bcrypt hash.
    """
    try:
        return bcrypt.checkpw(
            plain_password.encode("utf-8"),
            hashed_password.encode("utf-8"),
        )
    except Exception:
        return False

def generate_agent_token(agent_id: str, secret_key: str) -> str:
    """
    Generates a secure JWT token for agent authentication.
    """
    now = datetime.datetime.now(datetime.timezone.utc)
    payload = {
        "sub": agent_id,
        "iat": now,
        "exp": now + datetime.timedelta(days=365),  # Long-lived token for agents
    }
    return jwt.encode(payload, secret_key, algorithm="HS256")

def verify_agent_token(token: str, secret_key: str) -> Optional[Dict[str, Any]]:
    """
    Decodes and verifies a JWT token. Returns the payload dict or None if invalid.
    """
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return payload
    except jwt.PyJWTError:
        return None
