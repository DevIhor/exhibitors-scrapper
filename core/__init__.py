import csv
import os
from typing import Dict, List

FILE_NAME = 'exhibitors.csv'
FIELD_NAMES = ['company', 'site', 'decision_maker', 'person_role', 'person_linkedin', 'description']


def prepare_writer() -> None:
    """
    Prepare file to write data
    """
    if os.path.isfile(FILE_NAME):
        return
    with open(FILE_NAME, mode='w') as exhibitors_file:
        fieldnames = FIELD_NAMES
        writer = csv.DictWriter(exhibitors_file, fieldnames=fieldnames)
        writer.writeheader()


def write_data(
        data: Dict[str, str]
) -> None:
    """
    Writes exhibitors data to the file
    """
    with open(FILE_NAME, mode='a') as exhibitors_file:
        fieldnames = FIELD_NAMES
        writer = csv.DictWriter(exhibitors_file, fieldnames=fieldnames)
        writer.writerow(data)


def get_companies() -> List[str]:
    """
    Prepare file to write data
    """
    companies = []
    with open(FILE_NAME, mode='r') as exhibitors_file:
        fieldnames = FIELD_NAMES
        reader = csv.DictReader(exhibitors_file, fieldnames=fieldnames)
        for row in reader:
            companies.append(row['company'])
    return companies
