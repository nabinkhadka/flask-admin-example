# from flask_migrate import Migrate, MigrateCommand, Manager
# import os
# from app import app, db
#
# app_settings = os.getenv('APP_SETTINGS', 'project.server.config.DevelopmentConfig')
# app.config.from_object(app_settings)
#
# migrate = Migrate(app, db)
# manager = Manager(app)
#
# manager.add_command('db', MigrateCommand)
#
#
# if __name__ == '__main__':
#     manager.run()
