import os
import sys

import pandas as pd


class Combiner:
    def __init__(self, chunk_size=1000000):
        self.CHUNK_SIZE = chunk_size  # set chunk size to avoid out of memory error

    def check_csv_filepaths(self, csv_filepath_list):
        """
        Check if input csv filepaths valid or not

        :param csv_filepath_list: a list of csv filepath
        :return:
        """
        if len(csv_filepath_list) == 0:
            raise FileNotFoundError('Input Error: Please input csv filepath(s).')
        for filepath in csv_filepath_list:
            if not filepath.endswith('.csv'):
                raise FileNotFoundError('Input Error: The input file {} is not a csv file.'.format(filepath))
            elif not os.path.exists(filepath):
                raise FileNotFoundError('Input Error: The input file {} does not exist.'.format(filepath))

    def combine_csv_files(self, csv_filepath_list):
        """
        Combine the input csv files into one file and output it to the sys.stdout

        :param csv_filepath_list: a list of csv filepath
        :return:
        """
        self.check_csv_filepaths(csv_filepath_list)
        header = True
        for filepath in csv_filepath_list:
            df_chunks = pd.read_csv(filepath, chunksize=self.CHUNK_SIZE)
            for chunk in df_chunks:
                chunk['filepath'] = filepath.split('/')[-1]
                chunk.to_csv(sys.stdout, index=False, header=header)
                if header:
                    header = False


if __name__ == '__main__':
    csv_filepath_list = []
    for filepath in sys.argv[1:]:
        csv_filepath_list.append(filepath)

    combiner = Combiner(chunk_size=1000000)
    combiner.combine_csv_files(csv_filepath_list)


