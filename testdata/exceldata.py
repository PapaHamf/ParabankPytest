import openpyxl

class ExcelData():

    @staticmethod
    def get_excel_data(file_name: str, sheet_name: str = "All") -> dict:
        """
        Returns the data from the Excel file as a dictionary.
        :param file_name: Filename of the Excel file.
        :param sheet_name:  Let's you select the sheet in the workbook.
        :return: List of dictionaries w/ data.
        """
        book = openpyxl.load_workbook(f"../{file_name}")
        sheet = book.wb[sheet_name]
        excel_data: list = []

