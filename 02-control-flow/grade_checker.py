def letter_grade(score: float) -> str:
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")
    if score >= 80:
        return "A+"
    if score >= 70:
        return "A"
    if score >= 60:
        return "A-"
    if score >= 50:
        return "B"
    if score >= 40:
        return "C"
    if score >= 33:
        return "D"
    return "F"


if __name__ == "__main__":
    score = float(input("Score: "))
    print("Grade:", letter_grade(score))
