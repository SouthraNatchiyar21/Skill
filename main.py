import sqlite3
import pandas as pd


# ----------------------------------------
# ✅ STEP 1: Setup Database and Sample Table
# ----------------------------------------
def setup_db():
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    # Optional: Add some sample data
    sample_data = [
        ("Alice", "alice@example.com"),
        ("Bob", "bob@example.com")
    ]
    cursor.executemany('''
        INSERT INTO users (name, email) VALUES (?, ?)
    ''', sample_data)

    conn.commit()
    conn.close()
    print("✅ Database and sample table set up.")


# ----------------------------------------
# 📤 STEP 2: Export table data to CSV
# ----------------------------------------
def export_db_as_csv(db_path: str, table_name: str, output_file: str):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    df.to_csv(output_file, index=False)
    conn.close()
    print(f"✅ Exported data from '{table_name}' to '{output_file}'")


# ----------------------------------------
# 📥 STEP 3: Import data from CSV into DB
# ----------------------------------------
def csv_to_db(db_path: str, table_name: str, input_file: str):
    conn = sqlite3.connect(db_path)
    df = pd.read_csv(input_file)
    df.to_sql(table_name, conn, if_exists='append', index=False)
    conn.close()
    print(f"✅ Imported data from '{input_file}' into '{table_name}' table")


# ----------------------------------------
# 🚀 STEP 4: Run everything
# ----------------------------------------
if __name__ == "__main__":
    setup_db()

    # Export data to CSV
    export_db_as_csv("example.db", "users", "users_export.csv")

    # OPTIONAL: To test importing, first prepare a CSV like 'input.csv'
    # csv_to_db("example.db", "users", "input.csv")  # Uncomment to test import
