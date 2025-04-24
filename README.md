# Campus Recruitment Management System

A Django-based web application for managing campus recruitment processes, connecting students, alumni, and companies.

## Features

- Multi-user role system:
  - Admin
  - Student
  - Alumni
  - Company
  - Guest
  - User

- Key functionalities:
  - Job post management
  - Internship opportunities
  - Alumni networking
  - User profiles
  - Friend connections
  - Request management

## Technical Stack

- Backend Framework: Django
- Frontend: HTML, CSS, JavaScript
- UI Components:
  - CKEditor
  - Chart.js
  - DataTables
  - Toastr notifications
  - SweetAlert
  - Range Slider
  - Peity Charts
  - Knob.js

## Project Structure

```
├── Admin/
├── Alumni/
├── Company/
├── Guest/
│   └── static/
│       ├── Admin/
│       └── Main/
├── Student/
├── User/
│   └── Templates/
└── Mainproject/
```

## Installation

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

## Configuration

The project uses Django's default settings with:
- Debug mode enabled
- SQLite database
- Standard Django middleware
- Custom apps configured in INSTALLED_APPS

## License

This project includes third-party components with their respective licenses:
- CKEditor: Licensed under GPL, LGPL, and MPL licenses
- Various UI components under MIT license

## Contributing

Feel free to submit issues and pull requests to help improve the project.