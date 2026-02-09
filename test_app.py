import unittest
from app import create_app, db
from app.models import Task

class TestToDoApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            Task.query.delete()
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_login(self):
        response = self.client.post('/login', data={'username': 'admin', 'password': 'admin'})
        self.assertEqual(response.status_code, 302)  # Redirect to tasks

    def test_add_task(self):
        with self.client:
            self.client.post('/login', data={'username': 'admin', 'password': 'admin'})
            response = self.client.post('/add', data={'title': 'Test Task'})
            self.assertEqual(response.status_code, 302)
            with self.app.app_context():
                task = Task.query.first()
                self.assertIsNotNone(task)
                self.assertEqual(task.title, 'Test Task')

    def test_toggle_status(self):
        with self.client:
            self.client.post('/login', data={'username': 'admin', 'password': 'admin'})
            self.client.post('/add', data={'title': 'Test Task'})
            with self.app.app_context():
                task = Task.query.first()
                task_id = task.id
            response = self.client.post(f'/toggle/{task_id}')
            self.assertEqual(response.status_code, 302)
            with self.app.app_context():
                task = Task.query.get(task_id)
                self.assertEqual(task.status, 'working')

    def test_edit_task(self):
        with self.client:
            self.client.post('/login', data={'username': 'admin', 'password': 'admin'})
            self.client.post('/add', data={'title': 'Test Task'})
            with self.app.app_context():
                task = Task.query.first()
                task_id = task.id
            response = self.client.post(f'/edit/{task_id}', data={'title': 'Updated Task'})
            self.assertEqual(response.status_code, 302)
            with self.app.app_context():
                task = Task.query.get(task_id)
                self.assertEqual(task.title, 'Updated Task')

    def test_delete_task(self):
        with self.client:
            self.client.post('/login', data={'username': 'admin', 'password': 'admin'})
            self.client.post('/add', data={'title': 'Test Task'})
            with self.app.app_context():
                task = Task.query.first()
                task_id = task.id
            response = self.client.post(f'/delete/{task_id}')
            self.assertEqual(response.status_code, 302)
            with self.app.app_context():
                task = Task.query.get(task_id)
                self.assertIsNone(task)

    def test_clear_tasks(self):
        with self.client:
            self.client.post('/login', data={'username': 'admin', 'password': 'admin'})
            self.client.post('/add', data={'title': 'Task 1'})
            self.client.post('/add', data={'title': 'Task 2'})
            response = self.client.post('/clear')
            self.assertEqual(response.status_code, 302)
            with self.app.app_context():
                tasks = Task.query.all()
                self.assertEqual(len(tasks), 0)

if __name__ == '__main__':
    unittest.main()
