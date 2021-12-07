CREATE PROCEDURE create_all_tables()
LANGUAGE SQL
AS $$
CREATE TABLE processor
(sku INT NOT NULL,
 brand VARCHAR(50) NOT NULL,	
 model VARCHAR(50) NOT NULL,
 socket VARCHAR(50) NOT NULL,
 number_of_cores INT NOT NULL,
 number_of_threads INT NOT NULL,
 integrated_graphics_processor VARCHAR(50) NOT NULL,
 tdp INT NOT NULL,
 price INT NOT NULL, 
 amount INT NOT NULL
);

CREATE TABLE cooling
(sku INT NOT NULL, 
brand VARCHAR(50) NOT NULL, 
model VARCHAR(50) NOT NULL, 
socket VARCHAR(50) NOT NULL,						 
tdp INT NOT NULL, 
price INT NOT NULL, 
amount INT NOT NULL
);

CREATE TABLE motherboard
(sku INT NOT NULL, 
brand VARCHAR(50) NOT NULL, 
model VARCHAR(50) NOT NULL, 
socket VARCHAR(50) NOT NULL,
chipset VARCHAR(50) NOT NULL, 
mem_type VARCHAR(50) NOT NULL,
num_mem_slots INT NOT NULL,
form_factor VARCHAR(50) NOT NULL, 
m2_slot INT NOT NULL,
price INT NOT NULL, 
amount INT NOT NULL
);

CREATE TABLE ram
(sku INT NOT NULL, 
brand VARCHAR(50) NOT NULL, 
model VARCHAR(50), 
mem_type VARCHAR(50) NOT NULL, 
mem_capacity INT NOT NULL, 
frequency INT NOT NULL, 
num_of_modules INT NOT NULL, 
price INT NOT NULL, 
amount INT NOT NULL
);

CREATE TABLE graphics_card
(sku INT NOT NULL,
chip_manufacturer VARCHAR(50) NOT NULL,
brand VARCHAR(50) NOT NULL,
model VARCHAR(50) NOT NULL,
mem_capacity INT NOT NULL,
mem_type VARCHAR(50) NOT NULL,
length INT NOT NULL,
price INT NOT NULL,
amount INT NOT NULL
);

CREATE TABLE power_supply
(sku INT NOT NULL, 
brand VARCHAR(50) NOT NULL, 
model VARCHAR(50) NOT NULL, 
output_power INT NOT NULL,
price INT NOT NULL, 
amount INT NOT NULL
);


CREATE TABLE case_pc
(sku INT NOT NULL, 
brand VARCHAR(50) NOT NULL, 
model VARCHAR(50) NOT NULL, 
form_factor VARCHAR(50) NOT NULL,
graphics_card_lenght INT NOT NULL, 
price INT NOT NULL, 
amount INT NOT NULL
);


CREATE TABLE hard_disc_drive
(sku INT NOT NULL, 
brand VARCHAR(50) NOT NULL, 
model VARCHAR(50) NOT NULL, 
capacity INT NOT NULL, 
rotation_speed INT NOT NULL, 
form_factor VARCHAR(50) NOT NULL,
price INT NOT NULL, 
amount INT NOT NULL
);


CREATE TABLE solid_state_drive
(sku INT NOT NULL, 
brand VARCHAR(50) NOT NULL,
model VARCHAR(50) NOT NULL, 
capacity INT NOT NULL, 
form_factor VARCHAR(50),
price INT NOT NULL, 
amount INT NOT NULL
);


CREATE TABLE order_customer
(order_id SERIAL, 
customer_phone VARCHAR(15) NOT NULL, 
proc_sku INT NOT NULL, 
cool_sku INT NOT NULL, 
ram_sku INT NOT NULL, 
ram_amount INT NOT NULL, 
motherboard_sku INT NOT NULL, 
graphics_card_sku INT NOT NULL, 
hdd_sku INT NOT NULL, 
ssd_sku INT NOT NULL, 
power_supply_sku INT NOT NULL, 
case_pc_sku INT NOT NULL, 
comments VARCHAR(300) NOT NULL, 
status VARCHAR(50) NOT NULL, 
total_price INT 
);




CREATE TABLE customer
(phone_number VARCHAR(15) NOT NULL, 
first_name VARCHAR(30) NOT NULL, 
last_name VARCHAR(30) NOT NULL
);


$$;

CALL create_all_tables();


CREATE PROCEDURE drop_all_tables()
LANGUAGE SQL
AS $$
	DROP TABLE processor, cooling, motherboard, ram, power_supply, order_customer, customer, graphics_card, case_pc, hard_disc_drive, solid_state_drive;
$$;

CREATE PROCEDURE clear_all_tables()
LANGUAGE SQL
AS $$
	DELETE from processor;
	DELETE from cooling;
	DELETE from motherboard;
	DELETE from ram;
	DELETE from power_supply;
	DELETE from order_customer;
	DELETE from customer;
	DELETE from graphics_card;
	DELETE from case_pc;
	DELETE from hard_disc_drive;
	DELETE from solid_state_drive;
$$;
CREATE PROCEDURE insert_proc(sku_arg INT, brand_arg VARCHAR(50), model_arg VARCHAR(50), socket_arg VARCHAR(50), number_of_cores_arg INT,
						  number_of_threads_arg INT, integrated_graphicss_processor_arg VARCHAR(50), tdp_arg INT, price_arg INT, amount_arg INT)
LANGUAGE SQL
AS $$
	INSERT INTO processor
	VALUES
	(sku_arg, brand_arg, model_arg, socket_arg, number_of_cores_arg, number_of_threads_arg, integrated_graphicss_processor_arg, tdp_arg, price_arg, amount_arg);
$$;

CREATE PROCEDURE insert_cool(sku_arg INT, brand_arg VARCHAR(50), model_arg VARCHAR(50), socket_arg VARCHAR(50),
									 tdp_arg INT, price_arg INT, amount_arg INT)
LANGUAGE SQL
AS $$
	INSERT INTO cooling
	VALUES
	(sku_arg, brand_arg, model_arg, socket_arg, tdp_arg, price_arg, amount_arg);
$$;


CREATE PROCEDURE insert_motherboard(sku_arg INT, brand_arg VARCHAR(50), model_arg VARCHAR(50), socket_arg VARCHAR(50),
									 chipset_arg VARCHAR(50), mem_type_arg VARCHAR(50), num_mem_slots_arg INT, form_factor_arg VARCHAR(50), m2_slot_arg INT,
									 price_arg INT, amount_arg INT)
LANGUAGE SQL
AS $$
	INSERT INTO motherboard
	VALUES
	(sku_arg, brand_arg, model_arg, socket_arg, chipset_arg, mem_type_arg, num_mem_slots_arg, form_factor_arg, m2_slot_arg, price_arg, amount_arg);
$$;

CREATE PROCEDURE insert_gpu(sku_arg INT, chip_manufacturer_arg VARCHAR(50), brand_arg VARCHAR(50), model_arg VARCHAR(50), mem_capacity_arg INT,
					  mem_type_arg VARCHAR(50), length_arg INT, price_arg INT, amount_arg INT)
LANGUAGE SQL
AS $$
	INSERT INTO graphics_card
	VALUES
	(sku_arg, chip_manufacturer_arg, brand_arg, model_arg, mem_capacity_arg, mem_type_arg, length_arg, price_arg, amount_arg);
$$;

CREATE PROCEDURE insert_ram(sku_arg INT, brand_arg VARCHAR(50), model_arg VARCHAR(50), mem_type_arg VARCHAR(50), mem_capacity_arg INT,
									 frequency_arg INT, num_of_modules_arg INT, price_arg INT, amount_arg INT)
LANGUAGE SQL
AS $$
	INSERT INTO ram
	VALUES
	(sku_arg, brand_arg, model_arg, mem_type_arg, mem_capacity_arg, frequency_arg, num_of_modules_arg,  price_arg, amount_arg);
$$;


CREATE PROCEDURE insert_power_supply(sku_arg INT, brand_arg VARCHAR(50), model_arg VARCHAR(50), output_power_arg INT,
										  price_arg INT, amount_arg INT)
LANGUAGE SQL
AS $$
	INSERT INTO power_supply
	VALUES
	(sku_arg, brand_arg, model_arg, output_power_arg, price_arg, amount_arg);
$$;



CREATE PROCEDURE insert_case_pc(sku_arg INT, brand_arg VARCHAR(50), model_arg VARCHAR(50), form_factor_arg VARCHAR(50),
					graphics_card_lenght_arg INT, price_arg INT, amount_arg INT)
LANGUAGE SQL
AS $$
	INSERT INTO case_pc
	VALUES
	(sku_arg, brand_arg, model_arg, form_factor_arg, graphics_card_lenght_arg, price_arg, amount_arg);
$$;



CREATE PROCEDURE insert_hdd(sku_arg INT, brand_arg VARCHAR(50), model_arg VARCHAR(50), capacity_arg INT, rotation_speed_arg INT, form_factor_arg VARCHAR(50),
										 price_arg INT, amount_arg INT)
LANGUAGE SQL
AS $$
	INSERT INTO hard_disc_drive
	VALUES
	(sku_arg, brand_arg, model_arg, capacity_arg, rotation_speed_arg, form_factor_arg, price_arg, amount_arg);
$$;

CREATE PROCEDURE insert_ssd(sku_arg INT, brand_arg VARCHAR(50), model_arg VARCHAR(50), capacity_arg INT, form_factor_arg VARCHAR(50),
										 price_arg INT, amount_arg INT)
LANGUAGE SQL
AS $$
	INSERT INTO solid_state_drive
	VALUES
	(sku_arg, brand_arg, model_arg, capacity_arg, form_factor_arg, price_arg, amount_arg);
$$;

CREATE PROCEDURE insert_order_customer(order_id_arg INT, customer_phone_arg VARCHAR(15), proc_sku_arg INT, cool_sku_arg INT, ram_sku_arg INT,
								   ram_amount_arg INT, motherboard_sku_arg INT, graphics_card_sku_arg INT, hdd_sku_arg INT,
								  ssd_sku_arg INT, power_supply_sku_arg INT, case_sku_arg INT, comments_arg VARCHAR(300), status_arg VARCHAR(50))
LANGUAGE SQL
AS $$
	INSERT INTO order_customer
	VALUES
	(order_id_arg, customer_phone_arg, proc_sku_arg, cool_sku_arg, ram_sku_arg,
								   ram_amount_arg, motherboard_sku_arg, graphics_card_sku_arg, hdd_sku_arg,
								  ssd_sku_arg, power_supply_sku_arg, case_sku_arg, comments_arg, status_arg);
$$;


CREATE PROCEDURE insert_customer(phone_number_arg VARCHAR(15), first_name_arg VARCHAR(30), last_name_arg VARCHAR(30))
LANGUAGE SQL
AS $$
	INSERT INTO customer
	VALUES
	(phone_number_arg, first_name_arg, last_name_arg);
$$;

CREATE OR REPLACE FUNCTION f_total_price()
  RETURNS trigger AS
$$
BEGIN
         UPDATE order_customer
         SET total_price = (SELECT MIN(price) FROM processor JOIN order_customer ON processor.sku = order_customer.proc_sku) +
			      (SELECT MIN(price) FROM cooling JOIN order_customer ON order_customer.cool_sku = cooling.sku) +
			      (SELECT MIN(price) FROM motherboard JOIN order_customer ON order_customer.motherboard_sku = motherboard.sku) +
                  (SELECT MIN(price) FROM ram JOIN order_customer ON order_customer.ram_sku = ram.sku)*
				  (SELECT ram_amount FROM order_customer ORDER BY order_id DESC LIMIT 1) +
			      (SELECT MIN(price) FROM power_supply JOIN order_customer ON order_customer.power_supply_sku = power_supply.sku) +
			      (SELECT MIN(price_arg) FROM case_pc JOIN order_customer ON order_customer.case_sku = case_pc.sku) +
			      (SELECT MIN(price) FROM hard_disc_drive JOIN order_customer ON order_customer.hdd_sku = hard_disc_drive.sku) +
			      (SELECT MIN(price_arg) FROM solid_state_drive JOIN order_customer ON order_customer.ssd_sku = solid_state_drive.sku) +
				  (SELECT MIN(price) FROM graphics_card JOIN order_customer ON order_customer.graphics_card_sku = graphics_card.sku);
 
    RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';

CREATE TRIGGER after_Insert_f_total_price
  AFTER INSERT
  ON order_customer
  FOR EACH ROW
  EXECUTE PROCEDURE f_total_price();

CREATE FUNCTION return_proc() RETURNS SETOF processor AS $$
  SELECT *
  FROM processor;
$$ LANGUAGE SQL;


CREATE FUNCTION return_case_pc() RETURNS SETOF case_pc AS $$
  SELECT *
  FROM case_pc;
$$ LANGUAGE SQL;


CREATE FUNCTION return_cool() RETURNS SETOF cooling AS $$
  SELECT *
  FROM cooling;
$$ LANGUAGE SQL;


CREATE FUNCTION return_customer() RETURNS SETOF customer AS $$
  SELECT *
  FROM customer;
$$ LANGUAGE SQL;


CREATE FUNCTION return_gpu() RETURNS SETOF graphics_card AS $$
  SELECT *
  FROM graphics_card;
$$ LANGUAGE SQL;


CREATE FUNCTION return_hdd() RETURNS SETOF hard_disc_drive AS $$
  SELECT *
  FROM hard_disc_drive;
$$ LANGUAGE SQL;


CREATE FUNCTION return_motherboard() RETURNS SETOF motherboard AS $$
  SELECT *
  FROM motherboard;
$$ LANGUAGE SQL;


CREATE FUNCTION return_order_customer() RETURNS SETOF order_customer AS $$
  SELECT *
  FROM order_customer;
$$ LANGUAGE SQL;


CREATE FUNCTION return_power_supply() RETURNS SETOF power_supply AS $$
  SELECT *
  FROM power_supply;
$$ LANGUAGE SQL;


CREATE FUNCTION return_ram() RETURNS SETOF ram AS $$
  SELECT *
  FROM ram;
$$ LANGUAGE SQL;


CREATE FUNCTION return_ssd() RETURNS SETOF solid_state_drive AS $$
  SELECT *
  FROM solid_state_drive;
$$ LANGUAGE SQL;

CREATE PROCEDURE insert_data_to_tables()
LANGUAGE SQL
AS $$

INSERT INTO processor
VALUES
(1100,	'Intel',	'Celeron G5905',	'LGA 1200',	2,	2,	'Intel UHD graphicss 610',	58,	3999,	10),
(1101,	'Intel',	'Core i3-10100F',	'LGA 1200',	4,	8,	'none',	65,	6499,	11),
(1102,	'Intel',	'Pentium Gold G6500',	'LGA 1200',	2,	4,	'Intel UHD graphicss 630',	58,	7699,	9),
(1103,	'Intel',	'Core i5-10400F',	'LGA 1200',	6,	12,	'none',	65,	12799,	4),
(1104,	'Intel',	'Core i7-9700',	'LGA 1151-v2',	8,	8,	'Intel UHD graphicss 630',	65,	23499,	3),
(1105,	'Intel',	'Core i5-12600K',	'LGA 1700',	10,	16,	'Intel UHD graphicss 770',	215,	25799,	3),
(1106,	'Intel',	'Core i7-11700F',	'LGA 1200',	8,	16,	'none',	65,	25699,	5),
(1107,	'Intel',	'Core i7-12700KF',	'LGA 1700',	12,	20,	'none',	125,	36499,	3),
(1108,	'Intel',	'Core i9-11900',	'LGA 1200',	8,	16,	'Intel UHD graphicss 750',	65,	36799,	2),
(1109,	'Intel',	'Core i9-10980XE',	'LGA 2066',	18,	36,	'none',	165,	87499,	1),
(1200,	'AMD',	'Ryzen 3 4300GE',	'AM4',	4,	8,	'Radeon Vega 6',	35,	15799,	12),
(1201,	'AMD',	'Ryzen Threadripper 1920X',	'TR4',	12,	24,	'none',	180,	15299,	3),
(1202,	'AMD',	'Ryzen 5 3600',	'AM4',	6,	12,	'none',	65,	20399,	5),
(1203,	'AMD',	'Ryzen 7 3800X',	'AM4',	8,	16,	'none',	105,	28499,	1),
(1204,	'AMD',	'FX-4320',	'AM3+',	4,	4,	'none',	125,	2999,	1),
(1205,	'AMD',	'Ryzen 5 5600X',	'AM4',	6,	12,	'none',	65,	25999,	2),
(1206,	'AMD',	'Ryzen 7 5800X',	'AM4',	8,	16,	'none',	105,	35999,	3),
(1207,	'AMD',	'Ryzen Threadripper 3990X',	'sTRX4',	64,	128,	'none',	280,	349999,	1),
(1208,	'AMD',	'Ryzen 9 5950X',	'AM4',	16,	32,	'none',	105,	71999,	2);



INSERT INTO cooling
VALUES
(5100,	'AeroCool',	'Verkho 2',	'LGA 1200',	110,	899,	7),
(5200,	'Arctic Cooling',	'Freezer 50 TR',	'TR4',	250,	5299,	1),
(5300,	'be quiet!',	'PURE ROCK SLIM 2',	'AM4',	130,	2599,	6),
(5301,	'be quiet!',	'DARK ROCK PRO TR4',	'sTRX4',	250,	7499,	1),
(5400,	'CoolerMaster',	'Z70',	'AM3+',	95,	750,	3),
(5401,	'CoolerMaster',	'Air Frost Plus',	'AM4',	110,	799,	12),
(5402,	'CoolerMaster',	'MasterAir MA410M',	'LGA 1151-v2',	150,	4299,	2),
(5500,	'DEEPCOOL',	'Ice Blade 100',	'LGA 1151-v2',	100,	599,	20),
(5501,	'DEEPCOOL',	'GAMMAXX 300',	'LGA 1200',	130,	1299,	8),
(5600,	'Noctua',	'NH-U9 TR4-SP3',	'sTRX4',	180,	8999,	1);


INSERT INTO power_supply
VALUES
(6100,	'be quiet!',	'SYSTEM POWER 9 400W',	400,	3950,	4),
(6101,	'be quiet!',	'DARK POWER 12 750W',	750,	19999,	3),
(6102,	'be quiet!',	'DARK POWER 12 1200W',	1200,	39999,	1),
(6200,	'Corsair',	'VS350',	350,	3699,	6),
(6201,	'Corsair',	'CX550F RGB',	550,	6049,	7),
(6202,	'Corsair',	'TX850M',	850,	12999,	2),
(6300,	'Cougar',	'STE 600W',	600,	2799,	4),
(6301,	'Cougar',	'STX750',	750,	4999,	3),
(6400,	'DEEPCOOL',	'DE600 v2',	450,	2750,	3),
(6500,	'EVGA',	'550 N1',	550,	4999,	4),
(6501,	'EVGA',	'700 BR',	700,	6399,	4),
(6600,	'FSP',	'PNR PRO 400W',	400,	2599,	5),
(6700,	'Seasonic',	'S12III-650',	650,	5950,	5),
(6800,	'Thermaltake',	'Litepower RGB 450W',	450,	3099,	2),
(6801,	'Thermaltake',	'Smart PRO RGB 750W',	750,	7899,	3);


INSERT INTO graphics_card
VALUES
(3120,	'AMD',	'GIGABYTE',	'RX 6600 XT GAMING OC PRO',	8,	'GDDR6',	282,	76999,	2),
(3121,	'AMD',	'GIGABYTE',	'RX 5600 XT WINDFORCE OC',	6,	'GDDR6',	228,	88999,	1),
(3140,	'AMD',	'MSI',	'RX 6600 ARMOR',	8,	'GDDR6',	238,	69999,	5),
(3141,	'AMD',	'MSI',	'RX 6700 XT GAMING X',	12,	'GDDR6',	279,	119999,	4),
(3210,	'NVIDIA',	'ASUS',	'GTX 1660 PHOENIX OC',	6,	'GDDR5',	174,	59999,	4),
(3211,	'NVIDIA',	'ASUS',	'GTX 1660Ti TUF Gaming EVO OC EDITION',	6,	'GDDR6',	206,	65999,	3),
(3220,	'NVIDIA',	'GIGABYTE',	'RTX 2060 D6 6G',	6,	'GDDR6',	226,	69999,	2),
(3221,	'NVIDIA',	'GIGABYTE',	'RTX 3080 Ti AORUS MASTER',	12,	'GDDR6X',	319,	199999,	1),
(3230,	'NVIDIA',	'KFA2',	'GTX 1050Ti 1-Click OC',	4,	'GDDR5',	196,	27999,	3),
(3240,	'NVIDIA',	'MSI',	'GT 1030 LP OC',	2,	'GDDR4',	150,	8999,	10),
(3241,	'NVIDIA',	'MSI',	'GTX 1660 SUPER Gaming X',	6,	'GDDR6',	247,	72999,	3),
(3242,	'NVIDIA',	'MSI',	'RTX 3060 Ti VENTUS 2X OCV1',	8,	'GDDR6',	235,	94999,	4),
(3243,	'NVIDIA',	'MSI',	'RTX 3080 GAMING Z TRIO',	10,	'GDDR6X',	323,	169999,	1),
(3250,	'NVIDIA',	'Palit',	'RTX 3060 DUAL',	12,	'GDDR6',	245,	73999,	2),
(3251,	'NVIDIA',	'Palit',	'RTX 3070 JetStream',	8,	'GDDR6',	304,	109999,	2),
(3252,	'NVIDIA',	'Palit',	'RTX 3070 Ti GameRock',	8,	'GDDR6X',	304,	134999,	1),
(3253,	'NVIDIA',	'Palit',	'RTX 3080 GameRock',	10,	'GDDR6X',	304,	244999,	1),
(3254,	'NVIDIA',	'Palit',	'RTX 3090 GameRock',	24,	'GDDR6X',	304,	319999,	1),
(3260,	'NVIDIA',	'ZOTAC',	'GT 730 Zone Edition',	2,	'GDDR3',	146,	5999,	4);


INSERT INTO motherboard
VALUES
(2400,	'ASRock',	'B365M PRO4',	'LGA 1151-v2',	'B365',	'DDR4',	4,	'Micro-ATX',	2,	6099,	1),
(2401,	'ASRock',	'760GM-HDV',	'AM3+',	'760G',	'DDR3',	2,	'Micro-ATX',	0,	5499,	1),
(2402,	'ASRock',	'X370 Pro4',	'AM4',	'X370',	'DDR4',	4,	'Standart-ATX',	2,	6999,	1),
(2403,	'ASRock',	'B550 Pro4',	'AM4',	'B550',	'DDR4',	4,	'Standart-ATX',	2,	10099,	1),
(2404,	'ASRock',	'X570 Taichi Razer Edition',	'AM4',	'X570',	'DDR4',	4,	'Standart-ATX',	3,	31999,	1),
(2200,	'ASUS',	'PRIME H510M-R',	'LGA 1200',	'H510',	'DDR4',	2,	'Micro-ATX',	0,	5599,	2),
(2201,	'ASUS',	'ROG STRIX B560-G GAMING WIFI',	'LGA 1200',	'B560',	'DDR4',	4,	'Micro-ATX',	2,	15199,	1),
(2202,	'ASUS',	'ROG MAXIMUS XIII HERO',	'LGA 1200',	'Z590',	'DDR4',	4,	'Standart-ATX',	4,	39999,	1),
(2203,	'ASUS',	'TUF Z390-PLUS GAMING',	'LGA 1151-v2',	'Z390',	'DDR4',	4,	'Standart-ATX',	2,	12899,	1),
(2204,	'ASUS',	'PRIME B450-PLUS',	'AM4',	'B450',	'DDR4',	4,	'Standart-ATX',	1,	6350,	2),
(2205,	'ASUS',	'ROG ZENITH EXTREME',	'TR4',	'X399',	'DDR4',	8,	'E-ATX',	1,	44999,	1),
(2300,	'GIGABYTE',	'Z490 UD',	'LGA 1200',	'Z490',	'DDR4',	4,	'Standart-ATX',	2,	9999,	2),
(2301,	'GIGABYTE',	'X299X AORUS MASTER',	'LGA 2066',	'X299',	'DDR4',	8,	'E-ATX',	2,	37999,	1),
(2302,	'GIGABYTE',	'Z690 UD', 	'LGA 1700',	'Z690',	'DDR5',	4,	'Standart-ATX',	3,	17599,	2),
(2303,	'GIGABYTE',	'Z690 AORUS MASTER',	'LGA 1700',	'Z690',	'DDR5',	4,	'E-ATX',	5,	39999,	1),
(2304,	'GIGABYTE',	'A520I AC',	'AM4',	'A520',	'DDR4',	2,	'Mini-ITX',	1,	7999,	2),
(2305,	'GIGABYTE',	'X570 I AORUS PRO WIFI',	'AM4',	'X570',	'DDR4',	2,	'Mini-ITX',	3,	14999,	1),
(2306,	'GIGABYTE',	'TRX40 AORUS XTREME',	'sTRX4',	'TRX40',	'DDR4',	8,	'XL-ATX',	4,	79999,	1),
(2100,	'MSI',	'H410M PRO-E',	'LGA 1200',	'H410',	'DDR4',	2,	'Micro-ATX',	0,	5199,	6),
(2101,	'MSI',	'B560M-A PRO',	'LGA 1200',	'B560',	'DDR4',	2,	'Micro-ATX',	1,	6499,	3),
(2102,	'MSI',	'B450M-A PRO MAX',	'AM4',	'B450',	'DDR4',	2,	'Micro-ATX',	1,	4099,	2);


INSERT INTO ram
VALUES
(4100,  'Crucial', NULL,            'DDR4',  4,  2666,  1,  1599,  12),
(4101,  'Crucial',   NULL,             'DDR4',  8,  3400,  1,  2699,  8),
(4200,  'G.Skill',  'TRIDENT Z',        'DDR4',  8,  3200,  2,  6799,  1),
(4201,  'G.Skill',  'TRIDENT Z Neo RGB',    'DDR4',  32,  3600,  4,  51999,  1),
(4300,  'Hynix',  NULL,             'DDR4',  8,  3200,  1,  2599,  13),
(4301,  'Hynix',  NULL,             'DDR4',  16,  2666,  1,  4999,  8),
(4400,  'Kingston',  'ValueRAM',         'DDR3',  2,  1600,  1,  1650,  4),
(4401,  'Kingston',  'HyperX FURY Black Series',  'DDR3',  4,  1866,  1,  2399,  5),
(4402,  'Kingston',  'HyperX FURY Beast Black',  'DDR3',  8,  1866,  2,  10999,  2),
(4403,  'Kingston',  'FURY Beast Black',      'DDR4',  4,  2666,  1,  2199,  4),
(4404,  'Kingston',  'HyperX FURY Black',     'DDR4',  4,  3000,  1,  2299,  5),
(4405,  'Kingston',  'ValueRAM',          'DDR4',  8,  2666,  1,  2450,  7),
(4406,  'Kingston',  'FURY Beast Black RGB',    'DDR4',  8,  3000,  1,  3399,  4),
(4407,  'Kingston',  'HyperX FURY Black',    'DDR4',  8,  3600,  1,  4099,  5),
(4408,  'Kingston',  'HyperX FURY Black',    'DDR4',  32,  2400,  1,  10999,  3),
(4409,  'Kingston',  'FURY Beast Black RGB',    'DDR4',  16,  2666,  2,  11799,  4),
(4410,  'Kingston',  'FURY Beast Black',      'DDR4',  8,  3600,  4,  13999,  1),
(4411,  'Kingston',  'HyperX FURY RGB',      'DDR4',  32,  3600,  4,  55999,  1),
(4500,  'Patriot',  'Viper Elite II',      'DDR4',  8,  2666,  1,  2699,  5),
(4501,  'Patriot',  'Viper 4 Blackout',      'DDR4',  4,  3000,  2,  3399,  3),
(4502,  'Patriot',  'Viper 4 Blackout',      'DDR4',  8,  3000,  2,  5550,  3),
(4503,  'Patriot',  'Viper Elite II',      'DDR4',  8,  3600,  2,  5699,  2),
(4504,  'Patriot',  'Viper RGB',        'DDR4',  8,  4000,  2,  9999,  4),
(4601,  'Samsung',   NULL,             'DDR4',  4,  3200,  1,  1899,  9),
(4602,  'Samsung',   NULL,             'DDR4',  8,  2933,  1,  2899,  7);


INSERT INTO solid_state_drive
VALUES
(7110,	'Kingston',	'A400',	480,	'"2.5"',	3699,	6),
(7111,	'Kingston',	'KC600',	1024,	'"2.5"',	11499,	3),
(7120,	'Kingston',	'A400',	240,	'm.2',	1799,	4),
(7121,	'Kingston',	'KC2500',	250,	'm.2',	3499,	3),
(7122,	'Kingston',	'KC2500',	1000,	'm.2',	9899,	4),
(7210,	'Samsung',	'870 EVO',	250,	'"2.5"',	5099,	8),
(7211,	'Samsung',	'870 QVO',	4000,	'"2.5"',	36499,	1),
(7220,	'Samsung',	'860 EVO',	250,	'm.2',	4199,	7),
(7221,	'Samsung',	'980',	500,	'm.2',	6199,	3);


INSERT INTO hard_disc_drive
VALUES
(8100,	'Seagate',	'BarraCuda',	1000,	7200,	'"3.5"',	3299,	7),
(8101,	'Seagate',	'BarraCuda Pro',	500,	7200,	'"2.5"',	3199,	3),
(8102,	'Seagate',	'BarraCuda',	2000,	5400,	'"2.5"',	5999,	5),
(8103,	'Seagate',	'SkyHawk',	3000,	5400,	'"3.5"',	7299,	5),
(8200,	'WD',	'Blue',	500,	5400,	'"3.5"',	2599,	4),
(8201,	'WD',	'Blue',	500,	7200,	'"3.5"',	2699,	8),
(8202,	'WD',	'Blue',	1000,	5400,	'"3.5"',	3099,	6),
(8203,	'WD',	'Black',	1000,	7200,	'"3.5"',	5499,	4),
(8204,	'WD',	'Blue Mobile',	500,	5400,	'"2.5"',	2950,	5),
(8205,	'WD',	'Red Plus',	3000,	5400,	'"3.5"',	6499,	6);


INSERT INTO case_pc
VALUES
(9100,	'Aerocool',	'Bolt Mini',	'Micro-ATX',	318,	2899,	3),
(9101,	'Aerocool',	'Glider-G',	'Standatr-ATX',	325,	3099,	2),
(9200,	'be quiet!',	'PURE BASE 500 Window',	'Standatr-ATX',	369,	7899,	4),
(9300,	'CoolerMaster',	'MasterBox K501L',	'Standatr-ATX',	410,	3599,	4),
(9400,	'Corsair',	'Carbide Series SPEC-DELTA RGB',	'Standatr-ATX',	330,	4999,	5),
(9500,	'Cougar',	'MG120-G',	'Micro-ATX',	330,	2999,	5),
(9501,	'Cougar',	'QBX',	'Mini-ITX',	350,	4450,	4),
(9600,	'DEEPCOOL',	'E_SHIELD',	'E-ATX',	370,	3750,	2),
(9601,	'DEEPCOOL',	'MATREXX 55 MESH ADD-RGB 4F',	'Standatr-ATX',	370,	5950,	4),
(9700,	'Fractal Design',	'Core 2300',	'Standatr-ATX',	380,	5199,	2),
(9800,	'NZXT',	'H510',	'Standatr-ATX',	381,	6499,	2),
(9900,	'Thermaltake',	'Versa T35 TG RGB',	'Standatr-ATX',	300,	4699,	3),
(9901,	'Thermaltake',	'The Tower 100',	'Mini-ITX',	330,	8799,	1);


INSERT INTO customer
VALUES
('89053653555', 'Ivanov','Alex'),
('89081234567', 'Sidorov', 'Pavel');

$$;


CREATE PROCEDURE change_status_complete_order(order_id_arg INT)
LANGUAGE SQL
AS $$
	UPDATE order_customer
	SET status = 'Complete'
	WHERE order_id = order_id_arg;
$$;


CREATE PROCEDURE change_status_cancel_order(order_id_arg INT, proc_sku_arg INT, cool_sku_arg INT, ram_sku_arg INT, ram_amount_arg INT, motherboard_sku_arg INT, graphics_card_sku_arg INT, hdd_sku_arg INT,
				ssd_sku_arg INT, power_supply_sku_arg INT, case_sku_arg INT)
LANGUAGE SQL
AS $$
	UPDATE order_customer
	SET status = 'Cancel'
	WHERE order_id = order_id_arg;

	UPDATE processor
	SET amount = amount + 1
	WHERE processor.sku = proc_sku_arg;

	UPDATE cooling
	SET amount = amount + 1
	WHERE cooling.sku = cool_sku_arg;

	UPDATE ram
	SET amount = amount + ram_amount_arg
	WHERE ram.sku = ram_sku_arg;

	UPDATE motherboard
	SET amount = amount + 1
	WHERE motherboard.sku = motherboard_sku_arg;
	
	UPDATE graphics_card
	SET amount = amount + 1
	WHERE graphics_card.sku = graphics_card_sku_arg;
	
	UPDATE hard_disc_drive
	SET amount = amount + 1
	WHERE hard_disc_drive.sku = hdd_sku_arg;

	UPDATE solid_state_drive
	SET amount = amount + 1
	WHERE solid_state_drive.sku = ssd_sku_arg;

	UPDATE power_supply
	SET amount = amount + 1
	WHERE power_supply.sku = power_supply_sku_arg;

	UPDATE case_pc
	SET amount = amount + 1
	WHERE case_pc.sku = case_sku_arg;
$$;

CALL insert_data_to_tables();

