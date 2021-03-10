# Project - Thomas Plant

My project idea, is to make a system for an automated cocktail bar, incorporating customers, orders, what goes into each drink, and payment. It should include a database using relationships to tie at least 2 of the tables together, a functioning front-end website that will encorporate CRUD application, and a Kanban board made using Trello to document everything that needs to be done and what is still yet to be completed.
### What tables will I need?
* Customer
* Order
* Drinks
* Payment
* Bartender  


![datatables](https://user-images.githubusercontent.com/79214361/110125741-965d8600-7dbb-11eb-9f87-58687a695df6.png)  

Each of the different tables will contain columns that will each need to be formatted into different data types.


### Creating the Database
#### Connecting the database and the virtual machine to the SQL instance

![import](https://user-images.githubusercontent.com/79214361/110126068-f0f6e200-7dbb-11eb-8929-22eba9d32459.png)  

These commands are importing the 'Flask' features from the flask module installed onto this virtual machine.  
The 'app.config' commands are referencing the SQL instance, user and directory that the VM will be connecting to.  

#### Designing the tables and what data/data types they will contain
 
![image](https://user-images.githubusercontent.com/79214361/110502835-77c8f900-80f3-11eb-8de4-4f12d565572e.png)

Each column in the table is being assigned a data type depending on what type of data it is, as well as whether or not that field needs to be filled out or not. The 'ForeignKey' fields are using the data from other tables to fill in the fields.

#### Creating a second module and filling the fields with data

![image](https://user-images.githubusercontent.com/79214361/110130710-3bc72880-7dc1-11eb-909f-baca01a9a1e4.png)  

In a seperate module, I imported all of the tables from the 'app.py' so that I could then fill them with data, without affecting the main branch.  

I later found that the orders table couldn't be imported and filled in until the rest of the of the tables had been commited, assumably because it uses foreign keys from the other tables which needed to be generated before the foreign key can access it.

![image](https://user-images.githubusercontent.com/79214361/110502200-e5285a00-80f2-11eb-8d80-ab5460ae60ff.png)  

![image](https://user-images.githubusercontent.com/79214361/110502522-2c164f80-80f3-11eb-9d4a-c12796df3872.png)  

### Testing the app.py file
