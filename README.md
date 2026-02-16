# To-Do List Application (Flask)

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0+-green?style=flat&logo=flask)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-orange?style=flat)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)

A modern, responsive To-Do List application built with Flask and SQLAlchemy. Manage your tasks efficiently with features like user authentication, task creation, editing, deletion, and status tracking.

![Home Page](app/static/css/image.png)
*Home Page - View and manage your tasks*

![Login Page](app/static/css/image-1.png)
*Login Page - Secure user authentication*

## ✨ Features

- **User Authentication**: Secure login system to protect your tasks
- **Task Management**: Create, read, update, and delete tasks
- **Status Tracking**: Track task progress with three statuses:
  - 🔴 Pending
  - 🟡 Working
  - 🟢 Completed
- **Toggle Status**: Easily change task status with one click
- **Clear All**: Remove all tasks at once
- **Responsive Design**: Works on desktop and mobile devices
- **Modern UI**: Clean and attractive interface with gradient styling

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, JavaScript
- **Template Engine**: Jinja2

## 📋 Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

## 🚀 Installation

1. **Clone the repository**
   
```
bash
   git clone https://github.com/SonawaneKalpesh/To-Do-list-application-Flask.git
   cd To-Do-list-application-Flask
   
```

2. **Create a virtual environment (optional but recommended)**
   
```
bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
```

3. **Install dependencies**
   
```
bash
   pip install flask flask-sqlalchemy
   
```

4. **Run the application**
   
```
bash
   python run.py
   
```

5. **Open your browser**
   Navigate to `http://127.0.0.1:5000`

## 🔑 Default Login Credentials

- **Username**: `admin`
- **Password**: `admin`

> ⚠️ **Security Note**: Change the default credentials in `app/routes/auth.py` for production use.

## 📁 Project Structure

```
To-Do-list-application-Flask/
├── app/
│   ├── __init__.py          # Application factory
│   ├── models.py            # Database models
│   ├── routes/
│   │   ├── auth.py          # Authentication routes
│   │   └── tasks.py         # Task management routes
│   ├── static/
│   │   └── css/
│   │       └── style.css    # Styling
│   └── templates/
│       ├── base.html        # Base template
│       ├── login.html       # Login page
│       ├── register.html    # Registration page
│       ├── tasks.html       # Tasks dashboard
│       └── edit_task.html   # Edit task page
├── instance/
│   └── todo.db             # SQLite database
├── run.py                  # Application entry point
├── test_app.py            # Unit tests
└── README.md              # This file
```

## 🎯 Usage

1. **Login**: Use default credentials to access the dashboard
2. **Add Task**: Enter a task title and click "Add"
3. **Toggle Status**: Click "Toggle" to change task status
4. **Edit Task**: Click "Edit" to modify task title
5. **Delete Task**: Click "Delete" to remove a task
6. **Clear All**: Click "Clear All" to remove all tasks
7. **Logout**: Click "Logout" to end session

## 🧪 Running Tests

```
bash
python -m pytest test_app.py
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

- **Kalpesh Sonawane** - [GitHub](https://github.com/SonawaneKalpesh)

## 🙏 Acknowledgments

- Flask Documentation
- SQLAlchemy Documentation
- Open source community

---

Made with ❤️ using Flask
