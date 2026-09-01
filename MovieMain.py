import os
from MovieClass import Customer

MOVIES_FILES = "Movies.txt"
CUSTOMERS_FILE = "Customers.txt"
FINE_PER_DAY = 5

def load_movies():
    """Load movies from Movies.txt into {title: {"total": int, "available": int}}."""
    movies = {}
    if not os.path.exists(MOVIES_FILES):
        return movies
    try:
        with open(MOVIES_FILES, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) != 3:
                    continue
                title, total, available = parts
                try:
                    movies[title] = {"total": int(total), "available": int(available)}
                except ValueError:
                    continue
    except IOError as e:
        print(f"Could not read {MOVIES_FILES}: {e}")
    return movies

def load_customers():
    """Load customers from Customers.txt into a list of Customer objects."""
    customers = []
    if not os.path.exists(CUSTOMERS_FILE):
        return customers
    try:
        with open(CUSTOMERS_FILE, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                customer = Customer.fromFileString(line)
                if customer is not None:
                    customers.append(customer)
    except IOError as e:
        print(f"Could not read {CUSTOMERS_FILE}: {e}")
    return customers

def save_movies(movies):
    try:
        with open(MOVIES_FILES, "w") as f:
            for title, info in movies.items():
                f.write(f"{title}|{info['total']}|{info['available']}\n")
    except IOError as e:
        print("Could not save {MOVIES_FILES}: {e}")

def save_customers(customers):
    try:
        with open(CUSTOMERS_FILE, "w") as f:
            for customer in customers:
                f.write(customer.toFileString() + "\n")
    except IOError as e:
        print(f"Could not save {CUSTOMERS_FILE}: {e}")

def get_int_input(promt, min_value=None):
    while True:
        raw = input(promt)
        try:
            value = int(raw)
            if min_value is not None and value < min_value:
                print(f"Please enter a number >= {min_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input - please enter a whole number.")

def get_float_input(prompt, min_value=None):
    while True:
        raw = input(prompt)
        try:
            value = float(raw)
            if min_value is not None and value < min_value:
                print(f"Please enter a number >= {min_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input - please enter a number.")

def choose_from_list(items, label):
    if not items:
        print(f"No {label} available.")
        return None
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")
    choice = get_int_input(f"Select a {label} (0 to cancel): ", min_value=0)
    if choice == 0 or choice > len(items):
        return None
    return items[choice - 1]

def rent_movie(movies, customers):
    if not customers:
        print("No customers exist yet - please add one first.")
        add_customer(customers)
        if not customers:
            return
    available_titles = [t for t, info in movies.items() if info["available"] > 0]
    if not available_titles:
        print("No movies currently avaiable to rent.")
        return
    print("\nAvailable movies:")
    title = choose_from_list(available_titles, "movie")
    if title is None:
        return
    print("\nCustomers")
    names = [c.getName() for c in customers]
    chosen_name = choose_from_list(names, "customer")
    if chosen_name in None:
        return
    customer = next(c for c in customers if c.getName() == chosen_name)
    movies[title]["available"] -= 1
    customer.rentMovie(title)
    print(f"'{title}' rented to {customer.getName()}.")

def add_customer(customers):
    name = input("Customer name: ").strip()
    email = input("Customer email: ").strip()
    if not name or not email:
        print("Name and email are required - customer not added.")
        return
    customers.append(Customer(name, email))
    print(f"Customer '{name}' added.")

def return_movie(movies, customers):
    renting_customers = [c for c in customers if c.getMoviesRented()]
    if not renting_customers:
        print("No customers currently have movies rented out.")
        return
    print("\nCustomers with rentals:")
    for c in renting_customers:
        print(f"- {c.getName()}: {c.getMoviesRented()}")
        names = [c.getName() for c in renting_customers]
        chosen_name = choose_from_list(names, "customer")
        if chosen_name is None:
            return
        customer = next(c for c in renting_customers if c.getName() == chosen_name)
        movie = choose_from_list(customer.getMoviesRented(), "movie")
        if movie is None:
            return
        customer.returnMovie(movie)
        if movie in movies:
            movies[movie]["available"] += 1
        late = input("Was this movie returned late? (y/n): ").strip().lower
        if late == "y":
            days_late = get_int_input("How many days late? ", min_value=1)
            fine = days_late * FINE_PER_DAY
            customer.addFine(fine)
            print(f"Fine of R{fine} added to {customer.getName()}'s account.")

def view_outstanding_rentals(customers):
    any_rentals = False
    for c in customers:
        rented = c.getMoviesRented()
        if rented:
            any_rentals = True
            print(f"{c.getName()}: {rented}")
    if not any_rentals:
        print("No movies are currently rented out.")

def view_outstanding_fines(customers):
    any_fines = False
    for c in customers:
        if c.getFinesOwed() > 0:
            any_fines = True
            print(f"{c.getName()}: R{c.getFinesOwed():.2f}")
    if not any_fines:
        print("No outstanding fines.")

def pay_fines(customers):
    owing = [c for c in customers if c.getFinesOwed() > 0]
    if not owing:
        print("No customers currently owe fines.")
        return
    print("\nCustomers with fines:")
    for c in owing:
        print(f"- {c.getName()}: R{c.getFinesOwed():.2f}")
    names = [c.getName() for c in owing]
    chosen_name = choose_from_list(names, "customer")
    if chosen_name is None:
        return
    customer = next(c for c in owing if c.getName() == chosen_name)
    amount = get_float_input("Payment amount: R", min_value=0.01)
    paid = customer.payFine(amount)
    print(f"R{paid:.2f} paid. Remaining balance: R{customer.getFinesOwed():.2f}")

def print_menu():
    print("\n=== Movie Stars DVD Rentals ===")
    print("1. Rent Movie.")
    print("2. Add Customer.")
    print("3. Return Movie.")
    print("4. View Outstanding Rentals.")
    print("5. View Outstanding Fines.")
    print("6. Pay Fines.")
    print("0. Exit System.")

def main():
    movies = load_movies()
    customers = load_customers()
    while True:
        print_menu()
        choice = get_int_input("Enter your choice: ")
        if choice == 1:
            rent_movie(movies, customers)
        elif choice == 2:
            add_customer(customers)
        elif choice == 3:
            return_movie(movies, customers)
        elif choice == 4:
            view_outstanding_rentals(customers)
        elif choice == 5:
            view_outstanding_fines(customers)
        elif choice == 6:
            pay_fines(customers)
        elif choice == 0:
            save_customers(customers)
            save_movies(movies)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid option - please choose a number from the menu.")

if __name__ == "__main__":
    main()