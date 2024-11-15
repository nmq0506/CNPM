import hashlib

from saleapp.app.models import Category, Product, User


def load_categories():
    return Category.query.order_by('id').all()


def load_products(kw=None, category_id=None):
    products = Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))

    if category_id:
        products = products.filter(Product.category_id == category_id)

    return products.all()
def count_products():
    return Product.query.count()

def auth_user(username, password):
    password= hashlib.md5(password.strip().encode('utf-8')).hexdigest()
    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password)).first()
def get_user_by_id(id):
    return User.query.get(id)
