/*holds information about cars' insides*/
CREATE TABLE car (
	CID INTEGER PRIMARY KEY AUTOINCREMENT,
	TYPE_ID INTEGER NOT NULL,
	color TEXT NOT NULL,
	baby_seat BOOLEAN NOT NULL,
	charge_level INTEGER NOT NULL,
	availability BOOLEAN NOT NULL,
	check_success BOOLEAN NOT NULL,
	FOREIGN KEY (TYPE_ID) REFERENCES car_type (TID)
);

/*table containing info about car_type*/
CREATE TABLE car_type (
	TID INTEGER PRIMARY KEY AUTOINCREMENT,
	class TEXT NOT NULL,
	num_of_seats INTEGER NOT NULL,
	plug_compat TEXT NOT NULL,
	FOREIGN KEY (plug_compat) REFERENCES plug_type (name)
);

/**/
CREATE TABLE plug_type (
	name TEXT PRIMARY KEY,
	size INTEGER NOT NULL,
	shape TEXT NOT NULL
);

CREATE TABLE charging_station (
	UID INTEGER PRIMARY KEY AUTOINCREMENT,
	cost_per_kw INTEGER NOT NULL,
	num_of_sockets INTEGER NOT NULL,
	num_of_avalaible_sockets INTEGER NOT NULL,
	latitude DOUBLE NOT NULL,
	longitute DOUBLE NOT NULL
);

CREATE TABLE charging_info (
	CHARGING_ID INTEGER PRIMARY KEY AUTOINCREMENT,
	start_time DATETIME NOT NULL,
	car_id INTEGER NOT NULL, 
	cs_id INTEGER NOT NULL,
	FOREIGN KEY (car_id) REFERENCES car (CID),
	FOREIGN KEY (cs_id) REFERENCES charging_station (UID)
);

CREATE TABLE provider (
	company_id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT UNIQUE NOT NULL,
	phone_num TEXT NOT NULL
);

/* table containing providers' addresses */
CREATE TABLE provider_location (
	p_location_id INTEGER PRIMARY KEY NOT NULL,
	country TEXT NOT NULL,
	city TEXT NOT NULL,
	zipcode TEXT NOT NULL,
	street TEXT NOT NULL
	CONSTRAIT fk_provider 
	    FOREIGN KEY p_location_id
	    REFERENCES provider (PID)
	    ON DELETE CASCADE
);

/* */
CREATE TABLE workshop (
	WID INTEGER PRIMARY KEY AUTOINCREMENT,
	avalailable_timing TEXT NOT NULL
);

CREATE TABLE workshop_location (
	
);

/* table listing car parts which was sold by
* by provider to a certain workshop */
CREATE TABLE car_part_order (
    part_name TEXT NOT NULL,
    amount INTEGER NOT NULL DEFAULT 1,
    price_per_part FLOAT NOT NULL,
    order_date DATETIME NOT NULL,
    company_id INTEGER NOT NULL,
    workshop_id INTEGER NOT NULL,
    FOREIGN KEY (company_id) REFERENCES provider (company)id),
    FOREIGN KEY (workshop_id) REFERENCES workshop (WID)
    PRIMARY KEY (part_name, order_date, workshop_id, company_id)
);

CREATE TABLE car_repair_history (
    date_time DATETIME NOT NULL,
    WID INTEGER NOT NULL,
    CID INTEGER NOT NULL
);

CREATE TABLE repaired_car_parts (
    part_name TEXT NOT NULL,
    amount INTEGER NOT NULL DEFAULT 1,

);

CREATE TABLE customer (
	PID INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    phone_number TEXT UNIQUE NOT NULL,
    email TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    password_salt TEXT NOT NULl
);

CREATE TABLE customer_location (
	c_location_id INTEGER PRIMARY KEY AUTOINCREMENT,
	country TEXT NOT NULL,
	city TEXT NOT NULL,
	zipcode TEXT NOT NULL,
	CONSTRAIT fk_customer
	    FOREIGN KEY (c_location_id) 
	    REFERENCES customer (PID)
	    ON DELETE CASCADE
);

CREATE TABLE ride_order (
    order_id INTEGER NOT NULL AUTOINCREMENT,
    overall_price FLOAT NOT NULL,
    start_location TEXT NOT NULL,
    end_location TEXT NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    total_distance FLOAT NOT NULL,
    PID INTEGER NOT NULL,
    FOREIGN KEY (PID) REFERENCES customer (PID)
);

CREATE TABLE payment (
    payment_id INTEGER NOT NULL AUTOINCREMENT,
    date_time DATETIME NOT NULL,
    PID INTEGER NOT NULL,
    order_id INTEGER NOT NULL,
    FOREIGN KEY (PID) REFERENCES customer (PID),
    FOREIGN KEY (order_id) REFERENCES ride_order (order_id)
);


    
    
