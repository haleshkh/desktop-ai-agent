from langgraph.graph import StateGraph, END

from app.graph.state import AgentState

from app.agents.manager_agent import route_request
from app.agents.file_agent import file_agent
from app.agents.browser_agent import browser_agent


def manager_node(state: AgentState):
    state["route"] = route_request(state["query"])
    return state


def file_node(state: AgentState):
    state["response"] = file_agent(state["query"])
    return state


def browser_node(state: AgentState):
    state["response"] = browser_agent(state["query"])
    return state


# Create the graph FIRST
graph = StateGraph(AgentState)

# Add nodes
graph.add_node("manager", manager_node)
graph.add_node("file", file_node)
graph.add_node("browser", browser_node)

# Entry point
graph.set_entry_point("manager")


# Router
def router(state: AgentState):

    if state["route"] == "file":
        return "file"

    elif state["route"] == "browser":
        return "browser"

    return END


# Conditional routing
graph.add_conditional_edges(
    "manager",
    router,
    {
        "file": "file",
        "browser": "browser",
        END: END
    }
)

# End edges
graph.add_edge("file", END)
graph.add_edge("browser", END)

# Compile graph
desktop_graph = graph.compile()