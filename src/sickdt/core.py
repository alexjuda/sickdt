from datetime import datetime, timezone


def now():
    return datetime.now(timezone.utc)


def from_unix(seconds: float) -> datetime:
    return datetime.fromtimestamp(seconds).replace(tz=timezone.utc)


def _ensure_tz(dt: datetime):
    if dt.tzinfo is None:
        raise ValueError(f"This datetime is timezone-naive: {dt}")


def unix(instant: datetime) -> float:
    _ensure_tz(instant)
    return instant.timestamp()


def from_iso(timestamp: str) -> datetime:
    # 1. Change Zulu -> explicit timezone
    explicit = timestamp.replace("Z", "+00:00")
    # 2. Parse
    return datetime.fromisoformat(explicit)


def iso(instant: datetime) -> str:
    _ensure_tz(instant)
    # 1. Make sure it's in UTC
    utc_instant = instant.astimezone(timezone.utc)
    # 2. Generate timestamp
    ts = utc_instant.isoformat()
    # 3. Make it Zulu time
    return ts.replace("+00:00", "Z")
