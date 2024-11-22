import pandas as pd
import numpy as np

# Загрузка данных из двух документов
df1 = pd.read_excel('../нб.xlsx')
df2 = pd.read_excel('../check.xlsx', engine='openpyxl')

# Группировка первого DataFrame по Unit ID
grouped = df1.groupby('Unit ID')

# Определяем индексы столбцов для каждой группы
group_1_columns = ['т1', 'т1.1', 'т1.2']  # Первая группа (т1)
group_2_columns = ['п2', 'п2.1', 'п2.2', 'п2.3', 'п2.4', 'п2.5', 'п2.6', 'п2.7', 'п2.8', 'т2',
                   'т2.1', 'т2.2']  # Вторая группа (п2, т2)
group_3_columns = ['п3', 'п3.1', 'п3.2', 'п3.3', 'п3.4', 'т3']  # Третья группа (п3, т3)
group_4_columns = ['п4', 'п4.1', 'п4.2', 'п4.3', 'п4.4', 'т4']  # Четвертая группа (п4, т4)

# Проход по каждой группе
for unit_id, group in grouped:
    print(f"Processing Unit ID: {unit_id}")

    # Найдем строку с данным Unit ID во втором DataFrame
    matching_row = df2.loc[df2['Unit ID'] == unit_id]

    if not matching_row.empty:
        # Получаем список количества удаляемых значений "нб" для каждой группы
        attendance_touches = matching_row['attendance_touch'].values  # Получаем все числа после Unit ID

        column_indices = list(range(3, len(group.columns)))
        # Случайный выбор индексов для замены "нб" в каждой группе
        # Первая группа: т1
        group_1_indices = [group.columns.get_loc(col) for col in group_1_columns]
        group_2_indices = [group.columns.get_loc(col) for col in group_2_columns]
        group_3_indices = [group.columns.get_loc(col) for col in group_3_columns]
        group_4_indices = [group.columns.get_loc(col) for col in group_4_columns]

        # Случайный выбор индексов для замены "нб" в каждой группе
        # Первая группа: т1
        t1_indices = np.random.choice(group_1_indices, size=min(int(attendance_touches[0]), len(group_1_indices)),
                                      replace=False).tolist()

        # Вторая группа: п2 и т2
        p2_t2_indices = np.random.choice(group_2_indices, size=min(int(attendance_touches[1]), len(group_2_indices)),
                                         replace=False).tolist()

        # Третья группа: п3 и т3
        p3_t3_indices = np.random.choice(group_3_indices, size=min(int(attendance_touches[2]), len(group_3_indices)),
                                         replace=False).tolist()

        # Четвертая группа: п4 и т4
        p4_t4_indices = np.random.choice(group_4_indices, size=min(int(attendance_touches[3]), len(group_4_indices)),
                                         replace=False).tolist()

        # Замена "нб" на пробелы в соответствующих столбцах
        for i, row in group.iterrows():
            row_list = list(row)  # Преобразуем строку в список для изменения
            print(f"Processing row {i}, row data: {row_list}")

            print(f"Checking columns in t1_indices: {t1_indices}")
            for col_index in t1_indices:  # Идем по столбцам, которые указаны в t1_indices
                if row_list[col_index] == 'нб':
                    print(f"Changing 'нб' to ' ' at column index {col_index}")
                    row_list[col_index] = ' '

            # Вторая группа: п2 и т2
            print(f"Checking columns in p2_t2_indices: {p2_t2_indices}")
            for col_index in p2_t2_indices:  # Идем по столбцам для второй группы
                if row_list[col_index] == 'нб':
                    print(f"Changing 'нб' to ' ' at column index {col_index}")
                    row_list[col_index] = ' '

            # Третья группа: п3 и т3
            print(f"Checking columns in p3_t3_indices: {p3_t3_indices}")
            for col_index in p3_t3_indices:  # Идем по столбцам для третьей группы
                if row_list[col_index] == 'нб':
                    print(f"Changing 'нб' to ' ' at column index {col_index}")
                    row_list[col_index] = ' '

            # Четвертая группа: п4 и т4
            print(f"Checking columns in p4_t4_indices: {p4_t4_indices}")
            for col_index in p4_t4_indices:  # Идем по столбцам для четвертой группы
                if row_list[col_index] == 'нб':
                    print(f"Changing 'нб' to ' ' at column index {col_index}")
                    row_list[col_index] = ' '

            # Применение измененной строки обратно в DataFrame
            group.loc[i] = row_list

        # Замена модифицированной группы в исходном DataFrame
        df1.loc[df1['Unit ID'] == unit_id] = group
    else:
        print(f"No matching row found in df2 for Unit ID: {unit_id}")

# Сохранение модифицированного DataFrame в новый Excel файл
df1.to_excel('../Модифицированный журнал посещаемости.xlsx', index=False)
print("Модифицированный журнал посещаемости сохранен.")
