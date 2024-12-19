import csv
import pickle

def load_table():
    """
    .. function:: load_table()

   Loads data from telephones.csv into a dictionary.

   :returns: Dictionary: keys are column headers, values are column data lists.  Returns None on error.
   :rtype: dict or None

   Reads data from 'telephones.csv' (semicolon delimited).
   Each key is a column header, and its value is a list of that column's entries.

   :raises FileNotFoundError: File not found.
   :raises csv.Error: CSV parsing error.
   :raises Exception: Other errors.
    """
    with open('telephones.csv', 'r') as table:
        reader = csv.reader(table, delimiter=';')
        head = next(reader)
        strings = [el for el in reader]
        lst_res = []
        for ind in range(len(head)):
            strs = []
            for el in range(len(strings)):
                strs.append(strings[el][ind])
            lst_res.append(strs)
        dic = {head[num]:lst_res[num] for num in range(len(head))}
        return dic

# print(load_table())
dic = (load_table())


def load_table_txt(filename):
    """
    .. function:: load_table_txt(filename)

   Loads data from a tab-separated TXT file.

   :param filename: TXT file path.
   :type filename: str
   :returns: Dictionary: column headers as keys, column data as lists; or None on error.
   :rtype: dict or None

   Reads a TXT file (tab-delimited). First row is the header.

   :raises FileNotFoundError: File not found.
   :raises ValueError: Inconsistent column counts.
   :raises Exception: Other errors.
    """
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            if not lines:  # Handle empty file
                return None

            header = lines[0].strip().split('\t')
            data = [line.strip().split('\t') for line in lines[1:]]

            #Check for consistent number of columns
            if not all(len(row) == len(header) for row in data):
                print("Error: Inconsistent number of columns in the file.")
                return None


            result = {col: [row[i] for row in data] for i, col in enumerate(header)}
            return result
    except FileNotFoundError:
        return(f"File '{filename}' not found.")

# print(load_table_txt('телефоны.txt'))

def save_table_pickle(dic):
    """
    .. function:: save_table_pickle(dic)

   Saves a dictionary to a pickle file.

   :param dic: The dictionary to be saved.
   :type dic: dict
   :raises Exception: If an error occurs during file writing (e.g., permission issues, disk full).
    """
    with open('telephones.pickle', 'wb') as f:
        pickle.dump(dic, f)

print(save_table_pickle(dic))


def save_table(dic):
    """
    .. function:: save_table(dic)

   Saves a dictionary to a CSV file.

   :param dic: Dictionary to save. Keys become column headers, values become column data.
   :type dic: dict
   :raises Exception: If an error occurs during file writing.
    """
    keys, val = (dic.keys()), (dic.values())
    with open('new_telephones.csv', 'w+', newline='') as table:
        writer = csv.writer(table, delimiter=';')
        writer.writerow(keys)
        writer.writerows(zip(*val))

# print(save_table(load_table()))


def get_rows_by_number(name_file, dic, start=1, stop=None, copy_table=False):
    """
    .. function:: get_rows_by_number(name_file, dic, start=1, stop=None, copy_table=False)

   Writes selected rows from a dictionary to a CSV file.

   :param name_file: Name of the CSV file (existing file is overwritten if copy_table is False).
   :type name_file: str
   :param dic: Dictionary containing data to write (keys are headers).
   :type dic: dict
   :param start: Starting row number (1-based index). Defaults to 1.
   :type start: int
   :param stop: Ending row number (1-based index). Defaults to the last row.
   :type stop: int or None
   :param copy_table: If True, creates a new file ("new_" + name_file); otherwise, overwrites the existing file. Defaults to False.
   :type copy_table: bool
   :returns: "Success!" on success, error message on failure.
   :rtype: str

   Writes rows [start:stop] from the dictionary to the specified file.  Handles invalid start/stop values.

   :raises Exception: If file operations fail.
    """
    try:
        open(name_file)
        if copy_table == True:
            with open("new_" + name_file, 'w+', newline="") as table:
                writer = csv.writer(table, delimiter=';')
                writer.writerow(dic.keys())
                rows = list(zip(*dic.values()))
                if stop is None or stop > len(rows):
                    stop = len(rows)
                if stop < 0 or start < 0:
                    return "Неверный ввод!"
                else:
                    writer.writerows(rows[start - 1:stop])
        if copy_table == False:
            with open(name_file, 'w+', newline="") as table:
                writer = csv.writer(table, delimiter=';')
                writer.writerow(dic.keys())
                rows = list(zip(*dic.values()))
                if stop is None or stop > len(rows):
                    stop = len(rows)
                if stop < 0 or start < 0:
                    return "Неверный ввод!"
                else:
                    writer.writerows(rows[start - 1:stop])
    except:
        return "Произошла ошибка при вводе!"

# print(get_rows_by_number('telephones.csv', dic, 1, 3, copy_table=True))


def get_rows_by_index(name_file, dic, *args, copy_table=False):
    """
    .. function:: get_rows_by_index(name_file, dic, *args, copy_table=False)

   Writes specified rows from a dictionary to a CSV file.

   :param name_file: Name of the CSV file.
   :type name_file: str
   :param dic: Dictionary containing data; keys are headers, values are lists of data.
   :type dic: dict
   :param \*args: Variable number of row indices (1-based) to write.
   :type \*args: int
   :param copy_table: If True, creates a new file ("new_" + name_file); otherwise, overwrites the existing file. Defaults to False.
   :type copy_table: bool
   :returns: "Success!" or an error message.
   :rtype: str

   Writes the rows specified by indices to the CSV file.  Handles invalid indices.

   :raises Exception: If file operations fail.
    """
    try:
        open(name_file)
        if copy_table == True:
            with open("new_" + name_file, 'w+', newline="") as table:
                writer = csv.writer(table, delimiter=';')
                writer.writerow(dic.keys())
                rows = list(zip(*dic.values()))
                for index in args:
                    if index not in list(range(len(rows) + 1)[1:]):
                        return "Неверный ввод!"
                    else:
                        writer.writerow(rows[index - 1])
        if copy_table == False:
            with open(name_file, 'w+', newline="") as table:
                writer = csv.writer(table, delimiter=';')
                writer.writerow(dic.keys())
                rows = list(zip(*dic.values()))
                for index in args:
                    if index not in list(range(len(rows) + 1))[1:]:
                        return "Неверный ввод!"
                    else:
                        writer.writerow(rows[index - 1])
    except:
        return "Произошла ошибка при вводе!"

# get_rows_by_index("telephones.csv", dic, 1, 3, 4, copy_table=True)


def get_column_types(dic, index, by_number=True):
    """
    .. function:: get_column_types(dic, index, by_number=True)

   Returns the data type of the first element in a specified column of a dictionary.

   :param dic: Dictionary where keys are column names and values are lists of data.
   :type dic: dict
   :param index: Column index (1-based if by_number is True; column name if by_number is False).
   :type index: int or str
   :param by_number: If True, index refers to column number; if False, index refers to column name. Defaults to True.
   :type by_number: bool
   :returns: Dictionary containing column name and data type, or an error message.
   :rtype: dict or str


   :raises Exception: If an error occurs (e.g., invalid index).
    """
    try:
        if by_number == True:
            dict_result = {}
            dict_result[list(dic.keys())[index - 1]] = type(dic[list(dic.keys())[index - 1]][0])
            return dict_result
        if by_number == False:
            dict_result = {}
            if index in dic.keys():
                dict_result[index] = type(dic[index][0])
            else:
                return "Произошла ошибка при вводе!"
            return dict_result
    except:
        return "Произошла ошибка при вводе!"

# print(get_column_types(dic, 4))


def set_column_types(dic, type, index, by_number=True):
    """
    .. function:: set_column_types(dic, type, index, by_number=True)

   Attempts to convert the data type of a specified column in a dictionary.

   :param dic: The dictionary to modify; keys are column headers, values are lists of data.
   :type dic: dict
   :param type: The target data type (e.g., int, float, str).
   :type type: type
   :param index: The column index (1-based if by_number is True, column name if False).
   :type index: int or str
   :param by_number: If True, index is a column number; if False, index is a column name. Defaults to True.
   :type by_number: bool
   :returns: "Тип записан!" on success, "Тип не подходит." on failure.
   :rtype: str

   Converts data in the specified column to the target type using `map`.  Returns an error message if conversion fails for any element.

   :raises Exception: If the index is invalid or if a type conversion error occurs.
    """
    try:
        if by_number == True:
            dic[list(dic.keys())[index]] = list(map(type, dic[list(dic.keys())[index]]))
        if by_number == False:
            dic[index] = list(map(type, dic[index]))
        return "Тип записан!"
    except:
        return "Тип не подходит."

# print(set_column_types(dic, int, 1))


def get_values(dic, column=1):
    """
    .. function:: get_values(dic, column=1)

   Retrieves values from a specified column in a dictionary.

   :param dic: The input dictionary. Keys are column headers, values are data lists.
   :type dic: dict
   :param column: The column to retrieve (1-based index or column name). Defaults to 1.
   :type column: int or str
   :returns: A list of values from the specified column, or an error message.
   :rtype: list or str

   If `column` is an integer, it's treated as a 1-based index. If it's a string, it's treated as a column name.  Returns an error if the column is not found.

   :raises Exception: If an error occurs during data retrieval.
    """
    lst_result = []
    try:
        if column in dic.keys():
            lst_result += dic[column]
        else:
            if column in list(range(len(dic) + 1))[1:]:
                lst_result += list(dic.values())[column - 1]
            else:
                return "Произошла ошибка при вводе!"
        return lst_result
    except:
        return "Произошла ошибка при вводе!"

# print(get_values(dic, column=1))



def get_value(dic, column=1, row=1):
    """
    .. function:: get_value(dic, column=1, row=1)

   Retrieves a single value from a dictionary.

   :param dic: The input dictionary.  Keys are column headers, values are lists of data.
   :type dic: dict
   :param column: The column index (1-based integer) or column name to retrieve from. Defaults to 1.
   :type column: int or str
   :param row: The row index (1-based integer) to retrieve from. Defaults to 1.
   :type row: int
   :returns: The value at the specified column and row, or an error message.
   :rtype: any or str

   Retrieves a single value using either a column name or a 1-based column index and a 1-based row index. Returns an error if the column or row index is invalid.


   :raises Exception: If the column or row index is out of range or if there's an error during data access.
    """
    try:
        if column in dic.keys():
            return dic[column][row - 1]
        if column in list(range(len(dic) + 1))[1:]:
            return list(dic.values())[column - 1][row - 1]
        else:
            return "Произошла ошибка при вводе!"
    except:
        return "Произошла ошибка при вводе!"

# print(get_value(dic, column="цвет", row=2))


def set_values(dic, values, column=1):
    """
    .. function:: set_values(dic, values, column=1)

   Sets the values of a specified column in a dictionary.

   :param dic: The input dictionary. Keys are column headers, values are lists.
   :type dic: dict
   :param values: The new list of values to set for the column.
   :type values: list
   :param column: The column index (1-based integer) or column name to modify. Defaults to 1.
   :type column: int or str
   :returns: The modified dictionary or an error message.
   :rtype: dict or str

   Replaces the values in the specified column with the provided list.  Handles column specification by index or name.

   :raises Exception: If the column index or name is invalid, or if there is an error during value assignment.
    """
    try:
        if column in dic.keys():
            dic[column] = values
            return dic
        else:
            if column in list(range(len(dic) + 1))[1:]:
                dic[list(dic.keys())[column - 1]] = values
                return dic
            else:
                return "Произошла ошибка при вводе!"
    except:
        return "Произошла ошибка при вводе!"

# print(set_values(dic, [1000, 2000, 3000, 4000], column=2))


def set_value(dic, value, column=1, row=1):
    """
    .. function:: set_value(dic, value, column=1, row=1)

   Sets a single value in a dictionary.

   :param dic: The input dictionary. Keys are column headers, values are lists of data.
   :type dic: dict
   :param value: The new value to set.
   :type value: any
   :param column: The column index (1-based integer) or column name. Defaults to 1.
   :type column: int or str
   :param row: The row index (1-based integer). Defaults to 1.
   :type row: int
   :returns: The modified dictionary or an error message.
   :rtype: dict or str

   Sets the value at the specified row and column.  Handles column specification by index or name.
   Returns an error message if the indices are out of bounds.

   :raises Exception: If the column or row index is invalid or if there's an error during value assignment.
    """
    try:
        if column in dic.keys():
            dic[column][row - 1] = value
            return dic
        else:
            if column in list(range(len(dic) + 1))[1:]:
                dic[list(dic.keys())[column - 1]][row - 1] = value
                return dic
            else:
                return "Произошла ошибка при вводе!"
    except:
        return "Произошла ошибка при вводе!"

# print(set_value(dic, 'СИНИЙ', "цвет", 2))


def print_table(dic):
    """
    .. function:: print_table(dic)

   Prints a dictionary's contents in a tabular format.

   :param dic: The dictionary to print. Keys represent column headers; values are lists representing rows.
   :type dic: dict

   Prints the dictionary's keys as a header row, followed by each row of data.
   Assumes all value lists have the same length.
    """
    print(*dic.keys())
    for data in dic.values():
        print(*data)

# print(print_table(dic))
