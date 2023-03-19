from datetime import datetime, timedelta

users = [{"name": "Vasya", "birthday": "2000-03-20"},
         {"name": "Tanya", "birthday": "2000-03-22"},
         {"name": "Ylya", "birthday": "2000-03-27"},
         {"name": "Petya", "birthday": "2000-03-25"},
         {"name": "Sergey", "birthday": "2000-03-19"},
         {"name": "Denis", "birthday": "2000-03-24"},
         {"name": "Alex", "birthday": "2000-03-18"},
         {"name": "Anatoliy", "birthday": "2000-03-24"},
         {"name": "Olena", "birthday": "2000-03-15"},
         {"name": "Daria", "birthday": "2000-03-21"},
         {"name": "Alona", "birthday": "2000-03-17"},
         {"name": "Ihor", "birthday": "2000-03-31"}]
weeks_day = {"Monday": [],
             "Tuesday": [],
             "Wednesday": [],
             "Thursday": [],
             "Friday": []}

def get_birthdays_per_week(users: list) -> None:

    today = datetime.now().date()
    day_of_week = today.weekday()
    next_monday = (today + timedelta(days=7 - day_of_week))
    next_friday = (today + timedelta(days=11 - day_of_week))
    last_saturday = (next_monday - timedelta(days=2))

    for user in users:
        user_date = user['birthday'].split('-')
        bth_date = datetime(year=today.year, month=int(user_date[1]), day=int(user_date[2])).date()
        
        if last_saturday <= bth_date < next_monday:
            weeks_day['Monday'].append(user['name'] + ' ' + user_date[1] + '/' + user_date[2])
        elif next_monday <= bth_date <= next_friday:
            weeks_day[bth_date.strftime('%A')].append(user['name'] + ' ' + user_date[1] + '/' + user_date[2])
            
    for day, bth in weeks_day.items():
        
        if not bth:
            continue
        else:
            print_n_b = ', '.join(bth)
            print(f"{day}: {print_n_b}.")


if __name__ == "__main__":
    print("Don't forget to congratulate:\n")
    get_birthdays_per_week(users)
