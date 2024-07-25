grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(sorted(students))
avarge_score = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]),
                sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]

student_grades_set = {students[0]: avarge_score[0], students[1]: avarge_score[1],
                      students[2]: avarge_score[2], students[3]: avarge_score[3], students[4]: avarge_score[4]}

print(student_grades_set)