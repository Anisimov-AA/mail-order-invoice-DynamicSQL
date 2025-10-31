### 1. Clone Repository

```bash
git clone https://github.com/Anisimov-AA/mail-order-invoice-DynamicSQL.git
```

```bas
cd mail-order-invoice-DynamicSQL
```

### 2. Database Setup

#### Database Setup (One-time, as ROOT)

1. connect as root   
using gcloud CLI / using MySQL client / using MySQL locally
```bash
gcloud sql connect [db_name] --user=root
```
```bash
mysql --host=[IPv4 address] --user=root –-password
```
```bash
mysql -u root -p
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
-- check all users
SELECT user, host FROM mysql.user;
-- if user doesn't already exist:
CREATE USER 'username' IDENTIFIED BY 'password';
-- run even if user exists
GRANT ALL PRIVILEGES ON [db_name].* TO 'username';
```
   
5. exit
```sql
exit
```

#### Database Usage

1. connect to database
using gcloud CLI / using MySQL client / using MySQL locally
```bash
gcloud sql connect neu-test-db --user=YOUR_USERNAME
```
```bash
mysql --host=YOUR_CLOUD_SQL_IP --user=YOUR_USERNAME --password
```
```bash
mysql -u YOUR_USERNAME -p
```
   
2. use the database
```sql
USE mail_order;
```
   
3. example queries
```sql
-- view all tables
SHOW TABLES;

-- view table structure
DESC customers;

-- query data
SELECT * FROM customers;
```

4. exit
```sql
exit
```

### 3. Python Setup

#### Set Up Virtual Environment

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

#### Create `config/db_config.json`

```json
{
    "user": "YOUR_USERNAME",
    "password": "YOUR_PASSWORD",
    "host": "YOUR_CLOUD_SQL_IP/localhost",
    "database": "mail_order"
}
```
