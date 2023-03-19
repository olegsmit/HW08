from datetime import datetime, timedelta


users = [{"name": "Vasya", "birthday": "20.03.2000"},
         {"name": "Tanya", "birthday": "22.03.2000"},
         {"name": "Ylya", "birthday": "27.03.2000"},
         {"name": "Petya", "birthday": "25.03.2000"},
         {"name": "Sergey", "birthday": "19.03.2000"},
         {"name": "Denis", "birthday": "24.03.2000"},
         {"name": "Alex", "birthday": "18.03.2000"},
         {"name": "Anatoliy", "birthday": "24.03.2000"},
         {"name": "Olena", "birthday": "15.03.2000"},
         {"name": "Daria", "birthday": "21.03.2000"},
         {"name": "Alona", "birthday": "17.03.2000"},
         {"name": "Ihor", "birthday": "21.03.2000"}]


def get_birthdays_per_week(users):
    days_week = {"Monday": [],
                 "Tuesday": [],
                 "Wednesday": [],
                 "Thursday": [],
                 "Friday": []}

    today = datetime.now().date()

    for user in users:
        bth = datetime.strptime(user.get("birthday"), "%d.%m.%Y")
        btn_this_year = bth.replace(year=today.year).date()
        diff = btn_this_year - today
        if timedelta(-2) <= diff <= timedelta(4):
            days = datetime.weekday(btn_this_year)
            if days == 0 or days >= 5:
                days_week["Monday"].append(user["name"] + ' ' + str(bth.day) + '/' + str(bth.month))
            else:
                days_week[btn_this_year.strftime("%A")].append(user["name"] + ' ' + str(bth.day) + '/' + str(bth.month))


    for day, bth in days_week.items():
        if not bth:
            continue
        else:
            name_btn = ', '.join(bth)
            print(f'{day}: {name_btn}')


if __name__ == '__main__':

    get_birthdays_per_week(users)