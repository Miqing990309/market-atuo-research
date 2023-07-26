import os
# import xlsxwriter module
import xlsxwriter

directory = "output"

def createSheet(name):
    # Workbook() takes one, non-optional, argument
    # which is the filename that we want to create.
    workbook = xlsxwriter.Workbook(name)

    # The workbook object is then used to add new
    # worksheet via the add_worksheet() method.
    worksheet = workbook.add_worksheet()

    # Use the worksheet object to write
    # data via the write() method.
    worksheet.write('A1', 'Hello..')
    worksheet.write('B1', 'Geeks')
    worksheet.write('C1', 'For')
    worksheet.write('D1', 'Geeks')

    # Finally, close the Excel file
    # via the close() method.
    workbook.close()

def main():
    # current dir
    current_path = os.getcwd()
    # parent_dir = os.path.abspath(os.path.join(current_path, os.pardir))
    # Path
    path = os.path.join(current_path, directory)
    if not os.path.exists(path):
        os.mkdir(path)



if __name__ == '__main__':
    main()

