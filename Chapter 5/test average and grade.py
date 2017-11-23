def calc_average(test1, test2, test3, test4, test5):
    return (test1 + test2 + test3 + test4 + test5) / 5


def determine_grade(test_score):
    if 100 > test_score > 90:
        return 'A'
    elif 89 > test_score >= 80:
        return 'B'
    elif 79 > test_score >= 70:
        return 'C'
    elif 69 > test_score >= 60:
        return 'D'
    else:
        return 'F'


def main():
    print("Welcome to your test grade")
    test1 = int(input("Enter the score for test 1"))
    test2 = int(input("Enter the score for test 2"))
    test3 = int(input("Enter the score for test 3"))
    test4 = int(input("Enter the score for test 4"))
    test5 = int(input("Enter the score for test 5"))
    average = calc_average(test1, test2, test3, test4, test5)
    test1_grade = determine_grade(test1)
    test2_grade = determine_grade(test2)
    test3_grade = determine_grade(test3)
    test4_grade = determine_grade(test4)
    test5_grade = determine_grade(test5)
    average_grade = determine_grade(average)
    print("test score and grade of test 1 is ", test1, test1_grade)
    print("test score and grade of test 2 is ", test2, test2_grade)
    print("test score and grade of test 3 is ", test3, test3_grade)
    print("test score and grade of test 4 is ", test4, test4_grade)
    print("test score and grade of test 5 is ", test5, test5_grade)
    print("Average of score and grade is ", average, average_grade)


main()
