## Flask Admin

Flask Project - creates an Admin Dashboard using the [Flask-Admin](https://flask-admin.readthedocs.io/en/latest/introduction/#getting-started) Python (PyPi) package

Uses the [Bootswatch 3](https://bootswatch.com/3/default) styling themes: Lumen, Cyborg

![DISPLAY](https://user-images.githubusercontent.com/57027705/172066130-63a98317-71bc-4e37-81bc-f341554f3fd5.JPG)

![DISPLAY-2](https://user-images.githubusercontent.com/57027705/173208196-0a9df5a5-1e09-4ad3-baff-e7cb468d4846.JPG)


### Development

- Requires a python virtual environment: Recommend `pipenv` to activate the environment
- Requires a local Postgres environment with a superuser: Recommend using the Postgres CLI
- Install python dependencies: `pipenv install` or the equivalent command for your python package manager

### To run the development server: 

In the python shell: `FLASK_ENV=development  python3 app.py flask run`

Navigate to : https://localhost:5000/admin

To set the database:

- Enter the postgres CLI: `psql`

- Create a database:
`createdb database_name` 

- Switch to your created database:
`\c database_name`

- Change the `SQLALCHEMY_DATABASE_URI` string in `config.py` to reflect your database name and access: `"postgresql://databaseuser:password@localhost:5432/database_name"`

- Initialize database with [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/index.html) and SQLAlchemy by typing `flask db init` 

- Create initial migration with:
`flask db migrate -m "Initial migration(or other msg)"`

- Run migration with:
`flask db upgrade`

> **Note:** [Alembic]() in Flask-Migrate does not detect all changes to the database (changes to table names, column names, anonymous constraints) so you must review the migration script and edit as appropriate

### To Update the Database or Models

Each time the database models change repeat the `migrate` and `upgrade` commands

When adding a new model that should be accessible via the Admin panel, register the view to Flask-Admin:

`admin.add_view(ModelView(models.YourModelClass, db.session))`


