# 📚 Library Database Management System

A Python and SQL-based application designed to manage books, users, and transactions efficiently. The system supports full CRUD operations, tracks issued and returned books, and generates analytical reports for effective library management.

---

## 🚀 Project Overview

The Library Database Management System automates traditional library operations by replacing manual record-keeping with a structured relational database.

It enables:

* 📖 Book inventory management
* 👤 User registration & management
* 🔄 Book issuing & return tracking
* 📊 Analytical reporting

---

## 🎯 Problem Statement

Many small libraries still rely on manual registers to:

* Track issued books
* Monitor returns
* Maintain inventory

This leads to:

* Data inconsistency
* Human errors
* No analytical insights
* Time-consuming operations

---

## 💡 Solution

This system provides:

* Automated book availability tracking
* Real-time issue & return updates
* Structured relational database design
* Analytical SQL reports
* Data integrity using foreign keys

---

## 🛠 Tech Stack

* **Python**
* **MySQL**
* mysql-connector-python
* SQL
* (Optional) pandas & matplotlib for analytics

---

## 🗄 Database Schema

### 📘 Books Table

* book_id (Primary Key)
* title
* author
* category
* total_copies
* available_copies

### 👤 Users Table

* user_id (Primary Key)
* name
* email
* phone

### 🔄 Transactions Table

* transaction_id (Primary Key)
* book_id (Foreign Key)
* user_id (Foreign Key)
* issue_date
* return_date
* status

---

## ⚙ Features

### ✅ Book Management

* Add new books
* View all books
* Update book details
* Delete books

### ✅ User Management

* Register new users
* View user list
* Manage user details

### ✅ Issue & Return System

* Issue books (auto-reduces stock)
* Return books (auto-updates stock)
* Tracks active & completed transactions

### ✅ Analytical Reports

* Most issued books
* Overdue books
* Active users summary

---

## 📊 Business Logic

* Book cannot be issued if available_copies = 0
* Return operation automatically increases stock
* Overdue books identified using date comparison
* Reports generated using SQL aggregation functions

---

## 🖥 How to Run

### 1️⃣ Install Dependencies

```bash
pip install mysql-connector-python
```

### 2️⃣ Create Database

Run in MySQL:

```sql
CREATE DATABASE library_db;
USE library_db;
```

Then create tables using the provided schema.

### 3️⃣ Run Application

```bash
python library_system.py
```

---

## 📁 Project Structure

```
Library_DBMS/
│
├── library_system.py
├── schema.sql
├── README.md
└── requirements.txt
```

---

## 🔐 Future Improvements

* Admin authentication system
* Fine calculation for overdue books
* Dashboard using Streamlit
* Export reports to CSV
* Graphical analytics dashboard
* Web deployment

---

## 📌 Learning Outcomes

This project demonstrates:

* Relational Database Design
* SQL Query Optimization
* Foreign Key Constraints
* CRUD Operations in Python
* Real-world Business Logic Implementation
* Data Analysis using SQL


