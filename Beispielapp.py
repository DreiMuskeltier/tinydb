from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QFileDialog, QComboBox, QPushButton, QHBoxLayout, QWidget
from tinydb import TinyDB
from ui.Beispiel import Ui_MainWindow  # erzeugt durch pyside6-uic
import os

# Start-Datenbank
db_path = "datenbank.json"
db = TinyDB(db_path)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Container für Dropdown + "Neue DB"-Button
        self.db_widget = QWidget(self)
        self.db_layout = QHBoxLayout(self.db_widget)
        self.ui.verticalLayout.insertWidget(0, self.db_widget)

        # Dropdown-Menü für Datenbanken
        self.db_dropdown = QComboBox(self)
        self.db_layout.addWidget(self.db_dropdown)
        self.db_dropdown.currentIndexChanged.connect(self.switch_database)

        # Button zum Erstellen einer neuen Datenbank
        self.new_db_button = QPushButton("Neue Datenbank", self)
        self.db_layout.addWidget(self.new_db_button)
        self.new_db_button.clicked.connect(self.create_new_database)

        # Liste der Datenbanken vorbereiten
        self.databases = [db_path]  # Standard-Datenbank
        self.db_dropdown.addItem(db_path)

        # Buttons verbinden
        self.ui.buttonSave.clicked.connect(self.save_data)
        self.ui.buttonDelete.clicked.connect(self.delete_record)
        self.ui.pushLoadDB.clicked.connect(self.add_database_via_dialog)

        # Tabelle initial laden
        self.load_data()

    def add_database_via_dialog(self):
        # Neue vorhandene Datenbank auswählen
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Datenbank auswählen",
            "",
            "JSON-Dateien (*.json)"
        )
        if path and path not in self.databases:
            self.databases.append(path)
            self.db_dropdown.addItem(path)
            self.ui.logOutput.append(f"Datenbank hinzugefügt: {path}")

    def create_new_database(self):
        # Neue Datenbank erstellen
        path, _ = QFileDialog.getSaveFileName(
            self,
            "Neue Datenbank erstellen",
            "",
            "JSON-Dateien (*.json)"
        )
        if path:
            if not path.endswith(".json"):
                path += ".json"
            if not os.path.exists(path):
                TinyDB(path).close()  # leere DB erzeugen
                self.databases.append(path)
                self.db_dropdown.addItem(path)
                self.ui.logOutput.append(f"Neue Datenbank erstellt: {path}")
            else:
                self.ui.logOutput.append(f"Datenbank existiert bereits: {path}")

    def switch_database(self, index):
        global db, db_path
        db_path = self.databases[index]
        db = TinyDB(db_path)
        self.ui.logOutput.append(f"Datenbank gewechselt zu: {db_path}")
        self.load_data()

    def load_data(self):
        records = db.all()
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setRowCount(len(records))
        for row_index, eintrag in enumerate(records):
            self.ui.tableWidget.setItem(row_index, 0, QTableWidgetItem(str(eintrag.doc_id)))
            self.ui.tableWidget.setItem(row_index, 1, QTableWidgetItem(eintrag["name"]))
            self.ui.tableWidget.setItem(row_index, 2, QTableWidgetItem(str(eintrag["age"])))
            self.ui.tableWidget.setItem(row_index, 3, QTableWidgetItem(eintrag["city"]))
        self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "Name", "Alter", "Stadt"])

    def save_data(self):
        name = self.ui.inputName.text()
        age = self.ui.inputAge.text()
        city = self.ui.inputCity.text()

        entry = {"name": name, "age": age, "city": city}
        db.insert(entry)
        self.ui.logOutput.append(f"Gespeichert: {entry}")
        self.load_data()

    def delete_record(self):
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row < 0:
            self.show_msg("Bitte zuerst einen Eintrag auswählen.")
            return

        doc_id = int(self.ui.tableWidget.item(selected_row, 0).text())
        confirm = QMessageBox.question(
            self,
            "Löschen",
            "Diesen Eintrag wirklich löschen?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if confirm == QMessageBox.Yes:
            db.remove(doc_ids=[doc_id])
            self.load_data()

    def show_msg(self, text):
        QMessageBox.information(self, "Info", text)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
