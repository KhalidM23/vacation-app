# Vacation Share Platform

A web application for travelers to share and discover vacation experiences. Users can create detailed vacation posts with itineraries, bookmark favorite trips, and get inspired for their next adventure.

## Features

### User Authentication
- Secure user registration and login system
- Password hashing for security
- Session management with Flask-Login

### Vacation Management
- **Create Vacations**: Share your trips with destination, dates, total cost, and tips
- **Edit & Delete**: Full control over your vacation posts
- **View Details**: Comprehensive vacation pages with all information

### Itinerary System
- Add multiple activities to each vacation
- Track individual activity costs and dates
- Delete specific itinerary items

### Bookmarking
- Save favorite vacations for later reference
- Toggle bookmarks on/off easily
- View all bookmarked vacations in one place

### User-Specific Features
- My Vacations page - manage all your posts
- My Bookmarks page - access saved vacations
- Only vacation owners can edit/delete their posts

## Tech Stack

**Backend:**
- Python 3.13
- Flask (Web Framework)
- Flask-SQLAlchemy (Database ORM)
- Flask-Login (Authentication)
- SQLite (Database)

**Frontend:**
- HTML5
- Bootstrap 5.3 (CSS Framework)
- Jinja2 (Templating)

**Security:**
- Werkzeug password hashing
- Session-based authentication
- Protected routes with `@login_required`

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/KhalidM23/vacation-app.git
cd vacation-app
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows Git Bash
# OR
venv\Scripts\activate  # On Windows CMD
```

3. **Install dependencies**
```bash
pip install flask flask-sqlalchemy flask-login
```

4. **Run the application**
```bash
python app.py
```

5. **Open your browser**
```
http://localhost:5000
```

## Project Structure
```
vacation-app/
├── app.py                 # Main application file with routes
├── models.py              # Database models
├── templates/             # HTML templates
│   ├── base.html         # Base template with navbar
│   ├── home.html         # Landing page
│   ├── login.html        # Login page
│   ├── signup.html       # Registration page
│   ├── vacations.html    # Browse all vacations
│   ├── my_vacations.html # User's vacations
│   ├── my_bookmarks.html # Bookmarked vacations
│   ├── view_vacation.html # Vacation detail page
│   ├── create_vacation.html # Create new vacation
│   ├── edit_vacation.html # Edit vacation
│   └── add_itinerary.html # Add activity to itinerary
├── instance/
│   └── vacations.db      # SQLite database
└── venv/                 # Virtual environment (not tracked)
```

## Database Schema

### Users Table
- `id` (Primary Key)
- `username` (Unique)
- `password_hash`

### Vacations Table
- `id` (Primary Key)
- `destination`
- `start_date`
- `end_date`
- `total_cost`
- `tips`
- `user_id` (Foreign Key)

### Itineraries Table
- `id` (Primary Key)
- `activity`
- `date_of_activity`
- `cost_of_activity`
- `vacation_id` (Foreign Key)

### Bookmarks Table
- `id` (Primary Key)
- `user_id` (Foreign Key)
- `vacation_id` (Foreign Key)

## Usage

1. **Sign Up**: Create an account with username and password
2. **Browse**: View all vacations shared by the community
3. **Create**: Share your vacation with details and itinerary
4. **Bookmark**: Save interesting vacations for future reference
5. **Manage**: Edit or delete your own vacation posts

## Future Enhancements

- [ ] Search and filter vacations by destination or cost
- [ ] User profiles with travel statistics
- [ ] Photo uploads for vacations
- [ ] Comments and ratings system
- [ ] Copy/customize other users' vacations
- [ ] Export itinerary as PDF
- [ ] Social sharing features

## Author

Khalid Mohamed - [GitHub Profile](https://github.com/KhalidM23)

## Acknowledgments

- Built with Flask and Bootstrap
- Learning project for web development and user authentication
- Special thanks to the Flask and Bootstrap communities

## Acknowledgments

- Built with Flask and Bootstrap
- Learning project for web development and deployment