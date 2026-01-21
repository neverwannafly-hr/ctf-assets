import hashlib

def stamp(row_id, country, city, ts):
    msg = f"BLACKWIRE|{row_id}|{country}|{city}|{ts}".encode()
    return hashlib.sha256(msg).hexdigest()[:10]
