"""
Exercise 1:
Create a Pizza class that could have ingredients added to it. Raise an error if an attempt is made to add a duplicate ingredient.
"""
class Pizza:
    def __init__(self):
        self.ingredients = set()
    
    def add_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            raise ValueError(f"The ingredient '{ingredient}' is already added.")
        self.ingredients.add(ingredient)


"""
Exercise 2:
Create an Elevator class with methods to go up, go down, and get the current floor. The elevator should not be able to go below the ground floor (floor 0).
"""
class Elevator:
    def __init__(self):
        self.floor = 0

    def go_up(self):
        self.floor += 1

    def go_down(self):
        self.floor -= 1
        if(self.floor < 0):
            self.floor = 0
        

    def get_current_floor(self):
        return self.floor


"""
Exercise 3:
Create a class Stack with methods to push, pop, and check if the stack is empty. Raise an exception if a pop is attempted on an empty stack.
"""
class Stack:
    def __init__(self):
        """
        Initialize an empty stack with a dynamic list.
        """
        self.st = []  

    def push(self, item):
        """
        Add an item to the top of the stack.
        """
        self.st.append(item)

    def pop(self):
        """
        Remove and return the top item of the stack. Raise an exception if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("The stack is empty")
        return self.st.pop()

    def is_empty(self):
        """
        Check if the stack is empty.
        """
        return len(self.st) == 0



"""
Exercise 4:
Design a BankAccount class with methods to deposit, withdraw, and check balance. Ensure that an account cannot go into a negative balance.
"""
class BankAccount:
    def __init__(self, initial_balance):
        self.bal = initial_balance

    def deposit(self, amount):
        self.bal += amount

    def withdraw(self, amount):
        if self.bal < amount:
            raise ValueError(f"Balance cannot be negative")
        self.bal -= amount

    def check_balance(self):
        return self.bal


"""
Exercise 5:
Create a class Person with attributes for name and age. Implement a method birthday that increases the person's age by one. Raise an exception if an age less than 0 is entered.
"""
class Person:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError(f"Age cannot be negative")
        else:
            self.name = name
            self.age = age

    def birthday(self):
        self.age += 1


"""
Exercise 6:
Create an Animal base class and a Dog and Cat derived classes. Each animal should have a sound method which returns the sound they make.
"""
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"


"""
Exercise 7:
Design a class Calculator with static methods for addition, subtraction, multiplication, and division. Division method should raise a ZeroDivisionError when trying to divide by zero.
"""
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ZeroDivisionError("Division by zero")
        return x / y


"""
Exercise 8:
Create a class `Car` with attributes for speed and mileage. Raise a ValueError if a negative value for speed or mileage is entered.
"""
class Car:
    def __init__(self, speed, mileage):
        if speed < 0 or mileage < 0:
            raise ValueError("Negative sped or mileage is not possible")
        self.speed = speed
        self.mileage = mileage


"""
Exercise 9:
Create a Student class and a Course class. Each Course can enroll students and print a list of enrolled students.
"""
class Student:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self):
        self.students = []

    def enroll(self, student):
        self.students.append(student)

    def print_students(self):
        for course in self.arr:
            print(course)


"""
Exercise 10:
Create a Flight class with a destination, departure time, and a list of passengers. Implement methods to add passengers, change the destination, and delay the flight by a certain amount of time.
"""
from datetime import datetime, timedelta

class Flight:
    def __init__(self, destination, departure):
        self.destination = destination
        self.departure = datetime.strptime(departure, "%H:%M")
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def change_destination(self, new_destination):
        self.destination = new_destination

    def delay(self, delay_time):
        self.departure += timedelta(hours=delay_time)

    def get_departure_time(self):
        return self.departure.strftime("%H:%M")


"""
Exercise 11:
Create a Library class with a list of Book objects. The Book class should have attributes for title and author. The Library class should have methods to add books and find a book by title.
"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book


"""
Exercise 12:
Design a class Matrix that represents a 2D matrix with methods for addition, subtraction, and multiplication. Implement error handling for operations that are not allowed (e.g., adding matrices of different sizes).
"""
class Matrix:
    def __init__(self, matrix):
        """Initialize a 2D matrix."""
        
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if matrix else 0

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")
        
        result = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction")
        
        result = [
            [self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns of the first matrix must equal the number of rows of the second matrix")
        
        result = [
            [sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.cols)) for j in range(other.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)


"""
Exercise 13:
Create a class Rectangle with attributes for height and width. Implement methods for calculating the area and perimeter of the rectangle. Also, implement a method is_square that returns true if the rectangle is a square and false otherwise.
"""
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return self.height + self.width + self.height + self.width

    def is_square(self):
        return self.height == self.width


"""
Exercise 14:
Design a class Circle with attributes for radius. Implement methods for calculating the area and the circumference of the circle. Handle exceptions for negative radius values.
"""

import math
class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Negative radius")
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def circumference(self):
        return math.pi * 2 * self.radius


"""
Exercise 15:
Design a class Triangle with methods to calculate the area and perimeter. Implement error handling for cases where the given sides do not form a valid triangle.
"""
class Triangle:
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Not positive sides")
        
        if (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
            raise ValueError("Not valid")
        
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        s = self.perimeter() / 2
        area = math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
        return area

    def perimeter(self):
        """
        Calculate the perimeter of the triangle.
        """
        return self.side_a + self.side_b + self.side_c


"""
Exercise 16:
Design a class Triangle with methods to calculate the area and perimeter. Implement error handling for cases where the given sides do not form a valid triangle.
"""
class AbstractShape:
    def area(self):
        pass

    def perimeter(self):
        pass

# class Circle(AbstractShape):
#     def __init__(self, radius):
#         pass

# class Rectangle(AbstractShape):
    # def __init__(self, height, width):
        # pass

# class Triangle(AbstractShape):
#     def __init__(self, side_a, side_b, side_c):
#         pass

"""
Exercise 17:
Create a MusicPlayer class that contains a list of songs and methods to add songs, play a song, and skip to the next song. Also implement a method to shuffle the playlist.
"""
import random
class MusicPlayer:
    def __init__(self):
        self.playlist = []  
        self.current_song_index = -1  
        self.current_song = None

    def add_song(self, song):
        self.playlist.append(song)

    def play_song(self):
        if self.current_song_index == -1: 
            self.current_song_index = 0  
        self.current_song = self.playlist[self.current_song_index]

    def next_song(self):
        self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
        self.current_song = self.playlist[self.current_song_index]

    def shuffle(self):
        random.shuffle(self.playlist)  
        self.current_song_index = 0  


"""
Exercise 18:
Design a Product class for an online store with attributes for name, price, and quantity. Implement methods to add stock, sell product, and check stock levels. Include error handling for attempting to sell more items than are in stock.
"""

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, quantity):
        self.quantity += quantity

    def sell(self, quantity):
        if quantity > self.quantity:
            raise ValueError(f"Trying to sell more")
        self.quantity -= quantity

    def check_stock(self):
        return self.quantity


"""
Exercise 19:
Create a VideoGame class with attributes for title, genre, and rating. Implement methods to change the rating, change the genre, and display game details.
"""

class VideoGame:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def change_rating(self, rating):
        self.rating = rating

    def change_genre(self, genre):
        self.genre = genre

    def display_details(self):
        print(f"Video game with rating {self.rating} and title {self.title} and genre {self.genre}")


"""
Exercise 20:
Create a School class with a list of Teacher and Student objects. Teacher and Student classes should have attributes for name and age. The School class should have methods to add teachers, add students, and print a list of all people in the school.
"""
# class Person:
#     def __init__(self, name, age):
#         pass

# class Teacher(Person):
#     pass

# class Student(Person):
#     pass

class School:
    def __init__(self):
        pass

    def add_teacher(self, teacher):
        pass

    def add_student(self, student):
        pass

    def print_all(self):
        pass

"""
Exercise 21:
Design a Card class to represent a playing card with suit and rank. Then design a Deck class that uses the Card class. The Deck class should have methods to shuffle the deck, deal a card, and check the number of remaining cards.
"""
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Deck:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        self.remaining_cards = self.cards[:] 

    def shuffle(self):
        random.shuffle(self.remaining_cards)

    def deal(self):
        if self.remaining_cards:
            return self.remaining_cards.pop()
        else:
            return None

    def count(self):
        return len(self.remaining_cards)
