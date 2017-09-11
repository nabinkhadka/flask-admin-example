import os

import time
import pandas as pd
from app import db, app, models


class CSVHandler(object):
    """
        Handles GBs of data in chunk
    """
    fields = ['name', 'last_name', 'address', 'gender']

    def __init__(self, file_name, chunk_size=1000):
        self.file_name = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
        self.chunk_size = chunk_size

    def read(self):

        for df in pd.read_csv(
                self.file_name,
                skipinitialspace=True,
                chunksize=self.chunk_size,
                iterator=True,
                low_memory=False,
                usecols=self.fields
        ):
            rows = df.get_values()
            for row in rows.tolist():
                name = row[0]
                last_name = row[1]
                address = row[2]
                gender = row[3]
                student = models.Student(name, gender, address, last_name)
                db.session.add(student)
            db.session.commit()

    def insert(self):
        pass

if __name__ == '__main__':
    handler = CSVHandler('~/Downloads/huge.csv', 1000)
    handler.read()
