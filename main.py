from src.dbman import DataProvider
from src.ui import StoreUI

if __name__ == '__main__':
    db = DataProvider('farmacia', 'localhost', 'root', 'kennyow86!')
    if (db.open()):
        db.close()
        ui = StoreUI("Farmacia", 800, 600, 150, 150)
        ui.connect(db)
        ui.run()

