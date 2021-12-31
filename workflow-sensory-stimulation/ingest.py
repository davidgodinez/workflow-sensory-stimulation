import pathlib
import csv
from datetime import datetime

from .pipeline import subject
from .paths import get_sensory_root_data_dir


def ingest_subjects(subject_csv_path='./user_data/subjects.csv'):
    # -------------- Insert new "Subject" --------------
    with open(subject_csv_path, newline= '') as f:
        input_subjects = list(csv.DictReader(f, delimiter=','))

    print(f'\n---- Insert {len(input_subjects)} entry(s) into subject.Subject ----')
    subject.Subject.insert(input_subjects, skip_duplicates=True)

    print('\n---- Successfully completed ingest_subjects ----')

#TODO add ingest_sessions