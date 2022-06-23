from flask_migrate import Migrate
# from flask_admin import Admin
# from flask_admin.contrib.sqla import ModelView

from backend import models, create_app, db



app = create_app('development')
migrate = Migrate(app, db)

# # Flask Admin Configuration
# app.config["FLASK_ADMIN_SWATCH"] = "Cyborg"
# admin = Admin(app, name="International Artists Database", template_mode="bootstrap3")

# admin.add_view(ModelView(models.User, db.session))
# admin.add_view(ModelView(models.Artists, db.session))
# admin.add_view(ModelView(models.Songs, db.session))


@app.route("/")
def Home():
    return "<h1>Flask Admin Dashboard Test</h1><p>Go to the admin route: <a href='http://localhost:5000/admin'>http://localhost:5000/admin</a></p>"

if __name__ == "__main__":
    app.run()
