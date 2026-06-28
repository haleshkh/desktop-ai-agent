from app.llm.gemini import llm


def route_request(query: str):

    prompt = f"""
You are an AI routing agent.

Choose ONLY one route.

Available routes:
- file
- browser
- terminal

Rules:
- Opening websites or applications (VS Code, Chrome, Google, GitHub, YouTube) -> browser
- Creating, deleting, reading folders or files -> file
- Running commands -> terminal

User Request:
{query}

Return ONLY ONE WORD:
file
browser
terminal
"""

    response = llm.invoke(prompt)

    route = response.content.strip().lower()

    # Safety check
    if route not in ["file", "browser", "terminal"]:
        if "vs code" in query.lower():
            return "browser"
        elif any(word in query.lower() for word in ["google", "youtube", "github", "chrome"]):
            return "browser"
        elif any(word in query.lower() for word in ["folder", "file", "directory"]):
            return "file"
        else:
            return "terminal"

    return route