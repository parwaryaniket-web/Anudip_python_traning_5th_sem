'''
3. Smart Library Management System 
Problem Statement 
Create a digital library management system. 
Example Structure 
library = { 
    "B101": { 
        "title": "Python Basics", 
        "author": "ABC", 
        "copies": 5 
    } 
} 
Maintain records of at least 30 books. 
Requirements 
1. Add a book.  
2. Remove a book.  
3. Search a book by ID.  
4. Search by title.  
5. Update available copies.  
6. Issue a book.  
7. Return a book.  
8. Display books with fewer than 3 copies.  
9. Display books that are unavailable.  
10. Find the most available book.  
11. Generate a restocking report.  
12. Create a separate dictionary of books requiring immediate purchase.  
Challenge 
Generate a complete library summary report.
'''
# Smart Library Management System

# Library dictionary
library = {
    "B101": {"title": "Python Basics", "author": "ABC", "copies": 5},
    "B102": {"title": "Data Science", "author": "XYZ", "copies": 2},
    "B103": {"title": "AI Fundamentals", "author": "PQR", "copies": 0},
    "B104": {"title": "Web Development", "author": "LMN", "copies": 8},
    "B105": {"title": "Java Programming", "author": "DEF", "copies": 1}
}

# Add more books up to 30 using the same format

# --------------------------------------------------
# 1. Add a Book
# --------------------------------------------------
library["B106"] = {
    "title": "Machine Learning",
    "author": "GHI",
    "copies": 4
}

print("Book Added")

# --------------------------------------------------
# 2. Remove a Book
# --------------------------------------------------
del library["B105"]

print("Book Removed")

# --------------------------------------------------
# 3. Search Book by ID
# --------------------------------------------------
print("\nSearch by ID")
print(library["B101"])

# --------------------------------------------------
# 4. Search Book by Title
# --------------------------------------------------
print("\nSearch by Title")

for book_id, details in library.items():
    if details["title"] == "Python Basics":
        print(details)

# --------------------------------------------------
# 5. Update Available Copies
# --------------------------------------------------
library["B102"]["copies"] = 5

print("\nUpdated Copies")
print(library["B102"])

# --------------------------------------------------
# 6. Issue a Book
# Reduce copies by 1
# --------------------------------------------------
library["B101"]["copies"] = library["B101"]["copies"] - 1

print("\nBook Issued")
print(library["B101"])

# --------------------------------------------------
# 7. Return a Book
# Increase copies by 1
# --------------------------------------------------
library["B101"]["copies"] = library["B101"]["copies"] + 1

print("\nBook Returned")
print(library["B101"])

# --------------------------------------------------
# 8. Display Books with Less Than 3 Copies
# --------------------------------------------------
print("\nBooks with Less Than 3 Copies")

for book_id, details in library.items():
    if details["copies"] < 3:
        print(details["title"])

# --------------------------------------------------
# 9. Display Unavailable Books
# --------------------------------------------------
print("\nUnavailable Books")

for book_id, details in library.items():
    if details["copies"] == 0:
        print(details["title"])

# --------------------------------------------------
# 10. Find Most Available Book
# --------------------------------------------------
max_copies = 0
book_name = ""

for book_id, details in library.items():
    if details["copies"] > max_copies:
        max_copies = details["copies"]
        book_name = details["title"]

print("\nMost Available Book")
print(book_name)

# --------------------------------------------------
# 11. Restocking Report
# Books having less than 3 copies
# --------------------------------------------------
print("\nRestocking Report")

for book_id, details in library.items():
    if details["copies"] < 3:
        print(book_id, details["title"], details["copies"])

# --------------------------------------------------
# 12. Books Requiring Immediate Purchase
# Copies = 0
# --------------------------------------------------
purchase = {}

for book_id, details in library.items():
    if details["copies"] == 0:
        purchase[book_id] = details

print("\nBooks Requiring Purchase")
print(purchase)

# --------------------------------------------------
# Challenge : Complete Library Summary Report
# --------------------------------------------------
print("\n===== LIBRARY SUMMARY REPORT =====")

# Total number of books
print("Total Books =", len(library))

# Total available copies
total_copies = 0

for details in library.values():
    total_copies = total_copies + details["copies"]

print("Total Copies =", total_copies)

# Most available book
print("Most Available Book =", book_name)

# Number of books needing purchase
print("Books Needing Purchase =", len(purchase))