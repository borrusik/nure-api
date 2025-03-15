# NURE-RATING: University Professor Rating System

A web application for rating and reviewing university professors, built with Django. This system allows students to provide feedback on professors across different departments and faculties.

## 🌟 Features

- **Professor Ratings**: Students can rate professors on professionalism, clarity of explanations, and attitude toward students
- **Department Rankings**: View departments ranked by average professor ratings
- **Professor Search**: Quickly find professors using the search functionality with autocomplete
- **Statistics**: View top professors and departments based on ratings
- **Privacy-Focused**: IP-based tracking to prevent duplicate reviews
- **Mobile-Friendly**: Responsive design works on all devices
- **Photo Support**: Professors can have profile photos
- **Reporting System**: Report professors for inappropriate behavior

## 📋 Data Structure

- **Faculty**: University faculties (e.g., Computer Science, Engineering)
- **Department**: Academic departments within faculties
- **Professor**: Teaching staff with ratings and feedback
- **Feedback**: Student reviews with ratings for professionalism, clarity, and attitude

## 🛠️ Technical Stack

- **Backend**: Django 5.1
- **Database**: SQLite (can be migrated to PostgreSQL for production)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Deployment**: Ready for Render.com deployment

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/nure-rating.git
   cd nure-rating
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Import sample data (optional)**
   ```bash
   python manage.py import_professors exported_data/
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Web Interface: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## 📂 Project Structure

```
university_feedback/      # Main project directory
├── feedback_app/         # Main application 
│   ├── admin.py         # Admin panel configuration
│   ├── forms.py         # Form definitions
│   ├── models.py        # Database models
│   ├── views.py         # View functions
│   ├── urls.py          # URL routing
│   └── management/      # Custom management commands
├── templates/           # HTML templates
│   ├── base.html        # Base template
│   └── home.html        # Homepage template
├── static/              # Static files (CSS, JS, images)
├── media/               # User-uploaded files
└── university_feedback/ # Project settings
    ├── settings.py      # Django settings
    ├── urls.py          # Main URL configuration
    └── wsgi.py          # WSGI configuration
```

## 🔄 Import Data Format

To import professor data, organize your data in the following format:
```
exported_data/
├── Faculty1/
│   ├── Department1/
│   │   ├── Professor_Name1.txt
│   │   └── Professor_Name1.jpg
│   └── Department2/
│       ├── Professor_Name2.txt
│       └── Professor_Name2.jpg
└── Faculty2/
    └── Department3/
        ├── Professor_Name3.txt
        └── Professor_Name3.jpg
```

## 🚢 Deployment

The project is configured for deployment on Render.com with the following files:
- `build.sh`: Setup script that runs on deployment
- `Procfile`: Specifies the web server (Gunicorn)

## 👥 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact

For questions or support, please contact: wwork8655@gmail.com
