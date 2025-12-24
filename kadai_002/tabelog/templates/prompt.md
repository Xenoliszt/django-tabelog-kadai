## 命令
Django 管理サイトでstoreにFood category:を二つ以上紐づけられるように設定したい

## 前提
- 検索条件に引っかかりやすくするため
- 最大3つまでつけられる（例：ラーメン、定食、カレー　等）
- 必要ならば他のファイルも共有するので変更が必要なコードだけ手順を追って説明して
## 出力
サンプル例


以下はstore_list.html

{% extends "base.html" %}
{% block title %}店舗一覧{% endblock %}
{% block content %}


<div id="storeCarousel" class="carousel slide mb-4" data-bs-ride="carousel">
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#storeCarousel" data-bs-slide-to="0" class="active"></button>
    <button type="button" data-bs-target="#storeCarousel" data-bs-slide-to="1"></button>
    <button type="button" data-bs-target="#storeCarousel" data-bs-slide-to="2"></button>
  </div>

  <div class="carousel-inner">

    <div class="carousel-item active">
      <img src="/static/images/slide1.jpg" class="d-block w-100" alt="slide1">
    

      <div class="carousel-caption d-none d-md-block">
        <h3 class="fw-bold">地元の美味しいお店をご紹介</h3>
      </div>
    </div>


    <div class="carousel-item">
      <img src="/static/images/slide2.jpg" class="d-block w-100" alt="slide2">

      <div class="carousel-caption d-none d-md-block">
        <h3 class="fw-bold">富士市民に愛されるお店</h3>
      </div>
    </div>


    <div class="carousel-item">
      <img src="/static/images/slide3.jpg" class="d-block w-100" alt="slide3">

      <div class="carousel-caption d-none d-md-block">
        <h3 class="fw-bold">持ち帰り、テイクアウトも可</h3>
      </div>
    </div>

  <button class="carousel-control-prev" type="button" data-bs-target="#storeCarousel" data-bs-slide="prev">
    <span class="carousel-control-prev-icon"></span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#storeCarousel" data-bs-slide="next">
    <span class="carousel-control-next-icon"></span>
  </button>
</div>


<h1 class="section-title">・店舗一覧</h1>

  <div class="row">
    {% for store in stores %}
    <div class="col-12 col-md-4 mb-4">
        <div class="card">
            <img src="{{ store.image.url }}" class="card-img-top vertical-card-image">
            <div class="card-body">
                <h4 class="card-title">
                    <a href="/store/{{ store.id }}/">{{ store.name }}</a>
                
                </h4>

                <h7 class="card-title">
                    {{ store.business_hours }}
                </h7>

                <h8 class="card-title">
                    定休日:
                    {{ store.holiday }}
                </h8>

            </div>

        </div>
    </div>
    {% endfor %}
</div>


<h2 class="section-title mb-3">・カテゴリから探す</h2>

<div class="row mb-4 text-center">
  {% for category in categories %}
  <div class="col-12 col-md-4 mb-3">
    <a href="{% url 'tabelog:store_category' category.id %}" class="category-card">
      <div class="category-bg {{ category.keyword }}">
        <span>{{ category.name }}</span>
      </div>
    </a>
  </div>
  {% endfor %}

  
</div>


<h3 class="fw-bold text-white mb-2">・食べ物から探す</h3>

<div class="food-tag-wrapper mb-4">
    {% for food_category in food_categories %}
    <a href="{% url 'tabelog:food_category' food_category.id %}" class="food-tag">{{ food_category.name }}</a>
   {% endfor %}
</div>

{% endblock %}