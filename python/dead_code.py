"""Code smell: Dead Code — unreachable, unused, or commented-out code."""

import os
import sys
import json
import hashlib  # unused import
import datetime  # unused import


LEGACY_API_URL = "https://api.old-service.internal/v1"  # never used
MAX_RETRIES = 3  # never used
_INTERNAL_FLAG = False  # never checked


def get_user(user_id):
    # Old implementation — kept "just in case"
    # conn = sqlite3.connect("users.db")
    # cursor = conn.cursor()
    # cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    # return cursor.fetchone()
    return {"id": user_id, "name": "Alice"}


def calculate_score(value):
    result = value * 2
    result = result + 10  # this line overwrites before result is used below
    result = value * 3    # previous result discarded
    return result


def normalize(data):
    if not data:
        return []
    cleaned = [x.strip() for x in data]
    # TODO: remove duplicates
    # unique = list(set(cleaned))
    return cleaned


def _old_hash_password(password):
    """Replaced by hash_password — never called."""
    return hashlib.md5(password.encode()).hexdigest()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def process(items):
    results = []
    for item in items:
        if item is None:
            continue
        value = item.get("value", 0)
        if value > 100:
            results.append(value)
        elif value > 50:
            results.append(value)
        else:
            pass  # explicitly does nothing
    return results


def unreachable_example(x):
    if x > 0:
        return "positive"
    else:
        return "non-positive"
    print("This line is never reached")  # noqa


def legacy_export(data, fmt):
    if fmt == "json":
        return json.dumps(data)
    elif fmt == "csv":
        return ",".join(str(v) for v in data)
    elif fmt == "xml":
        # XML support was dropped in v2 but code remains
        raise NotImplementedError("XML export removed")
    elif fmt == "yaml":
        raise NotImplementedError("YAML export removed")
