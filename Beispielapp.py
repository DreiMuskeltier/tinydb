from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from tinydb import TinyDB
from ui.Beispiel import Ui_MainWindow  # erzeugt durch pyside6-uic

db = TinyDB("datenbank.json")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Button verbinden
        self.ui.buttonSave.clicked.connect(self.save_data)
        self.ui.buttonDelete.clicked.connect(self.delete_record)
        self.ui.pushLoadDB.clicked.connect(self.load_data)
    def load_data(self):
        records = db.all()
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setRowCount(len(records))
        for row_index, eintrag in enumerate(records):
            self.ui.tableWidget.setItem(row_index, 0, QTableWidgetItem(str(eintrag.doc_id))) 
            self.ui.tableWidget.setItem(row_index, 1, QTableWidgetItem(eintrag["name"]))
            self.ui.tableWidget.setItem(row_index, 2, QTableWidgetItem(str(eintrag["age"])))
            self.ui.tableWidget.setItem(row_index, 3, QTableWidgetItem(eintrag["city"]))
            self.ui.tableWidget.setHorizontalHeaderLabels(["", "Name", "Alter", "Stadt"])

    def save_data(self):
        name = self.ui.inputName.text()
        age = self.ui.inputAge.text()
        city = self.ui.inputCity.text()

        entry = {"name": name, "age": age, "city": city}
        db.insert(entry)
        
        self.ui.logOutput.append(f"Gespeichert: {entry}")
    def delete_record(self):
        """Ausgewählten Datensatz löschen."""
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
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
