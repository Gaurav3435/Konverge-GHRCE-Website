
# Konverge-GHRCE-Website

Konverge-GHRCE is a web platform build for demonstrating work conducted in the Lab. It can be used for managing purpose. It supports event registrations, schedules, and admin controls to streamline the event process.

## Features

- **User Authentication**: Secure login system for both participants and organizers.
- **Event Registration**: Allows participants to register for various events and competitions.
- **Schedule Display**: Real-time display of event schedules for easy tracking.
- **Admin Panel**: Manage and track events and participants efficiently.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python with Django framework
- **Database**: SQLite for lightweight storage

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Gaurav3435/Konverge-GHRCE-Website.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Konverge-GHRCE-Website
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations to configure the database:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

   Access the website locally at `http://127.0.0.1:8000/`.


