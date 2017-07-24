# run the flask application

from app import app

if __name__ == '__main__':
  app.secret_key = "super-secret"
  app.run()
