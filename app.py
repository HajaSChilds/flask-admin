from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from backend import models, create_app, db



app = create_app('development')
migrate = Migrate(app, db)

app.config["FLASK_ADMIN_SWATCH"] = "Lumen"
admin = Admin(app, name="My Test Admin", template_mode="bootstrap3")

admin.add_view(ModelView(models.User, db.session))


@app.route("/")
def Home():
    return "<h1>Flask Admin Dashboard Test</h1><p>Go to the admin route: <a href='http://localhost:5000/admin'>http://localhost:5000/admin</a></p>"


app.run()


