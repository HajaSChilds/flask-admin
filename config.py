import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://databaseuser:P@ssw0rd@localhost:5432/fake_admin"

class TestConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URL")

config = {
    'development': DevConfig,
    'testing': TestConfig,
    'default': DevConfig
}    