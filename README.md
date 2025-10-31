### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/mail-order-invoice-DynamicSQL.git
cd mail-order-invoice-DynamicSQL
```

### 2. Database Setup

#### 2.1 Database Setup (One-time, as ROOT)

connect as root
method 1: using gcloud CLI
```bash
gcloud sql connect [db_name] --user=root
```
method 2: using MySQL client
```bash
mysql --host=[IPv4 address] --user=root –-password
```
   
create database and load schema
```sql
CREATE DATABASE mail_order;
USE mail_order;
C:/.../sql/cr_mailorder.sql
```
   
verify tables
```sql
SHOW TABLES;
```

create user and grant permissions to user
```sql
-- if user doesn't already exist:
CREATE USER 'username' IDENTIFIED BY 'password';
-- run even if user exists
GRANT ALL PRIVILEGES ON [db_name].* TO 'username';
```
   
exit
```sql
exit
```

#### 2.2 Database Usage

connect to database
method 1: using gcloud CLI
```bash
gcloud sql connect neu-test-db --user=YOUR_USERNAME
```
method 2: using MySQL client
```bash
mysql --host=YOUR_CLOUD_SQL_IP --user=YOUR_USERNAME --password
```
   
use the database
```sql
USE mail_order;
```
   
example queries
```sql
-- View all tables
SHOW TABLES;

-- View table structure
DESCRIBE customer;
DESCRIBE orders;

-- Query data
SELECT * FROM customers;
```

exit
```sql
exit
```

### 3. Python Setup

#### 3.1. Set Up Virtual Environment

create virtual environment
```bash
py -m venv dbenv
```
   
activate virtual environment (you should see (dbenv) in prompt)
```bash
dbenv\Scripts\activate
```
   
install dependencies
```bash 
pip install -r requirements.txt
```
    
verify installation
```
pip list
```

### 3.2. Create `config/db_config.json`

```json
{
    "user": "YOUR_USERNAME",
    "password": "YOUR_PASSWORD",
    "host": "YOUR_CLOUD_SQL_IP",
    "database": "mail_order"
}
```
