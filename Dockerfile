FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# kadai_002 をアプリルートとしてコピー
COPY kadai_002 /app

# 依存関係インストール
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# staticfiles 用
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
