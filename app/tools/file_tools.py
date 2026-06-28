from pathlib import Path

WORKSPACE = Path("workspace")


def create_folder(folder_name: str):

    folder_path = WORKSPACE / folder_name

    folder_path.mkdir(parents=True, exist_ok=True)

    return f"Folder '{folder_name}' created successfully."