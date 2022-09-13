import sys

def gpacalc():
    gpa_dict = {'A':4.0, 'A-':3.66, 'B+':3.33, 'B':3.0, 'B-':2.66, 'C+':2.33, 'C':2.0, 'C-':1.66, 'D+':1.33, 'D':1.00, 'D-':.66, 'F':0.00}
    grade_list = []
    grade1 = sys.argv[1]
    grade2 = sys.argv[2]
    grade3 = sys.argv[3]
    grade4 = sys.argv[4]

    # grade1 = a
    # grade2 = b
    # grade3 = c
    # grade4 = d

    grade1 = grade_list.append(grade1.upper())
    grade2 = grade_list.append(grade2.upper())
    grade3 = grade_list.append(grade3.upper())
    grade4 = grade_list.append(grade4.upper())
    gpa = 0

    for k in grade_list:
        if k in gpa_dict.keys():
            gpa += gpa_dict[k]
    
    gpa = round(gpa/4, 2)

    print(f'My GPA is {gpa:.2f}')

gpacalc()