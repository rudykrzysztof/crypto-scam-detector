def classify_score(score: int) -> str:
    if score >= 80:
        return "LIKELY SCAM"
    if score >= 50:
        return "HIGH RISK"
    if score >= 25:
        return "RISKY"
    return "SAFE"
