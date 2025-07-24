import hashlib

import numpy as np


def embed_text(text: str) -> np.ndarray:
    """Mock embedding function for testing with deterministic return values."""
    # Create hash: deterministic and fast
    hash_object = hashlib.sha256(text.encode())
    hash_value = hash_object.digest()

    return np.frombuffer(hash_value, dtype=np.uint8).astype(np.float32)
