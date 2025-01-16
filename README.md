# Django Blog Project

A blogging platform built with Django. This project provides a robust system for creating, managing, and sharing blog posts with a clean, user-friendly interface.

## Features

- User authentication and authorization
- Create, edit, and delete blog posts
- Rich text editor for writing posts
- Comment system
- User profiles
- Responsive design
- Search functionality
- Tags and categories

## Tech Stack

- Python 3.x
- Django 4.x
- SQLite (development) / PostgreSQL (production)
- HTML/CSS
- JavaScript

## Project Setup

1. Clone the repository
```bash
git clone https://github.com/mohitshw/Blogs
cd Blogs
```

2. Create and activate virtual environment
```bash
# Windows
python -m venv benv
benv\Scripts\activate

# Linux/Mac
python -m venv benv
source benv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser
```bash
python manage.py createsuperuser
```

6. Run development server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Project Structure
```
blog_project/
│
├── apps/
│   ├── accounts/         # User authentication and profiles
│   └── blog/             # Core blogging functionality
│
├── static/               # Static files (CSS, JS, Images)
├── templates/            # HTML templates
├── config/              # Project configuration
├── manage.py
├── requirements.txt
└── README.md
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Development Guidelines

- Follow PEP 8 style guide for Python code
- Write tests for new features
- Update documentation when adding new features
- Use meaningful commit messages

## Environment Variables

Create a `.env` file in the root directory and add the following variables:
```
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
```

## Testing
```bash
python manage.py test
```

## Deployment

Deployment instructions will be added soon...

## License

Soon...

## Contact

Your Name - themohitsha@gmail.com
Project Link: [https://github.com/mohitshw/Blogs](https://github.com/mohitshw/Blogs)

## Acknowledgments

- Django Documentation
- Python Community
- All contributors