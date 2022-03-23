from salary import calculate_salary
from db.people import get_employees
from datetime import datetime as dt


if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print(dt.now())
