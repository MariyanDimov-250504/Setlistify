# Setlistify - Concert Setlist Archive
Django web application for cataloging concerts and setlists.

## Project Structure
- bands - Band management
- songs - Song management
- concerts - Concert and setlist management

### Setup Instructions
1. Clone the repository
2. Create virtual environment: `python -m venv .venv`
3. Activate virtual environment
4. Install dependencies: `pip install -r requirements.txt`
5. Create PostgreSQL database named `setlistify_db`
6. Create `.env` file with:

DB_NAME=setlistify_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your_secret_key
DEBUG=True

7. Run migrations: `python manage.py migrate`
8. Start server: `python manage.py runserver`

#### Environment Variables
| Variable | Description |
|----------|-------------|
| DB_NAME | PostgreSQL database name |
| DB_USER | Database user |
| DB_PASSWORD | Database password |
| DB_HOST | Database host (default: localhost) |
| DB_PORT | Database port (default: 5432) |
| SECRET_KEY | Django secret key |
| DEBUG | Debug mode (True/False) |


