from pydantic import BaseModel,Field
from typing_extensions import TypedDict
from typing import List, Annotated
from langgraph.graph.message import BaseMessage, add_messages

class State(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]