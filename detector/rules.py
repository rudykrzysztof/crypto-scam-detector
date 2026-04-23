RED_FLAG_RULES = {
    "guaranteed profit": 30,
    "risk-free": 25,
    "anonymous team": 20,
    "100x": 20,
    "instant profit": 20,
    "passive income": 15,
    "limited time": 10,
    "no audit": 25,
    "secret strategy": 20,
    "double your money": 30,
    "moon soon": 10,
    "get rich quick": 30,
    "exclusive presale": 10,
    "locked forever": 5,
    "next bitcoin": 10,
    "zero risk": 30,
    "guaranteed returns": 35,
    "financial freedom overnight": 35
}

SUSPICIOUS_PATTERNS = [
    ("too many exclamation marks", lambda text: text.count("!") >= 5, 10),
    ("too many uppercase words", lambda text: sum(1 for word in text.split() if word.isupper() and len(word) > 3) >= 5, 15),
    ("very short description", lambda text: len(text.split()) < 15, 10),
]
