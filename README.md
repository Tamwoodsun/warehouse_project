# selfprojectdjango

# Description
This is a basic warehouse management project, which is created by using ORM models , PostgreSQL and Python Django framework. 


# Version applied in this project
Python: 3.8
Django: 4.12
PostgreSQL: 14.13


# User who use this repository
## Admin
Admin can edit, delete, make any modification of records from the database.
They can also choose to list out the warehouse whether its storage quota is full or not.
## Registered User 
Registered User can view the orders, including when and where to rent
## Unregistered User
Unregistered user can only view the ,but cannot access the 

# Overview of the models

# How to apply to your database?

## Please input the following commands in your command terminal (Ubuntu)
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg\n

sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/jammy pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

apt list --upgradable
sudo apt install pgadmin4
sudo -u postgres psql

You are advised to make connection and changes in the DATABASE array from the path "newprojecttrial/settings.py".

# How to run this django website framework?
Please install the language based on the version applied in this project.

You should type "pip freeze > requirements.txt" to install the python package.

Then you run the server by typing "python manage.py runserver".

# URL Path Planning
## Example from Sir
| Url      | App | REST Method | Description |
| -------- | ---- | ----------- | --- |
| admin    | None   | GET        | Admin Page    |
| about    | Page     | GET        |  About Page  |
| listings |   listings   |    GET         | Overview of Building    |
| listings/<int:id> |  listings    | GET             | Building Specific Information    |
| listings/?page=<number:int> | listings | POST | Show Building in pages
| listings/search?<parameters:int> | listings | POST | Search Any Results
| accounts     | accounts     | GET         |     |
| accounts/login     | accounts     | POST         |  Registered User Login   |
| accounts/register     | accounts     | GET         |  Create a user    |
| accounts/dashboard | accounts     |   GET          | Dashboard of registered user    |
| contacts     |  contacts    | GET         |     |

## Our Map
| Url      | App | REST Method | Description |
| -------- | ---- | ----------- | --- |
| admin    | None   | GET       | Admin Page    |
| about    | Page    | GET        | About Page    |
| error    | Page | GET | Error Page
| service | Page | GET| Service Page
| warehouses | warehouse   |    GET         | Overview of all warehouse    |
| warehouses/<region:str> | warehouse   | GET | Show warehouses from that district |
| warehouses/?page=<number:int> | warehouse | GET | Show warehouses in pages |
| warehouse/<id:int> | warehouse   |    POST         |  Show independent warehouse record  |
| transfer | transfer   |    GET         | show records  |
| transfer/ | transfer |   | |
| user | user | |
| user/dashboard | user | GET | Show his record
| user/login | user |POST | User Login
| user/logout | | |



# warehouse_project
# warehouse_project
# warehouse_project
