import pandas as pd


def get_teachers():
    file = 'data/teachers.xlsx'

    df = pd.read_excel(file)

    data_list = df.values.tolist()

    s = ''

    for num, row in enumerate(data_list):
        s += f"""
{num+1}. ФИО: {row[0]}
Предмет: {row[1]}
------------------------------------------
    """

    return s



def get_teacher_info(number):
    file = 'data/teachers.xlsx'

    df = pd.read_excel(file)

    data_list = df.values.tolist()


    for num, row in enumerate(data_list):
        if num+1 == number:
            s = f"""ФИО: {row[0]}
Предмет: {row[1]}
Почта: {row[2]}
{row[3]}
Cсылка на страничку в HSE: {row[4]}
"""

    return s

