import random
import string
from datetime import datetime, timedelta

from db_handler import *


def combine(*args):
    l = list(args)
    if isinstance(l[0], str) | isinstance(l[0], datetime):
        l[0] = '\'' + str(l[0]) + '\''
    result = str(l[0])
    for i in range(1, len(args)):
        if isinstance(l[i], str) | isinstance(l[i], datetime):
            l[i] = '\'' + str(l[i]) + '\''
        result += ', ' + str(l[i])
    return result


def sampling(db):
    # plug_type table
    types = ["type 1", "type 2", "combination", "CHAdeMO", "tesla"]
    sizes = [1, 2, 3, 4]
    shapes = ["square", "rectangle"]
    for i in range(0, 10):
        r_type = random.choice(types)
        r_size = random.choice(sizes)
        r_shape = random.choice(shapes)
        db.insert('plug_type', 'name,size,shape', combine(r_type, r_size, r_shape))

    # car_type table
    class_types = ["business", "economy"]
    num_of_seats = [2, 4, 6]
    plug_compatibility = list(range(1, 11))
    for i in range(0, 10):
        r_class = random.choice(class_types)
        r_seats = random.choice(num_of_seats)
        r_plug = random.choice(plug_compatibility)
        db.insert('car_type', 'class,num_of_seats,plug_compat', combine(r_class, r_seats, r_plug))

    # car table
    type_id = list(range(1, 11))
    color = ["red", "blue", "white", "black"]
    baby_seat = [0, 1]
    charge_level = list(range(0, 101, 10))
    availability = ["charging", "on order", "repairing", "damaged", "idle"]
    check_success = [0, 1]
    prices = [round(random.uniform(1.00, 2.00), 2) for _ in range(0, 10)]
    for i in range(0, 10):
        r_type_id = random.choice(type_id)
        license_plate = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
        r_color = random.choice(color)
        r_baby = random.choice(baby_seat)
        r_charge = random.choice(charge_level)
        r_avail = random.choice(availability)
        r_check = random.choice(check_success)
        r_price = prices[i]
        db.insert('car', 'TYPE_ID,license_plate,color,baby_seat,charge_level,availability,check_success,price_per_km', combine(
            r_type_id, license_plate, r_color, r_baby, r_charge, r_avail, r_check, r_price
        ))

    # charging_station table
    cost_per_kw = [round(random.uniform(0.30, 1.20), 3) for _ in range(10)]
    num_of_sockets = list(range(1, 10))
    latitude = [25.339403, 57.643522, 54.342321, 43.349342]
    longitude = [-24.434322, -52.343411, -76.532113, -74.834881]
    for i in range(0, 10):
        r_cost = random.choice(cost_per_kw)
        r_num = random.choice(num_of_sockets)
        r_avail_socket = r_num - 1
        r_latitude = random.choice(latitude)
        r_longitude = random.choice(longitude)
        db.insert('charging_station', 'cost_per_kw,num_of_sockets,num_of_available_sockets,latitude,longitude', combine(
            r_cost, r_num, r_avail_socket, r_latitude, r_longitude
        ))

    # charging_order table
    car_id = list(range(1, 11))
    charging_station_id = list(range(1, 11))
    for i in range(0, 10):
        r_cid = random.choice(car_id)
        r_csid = random.choice(charging_station_id)
        date1, date2 = two_random_dates()
        print(date1)
        print(date2)
        db.insert('charging_order', 'start_time,end_time,car_id,cs_id', combine(date1, date2, r_cid, r_csid))

    # provider
    name = ["Company 1", "Company 2", "Company 3", "Company 4"]
    for i in range(0, 4):
        r_name = name[i]
        phone_num = random_phone()
        db.insert('provider', 'name,phone_num', combine(r_name, phone_num))

    # provider_location
    # yeah, i understand it is silly, but just for the sake of simplicity
    country = ["Australia", "Japan", "China", "Germany"]
    city = ["Bern", "Bratislava", "Luxembourg", "Laos"]
    street = ["Piccadilly", "Main St.", "Second"]
    for i in range(0, 10):
        # it's silly too, ofc
        r_country = random.choice(country)
        r_city = random.choice(city)
        r_street = random.choice(street)
        r_zipcode = ''.join(random.choice(string.digits) for _ in range(6))
        r_plid = i + 1
        db.insert('provider_location', 'p_location_id,country,city,zipcode,street', combine(
            r_plid, r_country, r_city, r_zipcode, r_street
        ))

    # workshop table
    open_time = [9, 12, 0, 18]
    close_time = [19, 0, 9, 3]
    for o, c in zip(open_time, close_time):
        open = str(o) + ":00"
        close = str(c) + ":00"
        db.insert('workshop', 'open_time,close_time', combine(open, close))

    # car_part_order table
    part_name = ["RP28", "Setula E-Pace RHO1", "TYC Combination Right", "DELPHI Brake Disc 278mm"]
    for i in range(0, 10):
        r_name = random.choice(part_name)
        r_amount = random.randint(1, 10)
        r_price = round(random.uniform(20.00, 50.00), 2)
        r_date, r2_date = two_random_dates()
        r_cid = random.randint(1, 4)
        r_wid = random.randint(1, 4)
        db.insert('car_part_order', 'part_name,amount,price_per_part,order_date,company_id,workshop_id', combine(
            r_name, r_amount, r_price, r_date, r_cid, r_wid
        ))

    # car_repair_history table
    for i in range(0, 10):
        r_date, r2_date = two_random_dates()
        r_wid = random.randint(1, 4)
        r_cid = random.randint(1, 4)
        db.insert('car_repair_history', 'date_time,WID,CID', combine(r_date, r_wid, r_cid))

    # repaired_car_parts
    for i in range(0, 10):
        r_name = random.choice(part_name)
        r_amount = random.randint(1, 4)
        ticket_id = random.randint(1, 10)
        db.insert('repaired_car_parts', 'part_name,amount,repair_ticket_id', combine(
            r_name, r_amount, ticket_id
        ))

    # customer table
    first_names = ["Homer", "Krosh", "Peter", "Jay", "Katy", "Lindsey"]
    last_names = ["Jefferson", "Cox", "Parker"]
    usernames = ["dalana", "kriff89", "john_doe", "terrra", "terrra1", "bunny", "twisted", "pixar"]
    endings = ["@mail.ru", "@gmail.com", "@yandex.ru"]
    emails = [usernames[i] + random.choice(endings) for i in range(0, 8)]
    hashes, salts = simplest_password_hash()
    for i in range(0, 8):
        r_first = random.choice(first_names)
        r_last = random.choice(last_names)
        r_username = usernames[i]
        r_phone = random_phone()
        r_email = emails[i]
        r_hash = hashes[i]
        r_salt = salts[i]
        db.insert('customer', 'first_name,last_name,username,phone_number,email,password_hash,password_salt',
                  combine(r_first, r_last, r_username, r_phone, r_email, r_hash, r_salt))

    # customer_location table
    for i in range(0, 8):
        r_country = random.choice(country)
        r_city = random.choice(city)
        r_zipcode = ''.join(random.choice(string.digits) for _ in range(6))
        db.insert('customer_location', 'c_location_id,country,city,zipcode', combine(
            i+1, r_country, r_city, r_zipcode
        ))

    # ride_order table
    start_location = ["Riverside Drive", "Cherry Lane", "8th Avenue", "Henry Street, 3", "Spring Street, 9"]
    pick_up_location = ["York Street, 5", "Smith Street, 3", "Railroad Ave.", "Harrison Street, 12", "Adams Ave."]
    # to prevent arriving at the same location
    end_location = ["Woodland Ave.", "Garden Street, 32", "Hudson Street, 20", "Evergreen Street, 11", "1st Ave."]
    pids = [random.randint(1, 8) for _ in range(1, 21)]
    cids = [random.randint(1, 10) for _ in range(1, 21)]
    for i in range(0, 20):
        r_start = random.choice(start_location)
        r_pick = random.choice(pick_up_location)
        r_dest = round(random.uniform(0.2, 4.5), 3)
        r_end = random.choice(end_location)
        r_start_time, r_end_time = two_random_dates()
        r_total_distance = round(random.uniform(1.5, 15.0), 3)
        r_price = round(prices[cids[i] - 1] * r_total_distance, 2)
        db.insert('ride_order', 'overall_price,start_location,pick_up_location,start_pick_up_dest,end_location,'
                                'start_time,end_time,total_distance,PID,CID', combine(
            r_price, r_start, r_pick, r_dest, r_end, r_start_time, r_end_time, r_total_distance, pids[i], cids[i]
        ))


    # payment table
    order_id = list(range(1, 21))
    for i in range(0, 20):
        date1, date2 = two_random_dates()
        db.insert('payment', 'date_time,PID,order_id', combine(date1, random.randint(1, 8), order_id[i]))


def simplest_password_hash():
    password_hashes = []
    salts = []
    for i in range(0, 8):
        password = ''.join(random.choice(string.ascii_letters) for _ in range(8))
        salt = ''.join(random.choice(string.ascii_letters) for _ in range(5))
        salts.append(salt)
        password_hashes.append(hash(password+salt))
    return password_hashes, salts


def random_phone():
    phone = ''.join(random.choice(string.digits) for _ in range(3))
    phone += '-'
    phone += ''.join(random.choice(string.digits) for _ in range(4))
    return phone


def two_random_dates():
    year = random.randint(2015, 2018)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    date1 = datetime(year, month, day, hour, minute, second)
    date2 = date1 + timedelta(0, random.randint(0, 100), 0, 0, random.randint(0, 100))
    return date1, date2
