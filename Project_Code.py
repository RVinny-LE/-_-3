from csv import *
from pickle import *


def Loading_Table_Data_CSV():
    '''
    Данная функция загружает данные из csv файла в словарь.

    Разделение - точка с запятой
    Ключи словаря, это заголовки столбцов.
    Значения словаря, это списки данных в столбце.

    Функция возвращает словарь если её работа прошла исправно и None при ошибке.
    '''
    with open('CSV_File.csv', 'r') as Table:        # Открываем файл с помощью конструкции "with ... as", чтобы в дальнейшем не беспокоится о его закрытии. Table - переменная
        
        Reader = reader(Table, delimiter = ';')        # Читаем данные из переменной Table построчно
        Cap = next(Reader)        # Извлекаем строку заголовков
        T_Data = [Elm for Elm in Reader]        # Считываем все остальные строки
        
        Inverted_Lst = []           # Сюда будем добавлять списки значений каждого столбца таблицы
        for Indx in range(len(Cap)):        # Транспонируем нашу матрицу значений. Внешний цикл пройдется по всем столбцам. Внутренний добавит к текущему списку значение соответствующего поля из каждой строки.
            Strings = []
            for Elm in range(len(T_Data)):
                Strings.append(T_Data[Elm][Indx])
            Inverted_Lst.append(Strings)
            
        Dict = {Cap[Num]:Inverted_Lst[Num] for Num in range(len(Cap))}        # Создаем словарь который будет возвращать наша функция
        return Dict

Dict = (Loading_Table_Data_CSV())


def Loading_Table_Data_TXT(Name):
    '''
    Данная функция загружает данные из txt файла в словарь.

    Разделение - табуляция
    Ключи словаря, это заголовки столбцов.
    Значения словаря, это списки данных в столбце.

    Функция возвращает словарь если её работа прошла исправно и None при ошибке.
    '''
    try:        # Обрабатываем исключение потери файла (FileNotFoundError)
        with open(Name, 'r') as f:
            Strings = f.readlines()        # Считываем файл построчно. Возращает список строк. Если список пуст, возвращает None
            if not Strings:
                return None

            Cap = Strings[0].strip().split('\t')        # Считывает первую строчку файла сохраняя ее как заголовки таблицы.
            T_Data = [Str.strip().split('\t') for Str in Strings[1:]]        # Считывает остальные данные

            if not all(len(Row) == len(Cap) for Row in T_Data):        # Сравниваем колличество элементов в каждой строчке с колличеством элементов в шапке таблицы
                print("Ошибка: неправильно заполнена таблица")
                return None


            Output = {Column: [Row[i] for Row in T_Data] for i, Column in enumerate(Cap)}
            return Output
    except FileNotFoundError:
        return(f"Файл '{Name}' не был найден.")


def Save_Table_In_Pickle_Format(Dic):
    '''
    Данная функция преобразует словать в байтовый поток (сереализирует) и сохраняет в файл формата pickle.
    Возвращает файл с байтовой записью словаря.
    '''
    with open('Pickle_File.pickle', 'wb') as File:
        dump(Dic, File)


def Save_Table_In_CSV_Format(Dic):
    '''
    Сохраняем табличку в CSV файле
    '''
    Keys, Value = (Dic.keys()), (Dic.values())
    with open('New_CSV_File.csv', 'w+', newline = '') as Table:
        Writer = writer(Table, delimiter = ';')
        Writer.writerow(Keys)
        Writer.writerows(zip(*Value))


def Output_Rows_By_Number(Name, Dic, Start = 1, Stop = None, Overwriting = False):
    
    try:
        open(Name)
        if Overwriting == True:
            with open('new_' + Name, 'w+', newline = '') as Table:
                Writer = writer(Table, delimiter = ';')
                Writer.writerow(Dic.keys())
                Rows = list(zip(*Dic.values()))
                if Stop is None or Stop > len(Rows):
                    Stop = len(Rows)
                if Stop < 0 or Start < 0:
                    return "Неверный ввод!"
                else:
                    Writer.writerows(Rows[Start - 1:Stop])
        if Overwriting == False:
            with open(Name, 'w+', newline='') as Table:
                Writer = writer(Table, delimiter = ';')
                Writer.writerow(Dic.keys())
                Rows = list(zip(*Dic.values()))
                if Stop is None or Stop > len(Rows):
                    Stop = len(Rows)
                if Stop < 0 or Start < 0:
                    return "Неверный ввод!"
                else:
                    Writer.writerows(Rows[Start - 1:Stop])
    except:
        return "Произошла ошибка при вводе!"


def Output_Rows_By_Index(Name, Dic, *Args, Overwriting = False):
    '''
    Записывает строки, указанные в индексах, в файл CSV.  Обрабатывает недопустимые индексы
    '''
    try:
        open(Name)
        if Overwriting == True:
            with open("new_" + Name, 'w+', newline = '') as Table:
                Writer = writer(Table, delimiter = ';')
                Writer.writerow(Dic.keys())
                Rows = list(zip(*Dic.values()))
                for Index in Args:
                    if Index not in list(range(len(Rows) + 1)[1:]):
                        return "Неверный ввод!"
                    else:
                        Writer.writerow(Rows[Index - 1])
        if Overwriting == False:
            with open(Name, 'w+', newline = '') as Table:
                Writer = writer(Table, delimiter = ';')
                Writer.writerow(Dic.keys())
                Rows = list(zip(*Dic.values()))
                for Index in Args:
                    if Index not in list(range(len(Rows) + 1))[1:]:
                        return "Неверный ввод!"
                    else:
                        Writer.writerow(Rows[Index - 1])
    except:
        return "Произошла ошибка при вводе!"


def Output_Column_Types(Dic, Index, Column = 1):
    '''
    Возвращает тип данных первого элемента в указанном столбце словаря
    '''
    try:
        if Column in Dic.keys():
            Output_Dic = {}
            Output_Dic[list(Dic.keys())[Index - 1]] = type(Dic[list(Dic.keys())[Index - 1]][0])
            return Output_Dic
        if Column in list(range(len(Dic) + 1))[1:]:
            dict_result = {}
            if index in dic.keys():
                dict_result[index] = type(dic[index][0])
            else:
                return "Произошла ошибка при вводе!"
            return dict_result
    except:
        return "Произошла ошибка при вводе!"


def Change_Column_Type(Dic, Type, Index, Column = 1):
    '''
    Меняем тип данных в столбике
    '''
    try:
        if Column in Dic.keys():
            Dic[list(Dic.keys())[Index]] = list(map(Type, Dic[list(Dic.keys())[Index]]))
        if Column in list(range(len(Dic) + 1))[1:]:
            Dic[Index] = list(map(Type, Dic[Index]))
        return "Тип записан!"
    except:
        return "Тип не подходит."


def Output_Values(Dic, Column = 1):
    '''
    Вывод всех значений столбца
    '''
    Output_Lst = []
    try:
        if Column in Dic.keys():
            Output_Lst += Dic[Column]
        else:
            if Column in list(range(len(Dic) + 1))[1:]:
                Output_Lst += list(Dic.values())[Column - 1]
            else:
                return "Произошла ошибка при вводе!"
        return Output_Lst
    except:
        return "Произошла ошибка при вводе!"


def Output_Value(Dic, Column = 1, Row = 1):
    '''
    Выводим одно значение из таблицы
    '''
    try:
        if Column in Dic.keys():
            return Dic[Column][Row - 1]
        if Column in list(range(len(Dic) + 1))[1:]:
            return list(Dic.values())[Column - 1][Row - 1]
        else:
            return "Произошла ошибка при вводе!"
    except:
        return "Произошла ошибка при вводе!"


def Change_Values(Dic, Values, Column = 1):
    '''
    Заменяет значения в указанном столбце на значения из предоставленного списка.  Обрабатывает спецификацию столбца по индексу или имени.
    '''
    try:
        if Column in Dic.keys():
            Dic[Column] = Values
            return Dic
        else:
            if Column in list(range(len(Dic) + 1))[1:]:
                Dic[list(Dic.keys())[Column - 1]] = Values
                return Dic
            else:
                return "Произошла ошибка при вводе!"
    except:
        return "Произошла ошибка при вводе!"


def Change_Value(Dic, Value, Column = 1, Row = 1):
    '''
    Заменяем значение в таблице
    '''
    try:
        if Column in Dic.keys():
            Dic[Column][Row - 1] = Value
            return Dic
        else:
            if column in list(range(len(Dic) + 1))[1:]:
                Dic[list(Dic.keys())[Column - 1]][Row - 1] = Value
                return Dic
            else:
                return "Произошла ошибка при вводе!"
    except:
        return "Произошла ошибка при вводе!"


def Output_Table(Dic):
    print(*Dic.keys())
    for T_Data in Dic.values():
        print(*T_Data)
