from rest_framework.views import APIView
from rest_framework.response import Response    
from rest_framework import status
from .authentication import User
from category.models import Category
from playlist.models import Playlist
from quiz.models import Quiz
from memory_game_api.settings import MEDIA_ROOT
import os
'''
Views for the auth app

Upon loging in the user gets two tokens. The tokens are hashed values of the username and password.
These tokens can be stored in the client's local storage or as a cookie.
The tokens are used to authenticate the user when they make requests to the API.
'''
class UserLoginView(APIView):
    '''Login view for User model'''
    def post(self, request):        
        '''Post method for User model'''
        username = request.data.get('username')
        password = request.data.get('password')
        user = User()
        if not user.login(username, password):
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
       
        # Create a response with two tokens. The tokens are hashed values of the username and password.
        response = Response(status=status.HTTP_200_OK, data={'token1': user.get_token1(), 'token2': user.get_token2()})
        return response

class FileManager(APIView):
    ''' View for managing files that are used by the game'''
    def get(self, request):
        '''Get method for FileManager'''
        used_files = {"images" : [], "audio" : [], "json" : []}
        all_files = self._get_list_of_all_files()
        self._get_list_of_used_files(used_files["images"], used_files["audio"], used_files["json"])
        # user = User()
        # if not user.authenticate(request):
        #     return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        # print files and their sizes
        image_folder = os.path.join(MEDIA_ROOT, 'images')
        audio_folder = os.path.join(MEDIA_ROOT, 'audio')
        json_folder = os.path.join(MEDIA_ROOT, 'json')
        for file in all_files["images"]:
            if file not in used_files["images"]:
                print("removing : ", file)
                print(os.path.getsize(os.path.join(image_folder, file)))
                os.remove(os.path.join(image_folder, file))
            else:
                print("keeping : ", file)
                print(os.path.getsize(os.path.join(image_folder, file)))
        
        for file in all_files["audio"]:
            if file not in used_files["audio"]:
                print("removing : ", file)
                print(os.path.getsize(os.path.join(audio_folder, file)))
                os.remove(os.path.join(audio_folder, file))
            else:
                print("keeping : ", file)
                print(os.path.getsize(os.path.join(audio_folder, file)))

        for file in all_files["json"]:
            if file not in used_files["json"]:
                print("removing : ", file)
                print(os.path.getsize(os.path.join(json_folder, file)))
                os.remove(os.path.join(json_folder, file))
            else:
                print("keeping : ", file)
                print(os.path.getsize(os.path.join(json_folder, file)))

        return Response(used_files, status=status.HTTP_200_OK)
    
    def _get_list_of_all_files(self):
        '''Get list of all files in the images folder'''
        image_folder = os.path.join(MEDIA_ROOT, 'images')
        image_files =  os.listdir(image_folder)
        audio_folder = os.path.join(MEDIA_ROOT, 'audio')
        audio_files = os.listdir(audio_folder)
        json_folder = os.path.join(MEDIA_ROOT, 'json')
        json_files = os.listdir(json_folder)
        
        return {"images" : image_files, "audio" : audio_files, "json" : json_files}
    
    def _get_list_of_used_files(self, images_array, audio_array, json_array):
        '''Get list of files that are used by the game'''        
        self._get_category_files(images_array)
        self._get_playlist_files(images_array, audio_array)
        self._get_quiz_files(json_array)        
    
    def _get_category_files(self, images_array):
        '''Get list of files that are used by the categories'''
        categories = Category.objects.all()
        for category in categories:              
            filename = self._extract_filename_form_path(category.image.path)            
            images_array.append(filename)
    
    def _get_playlist_files(self, images_array, audio_array):
        '''Get list of files that are used by the playlists'''
        playlists = Playlist.objects.all()
        for playlist in playlists:              
            filename = self._extract_filename_form_path(playlist.image.path)            
            images_array.append(filename)
            filename = self._extract_filename_form_path(playlist.audio.path)            
            audio_array.append(filename)
    
    def _get_quiz_files(self, json_array):
        '''Get list of files that are used by the quizzes'''
        quizzes = Quiz.objects.all()
        for quiz in quizzes:              
            filename = self._extract_filename_form_path(quiz.json.path)            
            json_array.append(filename)
    
    def _extract_filename_form_path(self, path):
        '''Extract filename from path'''
        return os.path.basename(path)