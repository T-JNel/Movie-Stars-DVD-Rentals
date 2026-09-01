class Customer:
    def __init__(self, name, email, movies_rented=None, fines_owed=0.0):
        self.__name = name
        self.__email = email
        self.__movies_rented = movies_rented if movies_rented is not None else []
        self.__fines_owed = float(fines_owed)

    #   Getters

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def getMoviesRented(self):
        return list(self.__movies_rented)

    def getFinesOwed(self):
        return self.__fines_owed

    #   Setters

    def setEmail(self, new_email):
        self.__email = new_email

    #   Behaviour Methods

    def rentMovie(self, movie):
        """Add movie title to customer's rent list."""
        self.__movies_rented.append(movie)

    def returnMovie(self, movie):
        """Remove title from customer's rent list."""
        if movie in self.__movies_rented:
            self.__movies_rented.remove(movie)
            return True
        return False

    def addFine(self, amount):
        """Increase customer's outstanding fine."""
        if amount > 0:
            self.__fines_owed += amount

    def payFine(self, amount):
        """Reduce customer's outstanding fines by amount"""
        if amount <= 0:
            return 0.0
        actual = min(amount, self.__fines_owed)
        self.__fines_owed -= actual
        return actual

    #   Serialization helpers

    def toFileString(self):
        """
        Convert this Customer into a single line for saving to Customers.txt.
        Format: name|email|fines_owed|movie1|movie2|movie3
        """
        movies_str = ",".join(self.__movies_rented)
        return f"{self.__name}|{self.__email}|{self.__fines_owed}|{movies_str}"

    @staticmethod
    def fromFileString(line):
        """Rebuild Customer object from a line previously written by toFileString()."""
        parts = line.strip().split("|")
        if len(parts) < 4:
            return None
        name, email, fines, movies_str = parts[0], parts[1], parts[2], parts[3]
        movies = movies_str.split(",") if movies_str else []
        try:
            fines_value = float(fines)
        except ValueError:
            fines_value = 0.0
        return Customer(name, email, movies, fines_value)

    def __str__(self):
        return f"{self.__name} ({self.__email}) - Fines: R{self.__fines_owed:.2f} - Rented: {self.getMoviesRented()}"