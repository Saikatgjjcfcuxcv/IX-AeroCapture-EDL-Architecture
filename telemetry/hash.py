from __future__ import annotations

import hashlib
import json
from typing import Any, Dict


def stable_json_dumps(obj: Any) -> str:
    """
    Stable JSON encoding for hashing/diffing.
    """
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_short(obj: Any, n: int = 12) -> str:
    payload = stable_json_dumps(obj).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:n]
