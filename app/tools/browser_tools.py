import subprocess
import webbrowser


def open_google():
    webbrowser.open("https://www.google.com")
    return "Google opened successfully."


def open_youtube():
    webbrowser.open("https://www.youtube.com")
    return "YouTube opened successfully."


def open_github():
    webbrowser.open("https://github.com")
    return "GitHub opened successfully."


def open_vscode():
    try:
        subprocess.Popen(["code"])
        return "VS Code opened successfully."
    except Exception as e:
        return f"Error opening VS Code: {e}"