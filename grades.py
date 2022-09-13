import sys

def grades():

    relations = {'Biology':80, 'Physics':88, 'Chemistry':98, 'Math':89, 'English':79, 'Music':67, 'History':68, 'Art':53, 'Economics':95, 'Psychology':88}

    grade = 0
    seen_grade = 0
    arg = sys.argv[1]
    for k, v in relations.items():
        if k == arg:
            pass
        else:
            grade += v
            seen_grade += 1

    final_grade = grade/seen_grade

    print(round(final_grade, 2))


grades()