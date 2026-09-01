# Movie-Stars-DVD-Rentals

School assignment turned practice project.

Scenario:

Movie Stars DVD Rentals is a small but busy video rental store that rents out DVDs and Blu-ray movies to customers in the local community. The store currently manages its records manually using text files, which often leads to errors such as lost rental information, incorrect fines, and difficulty tracking available movies.
To improve efficiency, the company has decided to develop a simple Python-based Movie Rental Management System. The system must allow staff to manage customers, track rented movies, calculate fines for late returns, and store all data in text files for future use.
You have been appointed as a junior developer to design and implement this system.

What was required in the assignment:
1.	Project Structure
Create the following Python files:
•	MovieMain.py – Main program (menu-driven application) 
•	MovieClass.py – Contains the Customer class 
Ensure proper file organisation and separation of logic.

2.	Customer Class (MovieClass.py)
Create a Customer class with the following requirements:
•	Attributes (Private)
•	Customer Name (string) 
•	Customer Email (string) 
•	Movies Rented (list) 
•	Fines Owed (float or integer) 
Methods
•	rentMovie(movie) – Adds a movie to the customer’s rented list 
•	returnMovie(movie) – Removes a movie from the rented list 
•	payFine(amount) – Reduces the customer’s outstanding fines 
Ensure proper encapsulation (use private attributes where appropriate).

3.	Main Application Logic (MovieMain.py)
The application must run continuously until the user chooses to exit.
Data Loading
•	Load movies from Movies.txt into a list or dictionary 
•	Load customers from Customers.txt (if file exists) 
•	Create Customer objects for each loaded customer and store them in a list

4.	Main Menu System
Display the following menu:
•	1 Rent Movie 
•	2 Add Customer 
•	3 Return Movie 
•	4 View Outstanding Rentals 
•	5 View Outstanding Fines 
•	6 Pay Fines 
•	0 Exit System

5.	Functional Requirements 
•	Option 1: Rent Movie
o	If no customers exist, prompt to create one 
o	Display available movies 
o	Allow selection of movie 
o	Display customers and allow selection 
o	Decrease available copies of selected movie 
o	Add movie to selected customer’s rented list

•	Option 2: Add Customer
o	Prompt for: 
	Customer name 
	Customer email 
o	Create Customer

•	Option 3: Return Movie
o	Display customers and their rented movies 
o	Select customer and movie to return 
o	Increase available copies of movie 
o	Remove movie from customer 
o	Ask if movie is late: 
	If yes, enter number of days late 
	Calculate fine: R5 per day 
	Add fine to customer account 

•	Option 4: View Outstanding Rentals
o	Display all customers and movies currently rented 

•	Option 5: View Outstanding Fines
o	Display customers with outstanding fines 

•	Option 6: Pay Fines
o	Display customers with fines 
o	Select customer 
o	Enter payment amount 
o	Deduct amount from fines owed 

•	Option 0: Exit System
o	Save all customer data to Customers.txt 
o	Save all movie data to Movies.txt 
o	Close the application safely

6.	Programming Requirements
•	Use functions to structure the program logically 
•	Include meaningful comments throughout the code 
•	Ensure input validation (where applicable) 
•	Proper use of lists/dictionaries 
•	Clean and readable code structure

What I want to add for practice:

1. Search function for movies
2. Sort option
3. Input validation
4. Movie categories
5. A movie class
6. Inheritance
7. Operator Overloading
8. CSV instead of .txt
9. Rental History Log
10. Data backups
11. Overdue detection by date
12. Rental limits
13. Fine caps
14. Simple GUI
15. Unit tests
16. Exception classes

Tools I will be using:
Coding:
- GitHub Desktop
- VS Code
- Python

