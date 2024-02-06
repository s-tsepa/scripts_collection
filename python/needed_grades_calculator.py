from typing import Iterable, Sequence


class Course:
    name: str
    cur_sum = 0
    cur_max = 0
    cur_sum_real = 0

    # min_c_points = 60

    def __init__(
            self,
            name: str,
            min_c_points: float,
            grades: Iterable[Sequence[float]]):
        self.name = name
        self.min_c_points = min_c_points
        for i in grades:
            a = i[0]
            b = i[1]
            c = i[2] if len(i) > 2 else 1
            self.add_new_grade(a, b, c)

    @property
    def left_max(self):
        return 100 - self.cur_max

    @property
    def left_needed(self):
        return self.min_c_points - self.cur_sum

    @property
    def real_s(self):
        return f"{round(self.cur_sum, 2)}" if self.cur_sum else f"({round(self.cur_sum_real, 2)})"

    def cur_ratio(self):
        return self.cur_sum / self.cur_max

    def add_new_grade(self, grade: float, max_grade: float, weight_coeff: int = 1):
        self.cur_sum += grade * weight_coeff
        self.cur_max += max_grade * weight_coeff

        # self.cur_max = round(self.cur_max, 2)
        # self.cur_sum = round(self.cur_sum, 2)

        if max_grade != 0:
            self.cur_sum_real = self.cur_sum

    def needed_ratio_for_left(self):
        if self.left_max == 0:
            if self.left_needed == 0:
                return None
            elif self.left_needed > 0:
                return "YOU GO TO RETAKE!"
            elif self.left_needed < 0:
                return "Completed !!!"
        res = self.left_needed / self.left_max
        res = round(res, 2)
        if res > 1:
            return f"You WILL go to Retake!: {res}"
        return res

    def __str__(self):
        return f"CUR: {self.real_s} / {self.cur_max} | " \
               f"LEFT NEEDED: {round(self.left_needed, 2)} / {round(self.left_max, 2)} [{self.needed_ratio_for_left()}]"

    def str_format(self, by_str: str):
        print(f"\n--- {self.name} ---")
        return by_str.format(f'{self.real_s} / {round(self.cur_max, 2)}', f'{round(self.left_needed, 2)} / {round(self.left_max, 2)}',
                             f'[{self.needed_ratio_for_left()}]')


offsets = [20, 20, 15]
offsets_s = ' '.join([f"{{:<{i}}}" for i in offsets])

print(offsets_s.format('CUR', 'LEFT NEEDED', 'Percent LEFT'))

courses = []


# c = Course('Diffurs', 55, [
#     (1, 15),  # Shilov theor 1
#     (7, 15),  # Practical 1
#     (12, 0),  # Bonus points
#     # (3, 0),   # Collocvium bonus points
#     (15, 15),  # Computational test

#     (11.5, 15),  # --- 2nd practical test
#     (4, 15),  # --- (THeor 2) Shilov test
#     # (4, 25)   # --- Final theor Oral
# ])
# # courses.append(c)
# print(c.str_format(offsets_s))

# c = Course('OS\'i', 60, [
#     [8.3, 10],  # Quizzes
#     [30 * 0.7833, 30],  # HW's (Labs)
#     [10.5, 20],  # Midterm
#     # [15, 20],  # Final
#     # [16, 20],  # Unattended Oral

#     [5, 0],  # Participation
# ])
# # courses.append(c)
# # print(c.str_format(offsets_s))

# c = Course('Optimization', 60, [
#     (7.5, 15),  # Test 1
#     (17, 30),  # Midterm
#     (11, 15),  # Test 2
#     # (25, 40),  # Final
# ])
# # print(c.str_format(offsets_s))
# # courses.append(c)

# c = Course('Probstat', 50, [
#     [12, 14],  # Test1
#     [12, 20],  # Midterm
#     [7, 14],  # Test2
#     # [0, 50], # Final
# ])
# print(c.str_format(offsets_s))
# # courses.append(c)

# c = Course('Intro to AI (Philo)', 60, [
#     [25 * 0.65, 25],  # Midterm
#     [20 * 0.82, 20],  # HW1
#     [9, 10],  # Attendance
#     # [1, 0], # Bonus
#     [20 * 0.89, 20], #HW2
#     [0.57 * 25, 25],  # Final
# ])
# # courses.append(c)


# c = Course('Physics', 50, [
#     # (3, 5),     # Attendance
#     (6.4, 10),  # Quiz 1
#     (5.3, 10),  # Quiz 2
#     (7.5, 10),  # Quiz 3
#     (5, 10),  # Quiz 4
#     (0, 10),  # Quiz 5
#     (3.75, 5),  # Assignment 1
#     (3.75, 5),  # Assignment 2
#     (5, 5),  # Assignment 3
#     (3.75, 5),  # Assignment 4
#     (4, 5),  # Assignment 5
#     # (0, 25),    # Final
# ])
# print(c.str_format(offsets_s))
# # courses.append(c)
# n_labs = 7

# c = Course('FIS', 60, [  # C
#     (2.5, 5),           # Attendance
#     (2, 2.5),     # Quiz 1
#     (2, 2.5),     # Quiz 1
#     (2, 2.5),     # Quiz 1
#     (2, 2.5),     # Quiz 1
#     (0.75 * 45/n_labs, 45/n_labs),    # Lab 1
#     (0.90 * 45/n_labs, 45/n_labs),    # Lab 2
#     (0 * 45/n_labs, 45/n_labs),    # Lab 3
#     (0 * 45/n_labs, 45/n_labs),    # Lab 4
#     (0.85 * 45/n_labs, 45/n_labs),    # Lab 5
#     (1.0 * 45/n_labs, 45/n_labs),    # Lab 6
#     (1.0 * 45/n_labs, 45/n_labs),    # Lab 7
#     (25.83, 40),    # Final
# ])
# courses.append(c)

# c = Course('IR', 60, [  # C
#     (6.67, 10),  # Quiz 1
#     (10, 10),  # Quiz 2
#     (10, 10),  # Quiz 3
#     (10, 10),  # Quiz 4
#     (10, 10),  # HW 1
#     (15, 15),  # HW 2
#     (5, 15),  # HW 3
#     (10, 20),  # HW 4
# ])
# courses.append(c)

# c = Course('DCD', 60, [  # C
#     (0, 10),  # Attendance
#     (10, 10),  # Lab 1
#     (10, 10),  # Lab 2
#     (6, 10),  # Lab 3
#     (6, 10),  # Lab 4
#     (13.9, 20),  # Final
#     # (35, 40),  # Project
# ])
# courses.append(c)

c = Course('SQR', 60, [  # C
    (0, 8),    # Quizzes (p1)
    (8.5, 12),  # Quizzes (p2)
    # (0, 60),    # Labs
    # (0, 20),    # Project
])
courses.append(c)

# c = Course('DE', 60, [  # C
#     (0, 10),    # Attendance
#     (0, 55),    # Labs
#     (0, 35),    # Exam
# ])
# courses.append(c)


# c = Course('Networks', 60, [  # C
#     (5, 5),  # Quizzes
#     (9/11 * 20, 20),  # Midterm
#     (3, 10), # Lec attendance
#     (15, 15), # Labs
#     # (0, 50),  # Final
# ])
# courses.append(c)

# c = Course('DB', 65, [  # B
#     (0.842 * 20, 20),  # Midterm
#     (20, 20), # Labs
#     (20 * 0.85, 20), # Assignment
#     # (0, 40),  # Final
# ])
# courses.append(c)

# c = Course('DNP', 60, [  # C
#     (10, 10),  # Lab 01
#     (5, 10),  # Lab 02
#     (9.5, 10),  # Lab 03
#     (0, 10),  # Lab 04
#     (0, 10),  # Lab 05
#     # (_, 10),  # Lab 06
#     # (_, 34),  # Final exam
#     (1.5, 6),  # Attendance
# ])
# courses.append(c)

def sort_by(x):
    a = x.needed_ratio_for_left()
    if isinstance(a, float):
        # print(a)
        return a
    return 0


courses.sort(key=sort_by, reverse=True)
c: Course
for c in courses:
    print(c.str_format(offsets_s))
