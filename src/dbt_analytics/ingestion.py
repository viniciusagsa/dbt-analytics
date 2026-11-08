from pathlib import Path
import duckdb


# Diretórios do projeto
PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DIR = PROJECT_ROOT / "data" / "raw"
WAREHOUSE_DIR = PROJECT_ROOT / "data" / "warehouse"

DATABASE_PATH = WAREHOUSE_DIR / "jaffle_shop.duckdb"


def load_raw_data():
    """Load source CSV files into DuckDB raw schema."""

    WAREHOUSE_DIR.mkdir(parents=True, exist_ok=True)

    connection = duckdb.connect(str(DATABASE_PATH))

    try:
        connection.execute("CREATE SCHEMA IF NOT EXISTS raw")

        files = {
            "raw_customers": RAW_DIR / "raw_customers.csv",
            "raw_orders": RAW_DIR / "raw_orders.csv",
            "raw_payments": RAW_DIR / "raw_payments.csv",
        }

        for table_name, file_path in files.items():

            if not file_path.exists():
                raise FileNotFoundError(
                    f"File not found: {file_path}"
                )

            connection.execute(
                f"""
                CREATE OR REPLACE TABLE raw.{table_name} AS
                SELECT *
                FROM read_csv_auto(?)
                """,
                [str(file_path)],
            )

            count = connection.execute(
                f"SELECT COUNT(*) FROM raw.{table_name}"
            ).fetchone()[0]

            print(f"{table_name}: {count} records loaded")

    finally:
        connection.close()


if __name__ == "__main__":
    load_raw_data()
