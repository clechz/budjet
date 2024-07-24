import pandas as pd
import csv
from datetime import datetime
from data import *

class CSV:
    csv_file = "finance_data.csv"
    columns = ["date", "amount", "category", "description"]
    
    #opens a csv file with the desired categories if there is'nt one already
    @classmethod
    def init_csv(cls):

        try:
            pd.read_csv(cls.csv_file)

        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.columns)
            df.to_csv(cls.csv_file, index=False)


    @classmethod
    def add(cls, date, amount, category, description):
        #creates dict to add into csv
        new = {
            "date": date,
            "amount": amount,
            "category": category,
            'description': description
        }

        #opens csv file and writes the dict into it
        with open(cls.csv_file, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.columns)
            writer.writerow(new)
        print(" Entry added successfuly")

def prompt_user():
    #ensures there is a dict already
    CSV.init_csv()
    #different columns prompts
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or enter for todays date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    #opens csv file and writes the dict into it
    CSV.add(date, amount, category, description)


prompt_user()