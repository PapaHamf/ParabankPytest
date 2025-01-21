import openpyxl
from openpyxl.workbook import Workbook


class ExcelData():

    @staticmethod
    def get_excel_data(file_name: str, sheet_name: str = None) -> list [dict]:
        """
        Returns the data from the Excel file as a dictionary.
        The first row should contain the column names used for the
        dictionary keys.
        :param file_name: Filename of the Excel file.
        :param sheet_name:  Let's you select the sheet in the workbook.
        :return: List of dictionaries w/ data.
        """
        book = openpyxl.load_workbook(f"../testdata/{file_name}")
        if sheet_name:
            sheet = book[sheet_name]
        else:
            sheet = book.active
        # Declaring temporary list
        excel_data: list = []
        # Reading the data
        for row in range(2, sheet.max_row+1):
            temp_dict: dict = {}
            for column in range(1, sheet.max_column+1):
                temp_dict[sheet.cell(row = 1, column = column).value] = sheet.cell(row = row, column = column).value
            excel_data.append(temp_dict)
        return excel_data


    @staticmethod
    def save_excel_data(file_name: str, data: list [dict]) -> None:
        """
        Lets you save the formatted data to the Excel file. The first row
        will contain the column names used for the dictionary keys.
        :param file_name: Filename of the Excel file
        :param data: List of lists containing the data to be written. First list should
        should contain the table headers.
        :return:
        """
        book = Workbook()
        sheet = book.active
        sheet.title = "Data"
        # Adding the header w/ column names
        column_names = data[0].keys()
        for key, name in enumerate(column_names, 1):
            sheet.column_dimensions[sheet.cell(row = 1, column = key).column_letter].width = 30
            sheet.cell(row = 1, column = key).value = name
        # Adding the data in rows
        for r_key, row in enumerate(data, 1):
            values: list = list(row.values())
            for c_key, column in enumerate(row, 1):
                sheet.cell(row = r_key + 1, column = c_key).value = values[c_key - 1]
        # Saving the file
        # book.save(f"../testdata/{file_name}")
        book.save(f"./{file_name}")