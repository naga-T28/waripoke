"""
WSGI config for app_config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
from wsgiref.handlers import CGIHandler
from django.core.wsgi import get_wsgi_application

# 環境情報の出力 (デバッグ用)
print("FILE_PATH: ", os.path.dirname(__file__))
print("PROJECT_NAME: ", os.path.basename(os.path.dirname(__file__)))

# プロジェクトのパスを設定
FILE_PATH = os.path.dirname(__file__)
PROJECT_PATH = os.path.expanduser("~/waripoke.xyz/public_html/app_config")

# プロジェクトのパスをsys.pathに追加
sys.path.append(PROJECT_PATH)
sys.path.append(os.path.dirname(PROJECT_PATH))

# Djangoの設定を指定
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_config.settings')

# WSGIアプリケーションを取得
application = get_wsgi_application()

# CGIとして実行する場合のエントリポイント
if __name__ == "__main__":
    CGIHandler().run(application)
