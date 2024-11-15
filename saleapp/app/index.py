from flask import render_template, request ,redirect
import dao
from saleapp.app import app , login
from flask_login import login_user , logout_user

@app.route("/")
def index():
    cates = dao.load_categories()

    kw = request.args.get('kw')
    cate_id = request.args.get('category_id')
    prods = dao.load_products(kw=kw, category_id=cate_id)
    return render_template('index.html', categories=cates, products=prods)

@app.route("/login", methods=['get', 'post'])
def login_process():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        print(username,password)
        u= dao.auth_user(username=username,password=password)
        if u:
            login_user(u)
            return redirect('/')
    return render_template('layout/login.html')

@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
