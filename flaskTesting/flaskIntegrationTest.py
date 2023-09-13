import io
import unittest
import pandas as pd
from app import app


class FlaskIntegrationTestCase(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_add_remove_todos_and_download_excel(self):
        for i in range(1, 6):
            self.client.post('/add', data={
                'todo': f'Todo {i}'
            })
        self.client.get('/remove/2')
        response = self.client.get('download_todos')
        self.assertEqual(response.status_code, second=200)
        self.assertEqual(response.content_type, second='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        with io.BytesIO(response.data) as buffer:
            df = pd.read_excel(buffer)
            self.assertListEqual(['Todo 1', 'Todo 3', 'Todo 4', 'Todo 5'], df.todo.values.tolist())
