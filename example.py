from llm_api.chat_completion import Function, Chat, Message
from pydantic import BaseModel, Field
from rich import print


def weather(zip: str = Field(description="The ZIP code of the city.")):
    """Get the weather report for a given location."""
    return "It's raining sideways!"


def get_zip_code(city: str) -> str:
    return "02110"


chat = Chat(
    model="gpt-4",
    functions=[
        Function.from_annotated_function(weather),
        Function.from_annotated_function(get_zip_code),
    ],
    messages=[Message(role="user", content="what's the weather like in Boston?")],
)

# print(chat.model_dump(exclude_none=True))
for i in chat.iterator():
    print(i)
