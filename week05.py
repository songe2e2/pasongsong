class Student:
    def __init__(self, korean_score, english_score, math_score):
        self.korean_score = korean_score
        self.english_score = english_score
        self.math_score = math_score

    def calculate_average(self):
        return (self.korean_score + self.english_score + self.math_score) / 3

def main():
    num_students = int(input("학생 수를 입력하세요: "))

    for i in range(num_students):
        korean_score = float(input(f"{i+1}번째 학생의 국어 점수를 입력하세요: "))
        english_score = float(input(f"{i+1}번째 학생의 영어 점수를 입력하세요: "))
        math_score = float(input(f"{i+1}번째 학생의 수학 점수를 입력하세요: "))

        student = Student(korean_score, english_score, math_score)
        average_score = student.calculate_average()
        print(f"{i+1}번째 학생의 평균 점수: {average_score:.2f}")

if __name__ == "__main__":
    main()
