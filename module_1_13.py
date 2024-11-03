grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

dictStudents = dict()
studentsSort = sorted(list(students))
for i in range(len(studentsSort)):
          dictStudents[studentsSort[i]]= sum(grades[i]) / len(grades[i])
print(dictStudents)

