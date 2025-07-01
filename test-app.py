import unittest
from app import app

class TodoTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_add_and_get_todo(self):
        response = self.client.post('/todos', json={'task': 'Learn Jenkins'})
        self.assertEqual(response.status_code, 201)

        response = self.client.get('/todos')
        self.assertEqual(response.status_code, 200) 
        self.assertIn('Learn Jenkins', response.get_data(as_text=True))

    def test_add_todo_without_task(self):
        response = self.client.post('/todos', json={})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
