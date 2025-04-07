# Late Show API

A Flask API for managing episodes, guests, and appearances on a late night talk show.

## Setup

1. Install dependencies:
```bash
pip install flask flask-sqlalchemy flask-migrate
```

2. Initialize database:
```bash
flask db init
flask db migrate
flask db upgrade
```

3. Seed the database:
```bash
python seed.py
```

4. Run the application:
```bash
python app.py
```

## API Endpoints

### GET /episodes
Returns all episodes

### GET /episodes/:id
Returns a specific episode with appearances

### GET /guests
Returns all guests

### POST /appearances
Creates a new appearance

## Data Models

- **Episode**: date, number
- **Guest**: name, occupation
- **Appearance**: rating (1-5), episode_id, guest_id
