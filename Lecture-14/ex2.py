def get_grades(d, names):
    # grades = []
    # for key in names:
    #     if key in d:
    #         print(d[key])
    #         grades.append(d[key])
    grades= [d[key]for key in names if key in d ]
    return grades


student_list ={
    'john': 'A',
    'betty':'B',
    'sean':'C'
}

result= get_grades(student_list, ['john', 'sean'])
print(result)
