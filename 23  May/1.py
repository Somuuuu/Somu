students_db = {
    'grading_scales': {
        'percentage': {
            'math': {'min': 97, 'max': 100, 'grade': 'A'},
            'science': {'min': 93, 'max': 96, 'grade': 'A+'},
            'english': {'min': 90, 'max': 92, 'grade': 'A++'},
            'history': {'min': 87, 'max': 89, 'grade': 'B'},
            'physics': {'min': 83, 'max': 86, 'grade': 'B+'},
        }
    }
}
subject = input("Enter subject name: ")
mark = int(input("Enter marks: "))
if subject in students_db['grading_scales']['percentage']:
    a = students_db['grading_scales']['percentage'][subject]
    if mark >= a['min'] and mark <= a['max']:
        print(a['grade'])
    else:
        print("You didn't scored minimum marks, but you passed.")
else:
    print("Enter valid subject name")    