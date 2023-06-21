"""
This is supporting class modules for files management:
    - Read/Write and load data
    - Refresh the data
Date created: 31-Aug-2022
Originator: anhvtFX17909
"""
import os


class File:
    #   Initiate the file class to manage file data:
    #   > Location
    #   > File name
    #   > Data loaded to program
    def __init__(self, cw_dir=None):
        if not cw_dir:
            cw_dir = os.getcwd()
        else:
            self.cw_dir = cw_dir

    # this module to convert the ID to an index for sorting the dataset
    def f_read(self):
        """
        :input: None - file data in the class
        :return: data from file ['id, name, DOB, birth place']
        """
        # initiate an array of input data
        try:
            f = open(self.cw_dir, 'r')
            f_data = f.read().splitlines()

            # Check if the file is empty or not. If the file is empty >> remind to add values
            if not f_data:  # IsEmpty!
                print('File empty! >>')
                return
            else:
                # return a list of data
                f_data_converted = self.convert(f_data[1:])
                return f_data_converted
        except IOError:
            print('Error: Unable to open file! Please try again')
            return
        f.close()

    def f_write_sdata(self, new_data):
        """
        :param new_data: for assignment 2, the data shall be an array
        :return: the file with array stored inside
        """
        try:
            f = open(self.cw_dir, 'a')
            f.write(f'{new_data}\n')
            f.close()
            print(f'Write to file asm2_data.csv successfully')
        except IOError:
            print('Unable to write to file')

    def convert(self, data):
        data_converted = []
        for i in data:
            id, name, bplace, dob = i.split(',')
            idx = int(id)
            data_converted.append([idx, name, bplace, dob])
        return data_converted

