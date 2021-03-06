"""this module has the unittests """
import unittest
import json

from app.initialize import create_app


class QuestionTestCase(unittest.TestCase):
    """This class represents the question test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(
            config_name="testing")
        self.client = self.app.test_client
        self.question = {'id': 1, 'title': 'how do i build a restful API?'}

    def test_question_creation(self):
        """Test API can create a question (POST request)"""
        response = self.client().post('/api/v1/questions',
                                      data=json.dumps(self.question),
                                      content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertIn('restful API', str(response.data))

    def test_api_can_get_all_questions(self):
        """Test API can get a question (GET request)."""

        response = self.client().get('/api/v1/questions')
        self.assertEqual(response.status_code, 200)
        self.assertIn('android apps', str(response.data))

    def test_api_can_get_question_by_id(self):
        """Test API can get a single question by using it's id."""

        result = self.client().get(
            '/api/v1/questions/1')
        self.assertEqual(result.status_code, 200)
        self.assertIn('ORMs', str(result.data))

    def test_question_can_be_edited(self):
        """Test API can edit an existing question. (PUT request)"""

        route = self.client().put('/api/v1/questions/1',
                                  data=json.dumps(self.question),
                                  content_type='application/json')
        self.assertEqual(route.status_code, 200)
        self.assertIn('restful API', str(route.data))

    def test_question_deletion(self):
        """Test API can delete an existing question. (DELETE request)."""

        response = self.client().delete('/api/v1/questions/1')
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        """teardown all initialized variables."""
        del self.question


# Make the tests conveniently executable
if __name__ == "__main__":

    unittest.main()
