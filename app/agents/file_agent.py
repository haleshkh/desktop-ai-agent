from app.tools.file_tools import create_folder


def file_agent(query: str):

    words = query.split()

    folder_name = words[-1]

    return create_folder(folder_name)