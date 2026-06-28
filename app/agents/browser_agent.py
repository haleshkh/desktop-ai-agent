from app.tools.browser_tools import (
    open_google,
    open_youtube,
    open_github,
    open_vscode
)
def browser_agent(query: str):

    query = query.lower()

    if "google" in query:
        return open_google()

    elif "youtube" in query:
        return open_youtube()

    elif "github" in query:
        return open_github()

    elif "vs code" in query or "vscode" in query:
        return open_vscode()

    return "Website or application not supported."

