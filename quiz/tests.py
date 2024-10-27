from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
import os

from memory_game_api import env
from game_admin.authentication import User

# Test QuizListView class with valid API key
class TestQuizListViewWithValidAPIKey(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("get-all-quizzes", args=["none", os.environ["API_KEY"]])
        self.response = self.client.get(self.url)

    def test_get_request(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

# Test QuizListView class with invalid API key
class TestQuizListViewWithInvalidAPIKey(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("get-all-quizzes", args=["none", "invalid_api_key"])
        self.response = self.client.get(self.url)

    def test_get_request(self):
        self.assertEqual(self.response.status_code, status.HTTP_401_UNAUTHORIZED)
    
# Test QuizAddView class with valid tokens and valid data
class TestQuizAddViewWithValidTokens(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User()
        self.user.login(os.environ["ADMIN_USERNAME"], os.environ["ADMIN_PASSWORD"])
        self.category_id = self.set_up_category()
        self.url = reverse("add-quiz")
        self.data = {
            "category": self.category_id,
            "json": open("media/test/test.json", "rb"),
        }
        self.response = self.client.post(
            self.url,
            self.data,
            HTTP_TOKEN1=self.user.get_token1(),
            HTTP_TOKEN2=self.user.get_token2(),
        )

    def set_up_category(self):
        url_add_category = reverse("category_add")
        data = {
            "name": "test_category",
            "description": "test_description",
            "image": open("media/test/test.png", "rb"),
        }
        response = self.client.post(
            url_add_category,
            data,
            HTTP_TOKEN1=self.user.get_token1(),
            HTTP_TOKEN2=self.user.get_token2(),
        )
        self.image_name = response.data["image"]

        if response.status_code == status.HTTP_201_CREATED:
            clean_up_after_uploading_category_image(self.image_name)
        self.dataset_id = response.data["id"]
        return response.data.get("id")

    def test_post_request(self):
        clean_up_after_uploading_quiz_json(self.response.data["json"])
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

# Test QuizAddView class with invalid tokens and valid data
class TestQuizAddViewWithInvalidTokens(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("add-quiz")
        self.data = {
            "category": 1,
            "json": open("media/test/test.json", "rb"),
        }
        self.response = self.client.post(self.url, self.data)

    def test_post_request(self):
        self.assertEqual(self.response.status_code, status.HTTP_401_UNAUTHORIZED)
# Test QuizAddView class with valid tokens and invalid data
class TestQuizAddViewWithValidTokensAndInvalidData(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User()
        self.user.login(os.environ["ADMIN_USERNAME"], os.environ["ADMIN_PASSWORD"])
        self.url = reverse("add-quiz")
        self.data = {
            "category": 1,
            "json": open("media/test/test.json", "rb"),
        }
        self.response = self.client.post(
            self.url,
            self.data,
            HTTP_TOKEN1=self.user.get_token1(),
            HTTP_TOKEN2=self.user.get_token2(),
        )

    def test_post_request(self):
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)
# Test QuizUpdateView class with valid tokens and valid data
class TestQuizUpdateViewWithValidTokens(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User()
        self.user.login(os.environ["ADMIN_USERNAME"], os.environ["ADMIN_PASSWORD"])
        self.category_id = self.set_up_category()
        self.quiz_id = self.set_up_quiz()
        self.url = reverse("update-quiz", args=[self.quiz_id])
        self.data = {
            "category": self.category_id,
            "json": open("media/test/test.json", "rb"),
        }
        self.response = self.client.put(
            self.url,
            self.data,
            HTTP_TOKEN1=self.user.get_token1(),
            HTTP_TOKEN2=self.user.get_token2(),
        )

    def set_up_category(self):
        url_add_category = reverse("category_add")
        data = {
            "name": "test_category",
            "description": "test_description",
            "image": open("media/test/test.png", "rb"),
        }
        response = self.client.post(
            url_add_category,
            data,
            HTTP_TOKEN1=self.user.get_token1(),
            HTTP_TOKEN2=self.user.get_token2(),
        )
        self.image_name = response.data["image"]

        if response.status_code == status.HTTP_201_CREATED:
            clean_up_after_uploading_category_image(self.image_name)
        self.dataset_id = response.data["id"]
        return response.data.get("id")

    def set_up_quiz(self):
        url_add_quiz = reverse("add-quiz")
        data = {
            "category": self.category_id,
            "json": open("media/test/test.json", "rb"),
        }
        response = self.client.post(
            url_add_quiz,
            data,
            HTTP_TOKEN1=self.user.get_token1(),
            HTTP_TOKEN2=self.user.get_token2(),
        )
        self.json_name = response.data["json"]
        if response.status_code == status.HTTP_201_CREATED:
            clean_up_after_uploading_quiz_json(self.json_name)
        return response.data.get("id")

    def test_put_request(self):
        clean_up_after_uploading_quiz_json(self.response.data["json"])
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
# Test QuizUpdateView class with invalid tokens and valid data
class TestQuizUpdateViewWithInvalidTokens(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("update-quiz", args=[1])
        self.data = {
            "category": 1,
            "json": open("media/test/test.json", "rb"),
        }
        self.response = self.client.put(self.url, self.data)

    def test_put_request(self):
        self.assertEqual(self.response.status_code, status.HTTP_401_UNAUTHORIZED)
# Test QuizUpdateView class with valid tokens and invalid data
class TestQuizUpdateViewWithValidTokensAndInvalidData(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User()
        self.user.login(os.environ["ADMIN_USERNAME"], os.environ["ADMIN_PASSWORD"])
        self.url = reverse("update-quiz", args=[1])
        self.data = {
            "category": 1,
            "json": open("media/test/test.json", "rb"),
        }
        self.response = self.client.put(
            self.url,
            self.data,
            HTTP_TOKEN1=self.user.get_token1(),
            HTTP_TOKEN2=self.user.get_token2(),
        )

    def test_put_request(self):
        self.assertEqual(self.response.status_code, status.HTTP_404_NOT_FOUND)
# Test QuizDeleteView class with valid tokens and valid data
class TestQuizDeleteViewWithValidTokens(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User()
        self.user.login(os.environ["ADMIN_USERNAME"], os.environ["ADMIN_PASSWORD"])
        self.category_id = self.set_up_category()
        self.quiz_id = self.set_up_quiz()
        self.url = reverse("delete-quiz", args=[self.quiz_id])
        self.response = self.client.delete(
            self.url,
            HTTP_TOKEN1=self.user.get_token1(),
            HTTP_TOKEN2=self.user.get_token2(),
        )

    def set_up_category(self):
        url_add_category = reverse("category_add")
        data = {
            "name": "test_category",
            "description": "test_description",
            "image": open("media/test/test.png", "rb"),
        }
        response = self.client.post(
            url_add_category,
            data,
            HTTP_TOKEN1=self.user.get_token1(),
            HTTP_TOKEN2=self.user.get_token2(),
        )
        self.image_name = response.data["image"]

        if response.status_code == status.HTTP_201_CREATED:
            clean_up_after_uploading_category_image(self.image_name)
        self.dataset_id = response.data["id"]
        return response.data.get("id")

    def set_up_quiz(self):
        url_add_quiz = reverse("add-quiz")
        data = {
            "category": self.category_id,
            "json": open("media/test/test.json", "rb"),
        }
        response = self.client.post(
            url_add_quiz,
            data,
            HTTP_TOKEN1=self.user.get_token1(),
            HTTP_TOKEN2=self.user.get_token2(),
        )
        self.json_name = response.data["json"]
        if response.status_code == status.HTTP_201_CREATED:
            clean_up_after_uploading_quiz_json(self.json_name)
        return response.data.get("id")

    def test_delete_request(self):
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
# Test QuizDeleteView class with invalid tokens and valid data
class TestQuizDeleteViewWithInvalidTokens(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("delete-quiz", args=[1])
        self.response = self.client.delete(self.url)

    def test_delete_request(self):
        self.assertEqual(self.response.status_code, status.HTTP_401_UNAUTHORIZED)

class SetupDatabase:
    """class for setting up a database with dummy data for tests"""

    def __init__(self, clean_up: True):
        self.client = APIClient()        
        self.clean_up = clean_up        
        self.user = self.set_up_user()
        self.category_id = self.set_up_category() 
        self.quiz_id = self.set_up_quiz()       

    def set_up_category(self)->int:
        url_add_category = reverse("category_add")
        data = {
            "name": "test_category",
            "description": "test_description",
            "image": open("media/test/test.png", "rb"),
        }
        response = self.client.post(
            url_add_category,
            data,
            HTTP_TOKEN1=self.user.get_token1(),
            HTTP_TOKEN2=self.user.get_token2(),
        )
        self.image_name = response.data["image"]

        if response.status_code == status.HTTP_201_CREATED:
            clean_up_after_uploading_category_image(self.image_name)
        self.dataset_id = response.data["id"]
        return response.data.get("id")

    def set_up_user(self)->User:
        user = User()
        user.login(os.environ["ADMIN_USERNAME"], os.environ["ADMIN_PASSWORD"])
        self.headers = {"Token1": user.get_token1(), "Token2": user.get_token2()}
        return user
    
    def set_up_quiz(self)->int:
        url_add_quiz = reverse("add-quiz")
        data = {
            "category": self.category_id,
            "json": open("media/test/test.json", "rb"),
        }
        response = self.client.post(
            url_add_quiz,
            data,
            HTTP_TOKEN1=self.user.get_token1(),
            HTTP_TOKEN2=self.user.get_token2(),
        )
        self.json_name = response.data["json"]
        if response.status_code == status.HTTP_201_CREATED:
            if self.clean_up:
                '''When testing the delete view, the test_add_quiz variable must be set to False, 
                because the delete view will delete the file'''
                clean_up_after_uploading_quiz_json(self.json_name)        
        return response.data.get("id")

    def get_category_id(self):
        return self.category_id

def clean_up_after_uploading_category_image(image_relative_path):
    """Clean up the image file after uploading it"""
    image_name = get_filename_from_path(image_relative_path)
    # Delete the image file from the media folder
    media_path = os.path.join(os.getcwd(), "media", "images", image_name)
    if os.path.exists(media_path):
        os.remove(media_path)

def get_filename_from_path(path)->str:
    """Get the filename from the path"""
    return path.split("/")[-1]

def clean_up_after_uploading_quiz_json(json_relative_path):
    """Clean up the json file after uploading it"""
    json_name = get_filename_from_path(json_relative_path)
    # Delete the json file from the media folder
    media_path = os.path.join(os.getcwd(), "media", "json", json_name)
    if os.path.exists(media_path):
        os.remove(media_path)