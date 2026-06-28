from app.llm.gemini import llm

response = llm.invoke("Say Hello")

print(response.content)