from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
import os

from memory_game_api import env
from game_admin.authentication import User


# Test case for CategoryGetAllView
class test_category_get_all(APITestCase):
    def setUp(self):
        self.user = User()
        self.user.login(os.environ["ADMIN_USERNAME"], os.environ["ADMIN_PASSWORD"])
        self.api_key = os.environ["API_KEY"]
        self.url = reverse("category_get_all", kwargs={"api_key": self.api_key})

    def test_get_all_categories(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# Test case for CategoryGetAllView with invalid api key
class test_category_get_all_invalid_api_key(APITestCase):
    def setUp(self):
        self.user = User()
        self.user.login(os.environ["ADMIN_USERNAME"], os.environ["ADMIN_PASSWORD"])
        self.api_key = "invalid api key"
        self.url = reverse("category_get_all", kwargs={"api_key": self.api_key})

    def test_get_all_categories(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


# Test case for CategoryAddView when access is authorized and the data is valid
class test_category_add_valid_data(APITestCase):
    def setUp(self):
        self.user = User()
        self.user.login(os.environ["ADMIN_USERNAME"], os.environ["ADMIN_PASSWORD"])
        self.token1 = self.user.get_token1()
        self.token2 = self.user.get_token2()
        self.url = reverse("category_add")

    def test_add_category(self):
        data = {
            "name": "Test Category",
            "description": "This is a test category",
            "image": open("media/test/test.png", "rb"),
        }
        response = self.client.post(
            self.url, data, HTTP_TOKEN1=self.token1, HTTP_TOKEN2=self.token2
        )
        if response.status_code == status.HTTP_201_CREATED:
            clean_up_after_uploading_image(response.data["image"])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# Test case for CategoryAddView when access authorization is successful but the data is invalid
class test_category_add_invalid_data(APITestCase):
    def setUp(self):
        self.user = User()
        self.user.login(os.environ["ADMIN_USERNAME"], os.environ["ADMIN_PASSWORD"])
        self.token1 = self.user.get_token1()
        self.token2 = self.user.get_token2()
        self.url = reverse("category_add")

    def test_add_category(self):
        data = {"name": "Test Category", "description": ""}
        response = self.client.post(
            self.url, data, HTTP_TOKEN1=self.token1, HTTP_TOKEN2=self.token2
        )
        if response.status_code == status.HTTP_201_CREATED:
            clean_up_after_uploading_image()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# Test case for CategoryUpdateView when access is not authorized(Invalid tokens)
class test_category_add_invalid_tokens(APITestCase):
    def setUp(self):
        self.url = reverse("category_add")

    def test_add_category(self):
        data = {"name": "Test Category", "description": "This is a test category"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


# Test case for CategoryUpdateView when access is authorized and the data is valid
class test_category_update_valid_data(APITestCase):
    def setUp(self):
        self.dataset_id = 0
        self.user = User()
        self.user.login(os.environ["ADMIN_USERNAME"], os.environ["ADMIN_PASSWORD"])
        self.token1 = self.user.get_token1()
        self.token2 = self.user.get_token2()
        self.dataset_id = add_dataset(self)
        # Attach id at the end of the url
        self.url = reverse("category_update", kwargs={"id": self.dataset_id})

    def test_update_category(self):
        # create a multipart form with an image file
        data = {
            "name": "Test Category",
            "description": "This is a test category",
            "image": open("media/test/test.png", "rb"),
        }

        response = self.client.put(
            self.url, data, HTTP_TOKEN1=self.token1, HTTP_TOKEN2=self.token2
        )
        if response.status_code == status.HTTP_200_OK:
            clean_up_after_uploading_image(response.data["image"])        
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# Test case for CategoryUpdateView when access authorization is successful but the data is invalid
class test_category_update_invalid_data(APITestCase):
    def setUp(self):
        self.dataset_id = 0
        self.user = User()
        self.user.login(os.environ["ADMIN_USERNAME"], os.environ["ADMIN_PASSWORD"])
        self.token1 = self.user.get_token1()
        self.token2 = self.user.get_token2()
        self.dataset_id = add_dataset(self)
        # Attach id at the end of the url
        self.url = reverse("category_update", kwargs={"id": self.dataset_id})


    def test_update_category(self):
        # create a multipart form with an image file
        data = {"name": "Test Category", "description": ""}

        response = self.client.put(
            self.url, data, HTTP_TOKEN1=self.token1, HTTP_TOKEN2=self.token2
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# Test class for CategoryUpdateView when access is not authorized(Invalid tokens))
class test_category_update_with_invalid_tokens(APITestCase):
    def setUp(self):
        self.url = reverse("category_update", kwargs={"id": 1})

    def test_update_category(self):
        data = {"name": "Test Category", "description": "This is a test category"}
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


# Test case for CategoryDeleteView when access is authorized and the id is valid
class test_category_delete_valid_data(APITestCase):
    def setUp(self):
        self.user = User()
        self.user.login(os.environ["ADMIN_USERNAME"], os.environ["ADMIN_PASSWORD"])
        self.token1 = self.user.get_token1()
        self.token2 = self.user.get_token2()
        self.dataset_id = add_dataset(self)
        # Attach id at the end of the url
        self.url = reverse("category_delete", kwargs={"id": self.dataset_id})

    def test_delete_category(self):
        response = self.client.delete(
            self.url, HTTP_TOKEN1=self.token1, HTTP_TOKEN2=self.token2
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


# Test case for CategoryDeleteView when access is authorized but the id is invalid
class test_category_delete_invalid_id(APITestCase):
    def setUp(self):
        self.user = User()
        self.user.login(os.environ["ADMIN_USERNAME"], os.environ["ADMIN_PASSWORD"])
        self.token1 = self.user.get_token1()
        self.token2 = self.user.get_token2()
        self.dataset_id = add_dataset(self)
        # Attach id at the end of the url
        self.url = reverse("category_delete", kwargs={"id": 100})

    def test_delete_category(self):
        response = self.client.delete(
            self.url, HTTP_TOKEN1=self.token1, HTTP_TOKEN2=self.token2
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# Test case for CategoryDeleteView when access is not authorized(Invalid tokens)
class test_category_delete_invalid_tokens(APITestCase):
    def setUp(self):
        self.url = reverse("category_delete", kwargs={"id": 1})

    def test_delete_category(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


def add_dataset(self):
    url_add_dataset = reverse("category_add")
    # create a multipart form with an image file
    data = {
        "name": "Test Category",
        "description": "This is a test category",
        "image": open("media/test/test.png", "rb"),
    }
    response = self.client.post(
        url_add_dataset, data, HTTP_TOKEN1=self.token1, HTTP_TOKEN2=self.token2
    )
    image_relative_path = response.data["image"]
    if response.status_code == status.HTTP_201_CREATED:
        clean_up_after_uploading_image(image_relative_path)

    return response.data["id"]


def clean_up_after_uploading_image(image_relative_path):
    """Clean up the image file after uploading it"""    
    # extract the image name from the relative path
    image_name = image_relative_path.split("/")[-1]
    # Delete the image file from the media folder
    media_path = os.path.join(os.getcwd(), 'media', 'images', image_name)    
    if os.path.exists(media_path):
        os.remove(media_path)
