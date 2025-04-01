def calculate_gs_score(correct_count, attempted_count):
    total_questions = 100
    marks_per_question = 2
    negative_marking = 0.66

    # Calculate wrong answers
    wrong_count = attempted_count - correct_count
    if wrong_count < 0:
        wrong_count = 0  # Ensure wrong count is not negative

    # Calculate total score
    score = (correct_count * marks_per_question) - (wrong_count * negative_marking)
    return score

def calculate_csat_score(correct_count, attempted_count):
    total_questions = 80
    marks_per_question = 2.5
    negative_marking = 0.66

    # Calculate wrong answers
    wrong_count = attempted_count - correct_count
    if wrong_count < 0:
        wrong_count = 0  # Ensure wrong count is not negative

    # Calculate total score
    score = (correct_count * marks_per_question) - (wrong_count * negative_marking)
    return score

def main():
    print("=" * 50)
    print(" " * 15 + "Welcome to the Exam Score Calculator")
    print("=" * 50)

    # GS Paper Calculation
    print("\n" + "=" * 30)
    print(" " * 10 + "GS Paper Score Calculation")
    print("=" * 30)
    correct_gs = int(input("Enter the number of correct answers for GS: "))
    attempted_gs = int(input("Enter the number of attempted questions for GS: "))
    gs_score = calculate_gs_score(correct_gs, attempted_gs)
    print(f"Total GS Score: {gs_score:.2f}")
    print("=" * 30)

    # CSAT Paper Calculation
    print("\n" + "=" * 30)
    print(" " * 10 + "CSAT Paper Score Calculation")
    print("=" * 30)
    correct_csat = int(input("Enter the number of correct answers for CSAT: "))
    attempted_csat = int(input("Enter the number of attempted questions for CSAT: "))
    csat_score = calculate_csat_score(correct_csat, attempted_csat)
    print(f"Total CSAT Score: {csat_score:.2f}")
    print("=" * 30)

    print("\n" + "=" * 50)
    print(" " * 15 + "Thank you for using the Exam Score Calculator!")
    print("=" * 50)

if __name__ == "__main__":
    main()

