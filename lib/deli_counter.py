katz_deli = ["Logan", "Avi", "Spencer", "Ruchi"]


def line(list_of_people_in_line):
    if len(list_of_people_in_line) == 0:
        print("The line is currently empty.")
    else:
        numbered_line_list = [
            f"{index + 1}. {person}"
            for index, person in enumerate(list_of_people_in_line)
        ]
        formatted_line = " ".join(numbered_line_list)
        print(f"The line is currently: {formatted_line}")


def take_a_number(list_of_people_in_line, person_name):
    list_of_people_in_line.append(person_name)
    number_in_line = list_of_people_in_line.index(person_name)
    print(f"Welcome, {person_name}. You are number {number_in_line + 1} in line.")


def now_serving(list_of_people_in_line):
    if len(list_of_people_in_line) > 0:
        first_in_line = list_of_people_in_line.pop(0)
        print(f"Currently serving {first_in_line}.")
    else:
        print("There is nobody waiting to be served!")


take_a_number(katz_deli, "Michael")
