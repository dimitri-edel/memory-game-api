"""
WSGI config for memory_game_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""
import os
import sys

sys.path.append('/opt/gameapi2/memory-game-api')
sys.path.append('/opt/gameapi2/memory-game-api/category')
sys.path.append('/opt/gameapi2/memory-game-api/game_admin')
sys.path.append('/opt/gameapi2/memory-game-api/playlist')
sys.path.append('/opt/gameapi2/memory-game-api/quiz')
sys.path.append('/opt/gameapi2/memory-game-api/memory_game_api')



from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "memory_game_api.settings")

application = get_wsgi_application()
