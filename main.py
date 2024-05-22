"""📌 Создать базовый шаблон для интернет-магазина,
содержащий общие элементы дизайна (шапка, меню,
подвал), и дочерние шаблоны для страниц категорий
товаров и отдельных товаров.
📌 Например, создать страницы "Одежда", "Обувь" и "Куртка",
используя базовый шаблон."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # return 'Привет! Введи в команднойстроке после "/" название страницы: одежда, обувь, куртка!'
    # return 'Заходи в наш магазин: http://127.0.0.1:5000/одежда'
    contex = {
        'title': 'Главная'
    }
    return render_template('index.html', **contex)

@app.route('/одежда/')
def clothes():
    contex = {
        'title': 'Одежда'
    }
    return render_template('clothes.html', **contex)


@app.route('/обувь/')
def footwear():
    contex = {
        'title': 'Обувь'
    }
    return render_template('footwear.html', **contex)


@app.route('/куртки/')
def jacket():
    contex = {
        'title': 'Куртки'
    }
    return render_template('jacket.html', **contex)


if __name__ == '__main__':
    app.run(debug=True)