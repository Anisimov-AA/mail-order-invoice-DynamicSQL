### 1. Clone Repository

```bash
https://github.com/Anisimov-AA/mail-order-invoice-DynamicSQL.git
cd mail-order-invoice-DynamicSQL
```

### 2. Database Setup

#### 2.1 Database Setup (One-time, as ROOT)

1. connect as root   
method 1: using gcloud CLI / method 2: using MySQL client
```bash
gcloud sql connect [db_name] --user=root
```
```bash
mysql --host=[IPv4 address] --user=root –-password
```
   
2. create database and load schema
```sql
CREATE DATABASE mail_order;
USE mail_order;
C:/.../sql/cr_mailorder.sql
```
   
3. verify tables
```sql
SHOW TABLES;
```

4. create user and grant permissions to user
```sql
-- if user doesn't already exist:
CREATE USER 'username' IDENTIFIED BY 'password';
-- run even if user exists
GRANT ALL PRIVILEGES ON [db_name].* TO 'username';
```
   
5. exit
```sql
exit
```

#### 2.2 Database Usage

1. connect to database
method 1: using gcloud CLI / method 2: using MySQL client
```bash
gcloud sql connect neu-test-db --user=YOUR_USERNAME
```
```bash
mysql --host=YOUR_CLOUD_SQL_IP --user=YOUR_USERNAME --password
```
   
2. use the database
```sql
USE mail_order;
```
   
3. example queries
```sql
-- View all tables
SHOW TABLES;

-- View table structure
DESCRIBE customer;
DESCRIBE orders;

-- Query data
SELECT * FROM customers;
```

4. exit
```sql
exit
```

### 3. Python Setup

#### 3.1. Set Up Virtual Environment

1. create virtual environment
```bash
py -m venv dbenv
```
   
2. activate virtual environment (you should see (dbenv) in prompt)
```bash
dbenv\Scripts\activate
```
   
3. install dependencies
```bash 
pip install -r requirements.txt
```
    
4. verify installation
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
