## BREWERIES API

## Tech Stack
- Django
- Db Sqlite

## Installation and Dependencies for local
- Download project repository

- Set up virtual environment on project directory

```
# Create venv file
python -m venv venv (windows)
python3 -m venv venv (macOS or Linux)

# Activate virtual environment
./venv/scripts/activate (windows)
soruce venv/bin/activate (macOS or Linux)

# Install requirements
pip install -r requirements.txt

```

- Change name env_example file to .env


## Usage

- For Documentation [redoc](http://localhost:8000/redoc)

- Open [swagger](http://localhost:8000/api/swagger)

- Create account on swagger /register request

- Login your account and obtain access token and copy.

- Open swagger authenticate and paste the token and login.

- After login successfully you can request every endpoint on swagger

- You can also request these url on [grqphql](http://localhost:8000/graphql)

### Restrictions
- You can make every request with user token.

### Design and Logic
- Authorization system (jwt)
- Database ( user )
- Request validation for get clean user informations
- Graphql queries
- Meaningful exceptions and Structured response
- Logical logs for users
- Clean code and code explanaiton
- Easy test with on swagger

