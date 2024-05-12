from datetime import datetime


def format_schedule_one_day(schedule):
    UTC_PLUS = 3
    if len(schedule) == 0:
        return "В этот день нет пар, отдыхаем!"

    # res = schedule[0]['date_start'].split("T")[0] + "\n\n"
    res = ''
    # res += """Пары на сегодня:"""

    for lesson in schedule:
        time_start = str(int(lesson['date_start'].split("T")[1].split(":")[0]) + UTC_PLUS) + ":" + \
                     lesson['date_start'].split("T")[1].split(":")[1]

        time_end = str(int(lesson['date_end'].split("T")[1].split(":")[0]) + UTC_PLUS) + ":" + \
                   lesson['date_end'].split("T")[1].split(":")[1]
        res += """
Дисциплина: %s - %s
Корпус: %s 
Время: %s - %s
Аудитория: %s
Преподователь: %s (%s)""" % (
        lesson['discipline'], lesson['type'], lesson['building'], time_start, time_end, lesson['auditorium'], lesson['lecturer_profiles'][0]['full_name'], lesson['lecturer_profiles'][0]['email'])

        res += "\n--------------\n"

    return res


def format_schedule_active(schedule):
    UTC_PLUS = 3
    if len(schedule) == 0:
        return "Сейчас нет пар"

    res_list = []
    res = ""
    dd = ''
    for lesson in schedule:
        time_start = str(int(lesson['date_start'].split("T")[1].split(":")[0]) + UTC_PLUS) + ":" + \
                     lesson['date_start'].split("T")[1].split(":")[1]

        time_end = str(int(lesson['date_end'].split("T")[1].split(":")[0]) + UTC_PLUS) + ":" + \
                   lesson['date_end'].split("T")[1].split(":")[1]
        date_str = lesson['date_start']
        pdate = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        date = pdate.strftime("%d %B")
        res += """
Дата: %s
Дисциплина: %s - %s
Корпус: %s 
Время: %s - %s
Аудитория: %s
Преподователь: %s (%s)""" % (date,
            lesson['discipline'], lesson['type'], lesson['building'], time_start, time_end, lesson['auditorium'],
            lesson['lecturer_profiles'][0]['full_name'], lesson['lecturer_profiles'][0]['email'])

        res += "\n--------------\n"

    return res


# def format_students_list(students_list):
#     res = ""
#     for i in range(len(students_list)):
#         res += "%s. %s - %s \n" % (str(i + 1), students_list[i]['label'], students_list[i]['description'])
#
#     return res

