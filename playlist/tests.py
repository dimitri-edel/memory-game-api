from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
import os

from memory_game_api import env
from game_admin.authentication import User

# class for testing the PlaylistGetAllView with a valid api key
class PlaylistGetAllViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('playlist_get_all', args=['none', os.environ["API_KEY"]])
        
    # test the get method for PlaylistGetAllView
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
# class for testing the PlaylistGetAllView with an invalid api key
class PlaylistGetAllViewTestInvalidApiKey(APITestCase):
    def setUp(self):
        self.url = reverse('playlist_get_all', args=['none', 'invalid_api_key'])
        
    # test the get method for PlaylistGetAllView
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

# class for setting up the database for tests
class SetupDatabase(APITestCase):
    def setUp(self):        
        self.user = self.set_up_user()
        self.category_id = self.set_up_category()
        self.playlist_id = self.set_up_playlist()
        self.client.post(reverse('playlist_add'), self.data, headers=self.headers)

    def set_up_category(self):
        url_add_category = reverse('category_add')
        data = {
            'name': 'test_category',
            'description': 'test_description',
            'image': open('media/images/test/test.png', 'rb')
        }
        response = self.client.post(url_add_category, data, HTTP_TOKEN1=self.user.get_token1(), HTTP_TOKEN2=self.user.get_token2())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        if response.status_code == status.HTTP_201_CREATED:
            clean_up_after_uploading_category_image()
        self.dataset_id = response.data["id"]        
        return response.data["id"]

    def set_up_playlist(self):
        self.data = {
            'category': self.category_id,
            'title': 'test_playlist',
            'description': 'test_description',
            'image': open('media/images/test/playlist_test.png', 'rb'),
            'audio': open('media/audio/test/playlist_test.mp3', 'rb')
        }
        url_add_playlist = reverse('playlist_add')
        response = self.client.post(url_add_playlist, self.data, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        if response.status_code == status.HTTP_201_CREATED:
            clean_up_after_uploading_playlist_files()
        return response.data['id']

    def set_up_user(self):
        user = User()
        user.login(os.environ["ADMIN_USERNAME"], os.environ["ADMIN_PASSWORD"])
        self.headers = {
            'Token1': user.get_token1(),
            'Token2': user.get_token2()
        }
        return user

def clean_up_after_uploading_category_image():
    ''' Clean up the image file after uploading it '''
    # Delete the image file from the media folder
    media_path = os.path.join(os.getcwd(), 'media', 'images', 'test.png')
    if os.path.exists(media_path):
        os.remove(media_path)

def clean_up_after_uploading_playlist_files():
    ''' Clean up the image file after uploading it '''
    # Delete the image file from the media folder
    image_path = os.path.join(os.getcwd(), 'media', 'images', 'playlist_test.png')
    mp3_path = os.path.join(os.getcwd(), 'media', 'audio', 'playlist_test.mp3')
    if os.path.exists(image_path):
        os.remove(image_path)
    if os.path.exists(mp3_path):
        os.remove(mp3_path)