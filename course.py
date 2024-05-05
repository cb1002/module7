  
room_dictionary = {
    'CSC101': '3004',
    'CSC102': '4501',
    'CSC103': '6755',
    'NET110': '1244',
    'COM241': '1411'
}


instructor_dictionary = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

time_dictionary = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}

course_number = input("Enter a course number : ")

room = room_dictionary.get(course_number)
instructor = instructor_dictionary.get(course_number)
meeting_time = time_dictionary.get(course_number)

if room and instructor and meeting_time:
    print(f"Course {course_number}:")
    print(f"Room Number: {room}")
    print(f"Instructor: {instructor}")
    print(f"Meeting Time: {meeting_time}")
else:
    print("Unable to find course. Maybe try a different number?")