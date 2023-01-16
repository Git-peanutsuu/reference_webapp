SOME_CONFIG = "configured in config.py"

class DefaultConfig(object):
  ENV= 'development'
  DEBUG = True
  TESTING = True
  DATABASE_URI = 'sqlite:///:memory:'
  SOME_CONFIG = "configured in Default class in config.py"

class ProductionConfig(DefaultConfig):
  ENV= 'production'
  DEBUG = False
  TESTING = False
  # DATABASE_URI = 'mysql://user@localhost/foo'
  # SOME_CONFIG = "configured in ProductionConfig class in config.py"
  
  # MYSQL_ADDRESS='127.0.0.1'
  # MYSQL_USER='root'
  # MYSQL_PASSWORD='password'
  # MYSQL_PORT=3306
  # MYSQL_DATABASE='hogepiyodb'

class DevelopmentConfig(DefaultConfig):
  DEBUG = True
  TESTING = True
  SOME_CONFIG = "configured in DevelopmentConfig class in config.py"