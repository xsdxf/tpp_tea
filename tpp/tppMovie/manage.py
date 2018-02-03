from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from eagleEye import create_app
from eagleEye.exts import db

from eagleEye.models import Movie, Cinema, Hall, HallScheduling, Seat, SeatScheduling, Order

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
