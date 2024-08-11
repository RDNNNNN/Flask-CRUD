from flask import Flask,render_template,request,redirect
from orm.settiing import db
from models.model import Product
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)
Migrate(app, db)


@app.route("/",methods=["GET","POST"])
def product():
    if request.method == "POST":

        title = request.form.get("title")
        price = request.form.get("price")
        desc = request.form.get("desc")

        product = Product(title=title,price=price,desc=desc)

        db.session.add(product)
        db.session.commit()

        return redirect('/')
    
    products = Product.query.order_by(Product.id.desc())
    return render_template('views/index.jinja',products=products)

@app.route("/new")
def new():
    return render_template('views/new.jinja',product=product)

@app.route("/<int:id>")
def show(id):
    product = Product.query.get_or_404(id)
    return render_template('views/show.jinja',product=product)

@app.route("/<int:id>/edit")
def edit(id):
    product = Product.query.get_or_404(id)
    return render_template('views/edit.jinja',product=product)

@app.route("/<int:id>",methods=["POST"])
def update(id):
    product = Product.query.get_or_404(id)
    
    product.title = request.form.get("title")
    product.price = request.form.get("price")
    product.desc = request.form.get("desc")

    db.session.commit()

    return render_template('views/show.jinja',product=product)


@app.route("/<int:id>/delete",methods=["POST"])
def delete(id):

    product = Product.query.get_or_404(id)

    db.session.delete(product)
    db.session.commit()

    return redirect('/')