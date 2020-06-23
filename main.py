

import datetime

import application.salary
import application.db.people

now = datetime.datetime.now()
print(f"текущая дата {now.day}/{now.month}/{now.year}")


if __name__ == '__main__':
    application.salary.calculate_salary()
    application.db.people.get_employees()

