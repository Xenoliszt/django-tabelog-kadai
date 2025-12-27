FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# requirements.txt を先にコピー（超重要）
COPY requirements.txt /app/

# 依存関係インストール
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# kadai_002 をアプリルートとしてコピー
COPY kadai_002 /app

# staticfiles 用
RUN python manage.py collectstatic --noinput

# Heroku 用 Gunicorn 起動
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
