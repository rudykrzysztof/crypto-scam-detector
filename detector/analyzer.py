from detector.rules import RED_FLAG_RULES, SUSPICIOUS_PATTERNS
from detector.scorer import classify_score


def analyze_project_text(text: str) -> dict:
    normalized = text.lower()
    score = 0
    matches = []

    for phrase, points in RED_FLAG_RULES.items():
        if phrase in normalized:
            score += points
            matches.append({
                "type": "keyword",
                "label": phrase,
                "points": points
            })

    for label, checker, points in SUSPICIOUS_PATTERNS:
        if checker(text):
            score += points
            matches.append({
                "type": "pattern",
                "label": label,
                "points": points
            })

    verdict = classify_score(score)

    return {
        "score": score,
        "verdict": verdict,
        "matches": matches
    }
