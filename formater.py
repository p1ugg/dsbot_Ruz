from datetime import datetime


def format_schedule_one_day(schedule):
    UTC_PLUS = 3
    if len(schedule) == 0:
        return "В этот день нет пар, отдыхаем!"

    res = ''
    for lesson in schedule:
        time_start = str(int(lesson['date_start'].split("T")[1].split(":")[0]) + UTC_PLUS) + ":" + \
                     lesson['date_start'].split("T")[1].split(":")[1]

        time_end = str(int(lesson['date_end'].split("T")[1].split(":")[0]) + UTC_PLUS) + ":" + \
                   lesson['date_end'].split("T")[1].split(":")[1]
        try:
            res += """
    Дисциплина: %s - %s
    Корпус: %s 
    Время: %s - %s
    Аудитория: %s
    Преподователь: %s (%s)""" % (
                lesson['discipline'], lesson['type'], lesson['building'], time_start, time_end, lesson['auditorium'],
                lesson['lecturer_profiles'][0]['full_name'], lesson['lecturer_profiles'][0]['email'])
        except Exception as ex:
            res += """
    Дисциплина: %s - %s
    Корпус: %s 
    Время: %s - %s
    Аудитория: %s
    Преподователь: %s (%s)""" % (
    lesson['discipline'], 'None',lesson['building'], time_start, time_end, lesson['auditorium'],
    lesson['lecturer_profiles'][0]['full_name'], lesson['lecturer_profiles'][0]['email'])

        res += "\n--------------\n"

    return res


def format_schedule_active(schedule):
    UTC_PLUS = 3
    if len(schedule) == 0:
        return "Сейчас нет пар"

    res_list = []
    res = ""
    dd = schedule[0]['date_start']
    pp = datetime.fromisoformat(dd.replace("Z", "+00:00"))
    dd = pp.strftime("%d %B")
    for lesson in schedule:
        time_start = str(int(lesson['date_start'].split("T")[1].split(":")[0]) + UTC_PLUS) + ":" + \
                     lesson['date_start'].split("T")[1].split(":")[1]

        time_end = str(int(lesson['date_end'].split("T")[1].split(":")[0]) + UTC_PLUS) + ":" + \
                   lesson['date_end'].split("T")[1].split(":")[1]
        date_str = lesson['date_start']
        pdate = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        date = pdate.strftime("%d %B")
        if date != dd:
            res_list.append(res)
            res = ''
            dd = date
        res += """
Дата: %s
Дисциплина: %s - %s
Корпус: %s 
Время: %s - %s
Аудитория: %s
Преподователь: %s (%s)""" % (date,
                             lesson['discipline'], lesson['type'], lesson['building'], time_start, time_end,
                             lesson['auditorium'],
                             lesson['lecturer_profiles'][0]['full_name'], lesson['lecturer_profiles'][0]['email'])

        res += "\n--------------\n"

    return res_list


def format_mes(keys_of_materials):
    list_of_keys = """"""
    for i in range(len(list(keys_of_materials.keys()))):
        list_of_keys += str(i + 1) + ". " + list(keys_of_materials)[i] + '\n'

    return list_of_keys
