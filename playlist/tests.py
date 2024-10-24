from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
import os

from memory_game_api import env
from game_admin.authentication import User


# class for testing the PlaylistGetAllView with a valid api key
class PlaylistGetAllViewTest(APITestCase):
    def setUp(self):
        self.url = reverse("playlist_get_all", args=["none", os.environ["API_KEY"]])

    # test the get method for PlaylistGetAllView
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# class for testing the PlaylistGetAllView with an invalid api key
class PlaylistGetAllViewTestInvalidApiKey(APITestCase):
    def setUp(self):
        self.url = reverse("playlist_get_all", args=["none", "invalid_api_key"])

    # test the get method for PlaylistGetAllView
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


# class for testing the PlaylistAddView with valid data and authorization
class PlaylistAddViewTest(APITestCase):
    def setUp(self):
        self.user = User()
        self.user.login(os.environ["ADMIN_USERNAME"], os.environ["ADMIN_PASSWORD"])
        self.headers = {
            "Token1": self.user.get_token1(),
            "Token2": self.user.get_token2(),
        }
        self.category_id = self.set_up_category()
        self.url = reverse("playlist_post")
        self.data = {
            "category": self.category_id,
            "title": "test_playlist",
            "description": "test_description",
            "image": open("media/test/playlist_test.png", "rb"),
            "audio": open("media/test/playlist_test.mp3", "rb"),
        }

    # test the post method for PlaylistAddView
    def test_post(self):
        response = self.client.post(self.url, self.data, headers=self.headers)
        print("image", response.data["image"])
        print("audio", response.data["audio"])
        if response.status_code == status.HTTP_201_CREATED:
            self.clean_up_after_uploading_playlist_files(response.data['image'], response.data['audio'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

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
        return response.data["id"]
    
    def clean_up_after_uploading_playlist_files(self, relative_path_image, relative_path_mp3):
        """Clean up the image and audio files after uploading them"""
        image_name = relative_path_image.split("/")[-1]
        mp3_name = relative_path_mp3.split("/")[-1]
        # Delete the image and audio files from the media folder
        media_path_image = os.path.join(os.getcwd(), "media", "images", image_name)
        media_path_mp3 = os.path.join(os.getcwd(), "media", "audio", mp3_name)
        if os.path.exists(media_path_image):
            os.remove(media_path_image)
        if os.path.exists(media_path_mp3):
            os.remove(media_path_mp3)


# class for setting up the database for tests
class SetupDatabase(APITestCase):
    def setUp(self):
        self.user = self.set_up_user()
        self.category_id = self.set_up_category()
        self.playlist_id = self.set_up_playlist()

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
        return response.data["id"]

    def set_up_playlist(self):
        self.data = {
            "category": self.category_id,
            "title": "test_playlist",
            "description": "test_description",
            "image": open("media/test/playlist_test.png", "rb"),
            "audio": open("media/test/playlist_test.mp3", "rb"),
        }
        url_add_playlist = reverse("playlist_add")
        response = self.client.post(url_add_playlist, self.data, headers=self.headers)

        if response.status_code == status.HTTP_201_CREATED:
            clean_up_after_uploading_playlist_files()
        return response.data["id"]

    def set_up_user(self):
        user = User()
        user.login(os.environ["ADMIN_USERNAME"], os.environ["ADMIN_PASSWORD"])
        self.headers = {"Token1": user.get_token1(), "Token2": user.get_token2()}
        return user


def clean_up_after_uploading_category_image(image_relative_path):
    """Clean up the image file after uploading it"""
    image_name = image_relative_path.split("/")[-1]
    # Delete the image file from the media folder
    media_path = os.path.join(os.getcwd(), "media", "images", image_name)
    if os.path.exists(media_path):
        os.remove(media_path)