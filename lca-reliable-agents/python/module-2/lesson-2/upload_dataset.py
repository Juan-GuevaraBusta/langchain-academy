from pathlib import Path

from dotenv import load_dotenv
from langsmith import Client

load_dotenv()

DATASET_NAME = "officeflow-dataset"
CSV_PATH = Path(__file__).parent / "officeflow-dataset.csv"

client = Client()

if client.has_dataset(dataset_name=DATASET_NAME):
    print(f"Dataset '{DATASET_NAME}' already exists, skipping upload.")
else:
    dataset = client.upload_csv(
        csv_file=str(CSV_PATH),
        input_keys=["question"],
        output_keys=[],
        name=DATASET_NAME,
        description="OfficeFlow customer questions",
    )
    print(f"Created dataset '{dataset.name}' ({dataset.id})")
