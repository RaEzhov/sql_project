# SQL project
SQL database and Python GUI for PC workshop
  
Vendor code is column 'sku'  
1129 is example of sku  
First figure is type of part  
	1 - processor  
	2 - motherboard   
	3 - graphics card  
	4 - ram  
	5 - cooling  
	6 - power supply  
	7 - hard disk drive  
	8 - solid state drive  
	9 - case  
  
Sku of processor (1XXX)  
Second figure is manufacturer  
	1 - Intel  
	2 - AMD  
Next figures just numbers in order  
  
Sku of motherboard (2XXX)  
Second figure is manufacturer  
	1 - MSI  
	2 - ASUS  
	3 - GIGABYTE  
	4 - ASRock  
Next figures just numbers in order  
  
Sku of graphics card (3XXX)  
Second figure is chip manufacturer  
	1 - AMD  
	2 - NVIDIA  
Third figure is card manufacturer  
	1 - ASUS  
	2 - GIGABYTE  
	3 - KFA2  
	4 - MSI  
	5 - Palit  
	6 - ZOTAC  
Next figures just numbers in order  
  
Sku of ram (4XXX)  
Second figure is manufacturer  
	1 - Crucial  
	2 - G.Skill  
	3 - Hynix  
	4 - Kingston  
	5 - Patriot  
	6 - Samsung  
Next figures just numbers in order  
  
Sku of cooling (5XXX)  
Second figure is manufacturer  
	1 - AeroCool  
	2 - Arctic Cooling  
	3 - be quiet!  
	4 - CoolerMaster  
	5 - DEEPCOOL  
	6 - Noctua
Next figures just numbers in order  
  
Sku of power supply (6XXX)  
Second figure is manufacturer  
	1 - be quiet!  
	2 - Corsair  
	3 - Cougar  
	4 - DEEPCOOL  
	5 - EVGA    
	6 - FSP  
	7 - Seasonic  
	8 - Thermaltake
Next figures just numbers in order  
  
Sku of solid state drive (7XXX)  
Second figure is manufacturer  
	1 - Kingston  
	2 - Samsung   
Third figure is type (2.5 or m.2)  
	 1 - 2.5  
	 2 - m.2  
Next figures just numbers in order  

Sku of solid state drive (8XXX)  
Second figure is manufacturer  
	1 - Seagate  
	2 - WD  
Next figures just numbers in order  
  
Sku of case (9XXX)  
Second figure is manufacturer  
	1 - AeroCool  
	2 - be quiet!  
	3 - CoolerMaster  
	4 - Corsair  
	5 - Cougar  
	6 - DEEPCOOL  
	7 - Fractal Design  
	6 - NZXT  
	9 - Thermaltake  
Next figures just numbers in order  
  
How to add new product  
Press to "New product" button. Enter sku.  
if this sku already exists then user enter amont of new products and this number adds to old value.  
if this slu is not exists then user enter all information about product and this cortege adds to table.  

drop_all_tables() - delete all tables  
clear_all_tables() - clear information from all tables  
create_all_tables() - create all 11 tables  
insert_proc(all rows from processor) - insert data row into table processor  
insert_cool(all rows from coll) - insert data row into table cooling  
insert_motherboard(all rows from motherboard) - insert data row into table motherboard  
insert_gpu(all rows from graphics_card) - insert data row into table graphics_card  
insert_ram(all rows from ram) - insert data row into table ram  
insert_power_supply(all rows from power_supply) - insert data row into table power_supply
insert_case_pc(all rows from case_pc) - insert data row into table case_pc  
insert_case_hdd(all rows from hard_disc_drive) - insert data row into table hard_disc_drive  
insert_case_ssd(all rows from solid_state_drive) - insert data row into table solid_state_drive  
insert_case_order_customer(all rows from order_customer) - insert data row into table order_customer  
insert_case_customer(all rows from customer) - insert data row into table customer  
return_proc() - return all rows from processor
return_cool() - return all rows from cooling
return_motherboard() - return all rows from motherboard
return_gpu() - return all rows from graphics_card
return_ram() - return all rows from ram
return_power_supply() - return all rows from power_supply
return_case_pc() - return all rows from case_pc
return_hdd() - return all rows from hard_disc_drive
return_ssd() - return all rows from solid_state_drive
return_order_customer() - return all rows from order_customer
return_customer() - return all rows from customer
insert_data_to_tables() - insert data to all tables for example
change_status_complete_order(order_id_arg INT) - change status from 'In progress' to 'Complete'
change_status_cancel_order(order_id_arg INT, and all sku from order_customer) - change status from 'In progress' to 'Cancel' and returns components to storage

