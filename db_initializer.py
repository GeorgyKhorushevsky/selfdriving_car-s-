# from db_handler import *


def init(db):

    db.query("""
        CREATE TABLE IF NOT EXISTS car (
            CID INTEGER PRIMARY KEY AUTOINCREMENT,
            license_plate TEXT UNIQUE NOT NULL,
            TYPE_ID INTEGER NOT NULL,
            color TEXT NOT NULL,
            baby_seat BOOLEAN NOT NULL,
            charge_level INTEGER NOT NULL,
            availability BOOLEAN NOT NULL,
            check_success BOOLEAN NOT NULL,
            price_per_km FLOAT NOT NULL,
            FOREIGN KEY (TYPE_ID) REFERENCES car_type (TID))
    """)

    db.query("""
        CREATE TABLE IF NOT EXISTS car_type (
            TID INTEGER PRIMARY KEY AUTOINCREMENT,
            class TEXT NOT NULL,
            num_of_seats INTEGER NOT NULL,
            plug_compat TEXT NOT NULL,
            CONSTRAINT car_type_uniqueness
                UNIQUE (class, num_of_seats, plug_compat) 
                ON CONFLICT REPLACE, 
            FOREIGN KEY (plug_compat) REFERENCES plug_type (pid))
    """)

    db.query("""
        CREATE TABLE IF NOT EXISTS plug_type (
            pid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            size INTEGER NOT NULL,
            shape TEXT NOT NULL,
            CONSTRAINT plug_type_uniqueness
                UNIQUE (name, size, shape)
                ON CONFLICT REPLACE)
    """)

    db.query("""
        CREATE TABLE IF NOT EXISTS charging_station (
            UID INTEGER PRIMARY KEY AUTOINCREMENT,
            cost_per_kw INTEGER NOT NULL,
            num_of_sockets INTEGER NOT NULL,
            num_of_available_sockets INTEGER NOT NULL,
            latitude DOUBLE NOT NULL,
            longitude DOUBLE NOT NULL)
    """)

    db.query("""
        CREATE TABLE IF NOT EXISTS charging_order (
            CHARGING_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            start_time DATETIME NOT NULL,
            end_time DATETIME NOT NULL,
            car_id INTEGER NOT NULL, 
            cs_id INTEGER NOT NULL,
            price FLOAT NOT NULL,
            FOREIGN KEY (car_id) REFERENCES car (CID),
            FOREIGN KEY (cs_id) REFERENCES charging_station (UID))
    """)

    db.query("""
        CREATE TABLE IF NOT EXISTS provider (
            company_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            phone_num TEXT NOT NULL)
    """)

    db.query("""
        CREATE TABLE IF NOT EXISTS provider_location (
            p_location_id INTEGER PRIMARY KEY NOT NULL,
            country TEXT NOT NULL,
            city TEXT NOT NULL,
            zipcode TEXT NOT NULL,
            street TEXT NOT NULL,
            CONSTRAINT fk_provider 
                FOREIGN KEY (p_location_id)
                REFERENCES provider (PID)
                ON DELETE CASCADE)
    """)

    db.query("""
          CREATE TABLE IF NOT EXISTS workshop_location (
              w_location_id INTEGER PRIMARY KEY NOT NULL,
              country TEXT NOT NULL,
              city TEXT NOT NULL,
              zipcode TEXT NOT NULL,
              street TEXT NOT NULL,
              CONSTRAINT fk_workshop
                  FOREIGN KEY (w_location_id)
                  REFERENCES workshop (WID)
                  ON DELETE CASCADE)
      """)

    db.query("""
        CREATE TABLE IF NOT EXISTS workshop (
            WID INTEGER PRIMARY KEY AUTOINCREMENT,
            open_time TEXT NOT NULL,
            close_time TEXT NOT NULL)
    """)

    db.query("""
        CREATE TABLE IF NOT EXISTS car_part_order (
            part_name TEXT NOT NULL,
            amount INTEGER NOT NULL DEFAULT 1,
            price_per_part FLOAT NOT NULL,
            order_date DATETIME NOT NULL,
            company_id INTEGER NOT NULL,
            workshop_id INTEGER NOT NULL,
            FOREIGN KEY (company_id) REFERENCES provider (company_id),
            FOREIGN KEY (workshop_id) REFERENCES workshop (WID)
            PRIMARY KEY (part_name, order_date, workshop_id, company_id))
    """)

    db.query("DROP TABLE IF EXISTS car_repair_history")
    db.query("""
        CREATE TABLE IF NOT EXISTS car_repair_history (
            repair_ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
            date_time DATETIME NOT NULL,
            overall_price FLOAT NOT NULL,
            WID INTEGER NOT NULL,
            CID INTEGER NOT NULL,
            UNIQUE(CID, WID, date_time))
    """)

    db.query("""
        CREATE TABLE IF NOT EXISTS repaired_car_parts (
            part_name TEXT NOT NULL,
            amount INTEGER NOT NULL DEFAULT 1,
            repair_ticket_id INTEGER NOT NULL,
            FOREIGN KEY (repair_ticket_id) REFERENCES car_repair_history (repair_ticket_id))
    """)

    db.query("""
        CREATE TABLE IF NOT EXISTS customer (
            PID INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            phone_number TEXT UNIQUE NOT NULL,
            email TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            password_salt TEXT NOT NULl)
    """)

    db.query("""
        CREATE TABLE IF NOT EXISTS customer_location (
            c_location_id INTEGER PRIMARY KEY,
            country TEXT NOT NULL,
            city TEXT NOT NULL,
            zipcode TEXT NOT NULL,
            CONSTRAINT fk_customer
                FOREIGN KEY (c_location_id) 
                REFERENCES customer (PID)
                ON DELETE CASCADE)
    """)

    db.query("""
        CREATE TABLE IF NOT EXISTS ride_order (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            overall_price FLOAT NOT NULL,
            start_location TEXT NOT NULL,
            pick_up_location TEXT NOT NULL,
            start_pick_up_dest FLOAT NOT NULL,
            end_location TEXT NOT NULL,
            start_time DATETIME NOT NULL,
            end_time DATETIME NOT NULL,
            total_distance FLOAT NOT NULL,
            PID INTEGER NOT NULL,
            CID INTEGER NOT NULL,
            FOREIGN KEY (PID) REFERENCES customer (PID),
            FOREIGN KEY (CID) REFERENCES car (CID))
    """)

    db.query("""
        CREATE TABLE IF NOT EXISTS payment (
            payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            date_time DATETIME NOT NULL,
            PID INTEGER NOT NULL,
            order_id INTEGER NOT NULL,
            FOREIGN KEY (PID) REFERENCES customer (PID),
            FOREIGN KEY (order_id) REFERENCES ride_order (order_id))
    """)

