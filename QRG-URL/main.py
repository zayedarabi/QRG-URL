import qrcode
import pandas as pd
import os
from datetime import datetime

class QRManager:
    def __init__(self, db_file="qr_database.xlsx"):
        self.db_file = db_file
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.base_path, self.db_file)
        
        if os.path.exists(self.db_path):
            self.df = pd.read_excel(self.db_path)
        else:
            self.df = pd.DataFrame(columns=["ID", "Name", "URL", "Date"])

    def generate(self, url, name):
        img = qrcode.make(url)
        file_path = os.path.join(self.base_path, f"{name}.png")
        img.save(file_path)
        
        new_entry = {
            "ID": len(self.df) + 1,
            "Name": name,
            "URL": url,
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.df = pd.concat([self.df, pd.DataFrame([new_entry])], ignore_index=True)
        self.df.to_excel(self.db_path, index=False)
        print(f"Saved: {file_path}")

    def delete_qr(self, name):
        if name in self.df['Name'].values:
            file_path = os.path.join(self.base_path, f"{name}.png")
            if os.path.exists(file_path):
                os.remove(file_path)
            
            self.df = self.df[self.df['Name'] != name]
            self.df.to_excel(self.db_path, index=False)
            print(f"Deleted: {name}")
        else:
            print("Name not found.")

    def list_all(self):
        print("\n--- Current Records ---")
        if self.df.empty:
            print("No data available.")
        else:
            print(self.df[["Name", "URL", "Date"]])
        print("-----------------------\n")

if __name__ == "__main__":
    manager = QRManager()
    while True:
        print("1. Generate QR\n2. List All\n3. Delete QR\n4. Exit")
        choice = input("Select: ")
        
        if choice == "1":
            manager.generate(input("URL: "), input("Name: "))
        elif choice == "2":
            manager.list_all()
        elif choice == "3":
            manager.delete_qr(input("Enter Name to Delete: "))
        elif choice == "4":
            break