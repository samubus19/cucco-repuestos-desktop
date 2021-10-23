from datetime import date, datetime

def formatearFecha(date_str):
    date_obj = datetime.strptime(date_str.split("T")[0], "%Y-%m-%d")
    return datetime.strftime(date_obj, '%d-%m-%Y')