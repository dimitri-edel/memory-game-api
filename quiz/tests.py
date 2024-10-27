from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
import os

from memory_game_api import env
from game_admin.authentication import User

class SetupDatabase:
    """class for setting up a database with dummy data for tests"""

    def __init__(self, clean_up: True):
        self.client = APIClient()        
        self.clean_up = clean_up
        self.user = self.set_up_user()
        self.category_id = self.set_up_category() 
        self.quiz_id = self.set_up_quiz()       

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

    def set_up_user(self):
        user = User()
        user.login(os.environ["ADMIN_USERNAME"], os.environ["ADMIN_PASSWORD"])
        self.headers = {"Token1": user.get_token1(), "Token2": user.get_token2()}
        return user
    
    def set_up_quiz(self):
        url_add_quiz = reverse("quiz_add")
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

    def get_category_id(self):
        return self.category_id

def clean_up_after_uploading_category_image(image_relative_path):
    """Clean up the image file after uploading it"""
    image_name = get_filename_from_path(image_relative_path)
    # Delete the image file from the media folder
    media_path = os.path.join(os.getcwd(), "media", "images", image_name)
    if os.path.exists(media_path):
        os.remove(media_path)

def get_filename_from_path(path):
    """Get the filename from the path"""
    return path.split("/")[-1]

def clean_up_after_uploading_quiz_json(json_relative_path):
    """Clean up the json file after uploading it"""
    json_name = get_filename_from_path(json_relative_path)
    # Delete the json file from the media folder
    media_path = os.path.join(os.getcwd(), "media", "json", json_name)
    if os.path.exists(media_path):
        os.remove(media_path)