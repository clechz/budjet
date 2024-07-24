from datetime import datetime

DATEFORMAT = "%d-%m-%Y"
CATEGORIES = {"i": "Income", "e": "Expense"}

def get_date(prompt, allow_default=False):
    
    date_str = input(prompt)

    #if user didn't give us a date and we are allowing the default
    if allow_default and not date_str:
        return datetime.today().strftime(DATEFORMAT)
    
    else:
        try: 
            valid_date = datetime.strptime(date_str, DATEFORMAT)
            return valid_date
        except ValueError:
            print(f'"{date_str}" IS INVALID. PLEASE ENTETR THE DATE IN dd-mm-yyyy format')
            return get_date(prompt)

def get_amount():
    try:
        amount = float(input("Please enter amount: "))
        if amount <= 0:
            raise ValueError("amount must be more than zero")
            
        return amount
    except ValueError as err:
        print(err)
        return get_amount()


def get_category():
  
    #if ur going to add more valid ctegories in the future plz change the input messege
    category = input("Enter category ('I for income' and 'E for Expense')").lower().replace(" ", "")
    # Note: 'in' checks for keys in the dictionary, use 'in dict.values()' to check for values
    if category not in CATEGORIES:
        print(category+" IS AN  INVALID CATEGORY")
        return get_category()
    else:
        return CATEGORIES[category]
    
def get_description():
     
    return input("Enter a description (Optional) : ")
    