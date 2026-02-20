# Setlistify - Concert Setlist Archive
Django web application for cataloging concerts and setlists.

## Project Structure
- bands - Band management
- songs - Song management
- concerts - Concert and setlist management

### Setup Instructions
1. Open Terminal (cmd, PowerShell, git bash)
2. From terminal clone repository in desired folder (use that folder for next setup steps)
2. Via PyCharm open the cloned repository folder (close environment creation if asked)
3. In PyCharm Terminal: 
-- Create virtual environment `python -m venv .venv`
-- Activate virtual environment `.venv\Scripts\activate`
-- Install dependencies `pip install -r requirements.txt`
4. Create `.env` file in root folder with following content:

DB_NAME=setlistify_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your_secret_key
DEBUG=True 

5. Connect to PostgreSQL and create database (read env about filling fields of the DB setup)
6. Run migrations: `python manage.py migrate`
7. Start server: `python manage.py runserver`
