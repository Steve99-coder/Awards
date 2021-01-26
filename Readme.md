# Awards

#### Author: [Stephen Nderitu](https://github.com/Steve99-coder/Awards)


* Link to live site: [S-Awards](https://blooming-tor-03493.herokuapp.com/)

## Description
This is an awards app that users can be able to post a project he/she has created and get it reviewed by his/her peers.



## Setup and installations
* Fork the data .
* git clone the award repo.
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.8 manage.py runserver`



## Getting started

### Prerequisites
* python3
* virtual environment
* pip

#### Clone the Repo 
```bash
git clone https://github.com/Steve99-coder/Awards
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3 -m venv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```


#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3 manage.py check
python manage.py makemigrations appawards
python3 manage.py sqlmigrate appawards 0001
python3 manage.py migrate
```

#### Run the app
```bash
python3 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)



## Testing the Application
`python manage.py test`
        
## Technologies Used

* [Python3.8](https://docs.python.org/3/)
* Django 
* Postgresql 
* Boostrap
* HTML

### License

* [[License: MIT]](Licence.md) <stevenderitu99@gmail.com>