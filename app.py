import chainlit as cl

@cl.on_message  # this function will be called every time a user inputs a message in the UI
async def main(message: str, message_id: str):
    """
    This function is called every time a user inputs a message in the UI.
    It sends back an intermediate response from Tool 1, followed by the final answer.

    Args:
        message: The user's message.

    Returns:
        None.
    """

    # Send an intermediate response from Tool 1.
    await cl.Message(
        author="Tool 1",
        content=f"Response from tool1",
        parent_id=message_id,
    ).send()

    # Send the final answer.
    await cl.Message(content=f"This is the final answer").send()