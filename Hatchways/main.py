import json
import sys
from csv import DictReader


# This array store all the students with their respective test and marks
students = {}
# This array store all the courses with their respective test and weightage
courses = {}


def store_student_course(csv_arg, class_name):
    with open(csv_arg, encoding="utf-8") as csvf:
        csv_reader = DictReader(csvf)

        for row in csv_reader:
            if "id" in row.keys():
                row["id"] = int(row["id"])
            if class_name == "Course":
                courses[row["id"]] = {"name": row["name"], "teacher": row["teacher"], "test_weightage": {}}
            if class_name == "Student":
                students[row["id"]] = {"name": row["name"], "test_marks": {}}


def store_tests(csv_arg):
    with open(csv_arg, encoding="utf-8") as csvf:
        csv_reader = DictReader(csvf)

        # Convert each row into a dictionary in courses array
        for row in csv_reader:
            if "id" in row.keys():
                row["id"] = int(row["id"])
            if "course_id" in row.keys():
                row["course_id"] = int(row["course_id"])
            if "weight" in row.keys():
                row["weight"] = float(row["weight"])/100
            courses[row["course_id"]]["test_weightage"][row["id"]] = row["weight"]


def store_marks(csv_arg):
    with open(csv_arg, encoding="utf-8") as csvf:
        csv_reader = DictReader(csvf)

        # Convert each row into a dictionary in students array
        for row in csv_reader:
            if "test_id" in row.keys():
                row["test_id"] = int(row["test_id"])
            if "student_id" in row.keys():
                row["student_id"] = int(row["student_id"])
            if "mark" in row.keys():
                row["mark"] = float(row["mark"])
            students[row["student_id"]]["test_marks"][row["test_id"]] = row["mark"]


def check_course_weights():
    for key, values in courses.items():
        return False if sum(values["test_weightage"].values()) != 1 else True


def make_json_calculate_total_average(test_marks):
    total_average = 0.0
    course_counter = 0
    for values in courses.values():
        courses_set = test_marks.keys() & values["test_weightage"].keys()
        if courses_set:
            course_counter += 1
        for keys in courses_set:
            total_average += test_marks[keys] * values["test_weightage"][keys]
    return float("{:.2f}".format(total_average/course_counter))


def make_json_student_courses(test_marks):
    student_courses = []
    for key, values in courses.items():
        course_test = test_marks.keys() & values["test_weightage"].keys()
        if course_test:
            course_average = 0.0
            for course in course_test:
                course_average += (test_marks[course] * values["test_weightage"][course])
            student_courses.append(
                {
                    "id": key,
                    "name": values["name"],
                    "teacher": values["teacher"],
                    "courseAverage": float("{:.2f}".format(course_average))
                }
            )
    return student_courses


def make_json():
    final_json = {}
    if students:
        if check_course_weights():
            final_json = {"students": []}
            for key, value in students.items():
                final_json["students"].append(
                    {
                        "id": key,
                        "name": value["name"],
                        "totalAverage": make_json_calculate_total_average(value["test_marks"]),
                        "courses": make_json_student_courses(value["test_marks"])
                    }
                )
        else:
            final_json = {"error": "Invalid course weights"}
    else:
        final_json = {"error": "There are not students"}
    return final_json


def dump_data(output_file):
    with open(output_file, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(make_json(), indent=2))


# Call the make_json function
store_student_course(sys.argv[1], "Course")
store_student_course(sys.argv[2], "Student")
store_tests(sys.argv[3])
store_marks(sys.argv[4])
dump_data(sys.argv[5])
