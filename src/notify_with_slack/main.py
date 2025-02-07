import logging
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
TOKEN = ""

# ID of the channel you want to send the message to
channel_id = ""

def send_message_with_slack(bot_token, channel_id, message: str):
    client = WebClient(token=bot_token)
    logger = logging.getLogger(__name__)

    try:
        # Call the chat.postMessage method using the WebClient
        result = client.chat_postMessage(
            channel=channel_id, 
            text=str(message)
        )
        logger.info(result)

    except SlackApiError as e:
        logger.error(f"Error posting message: {e}")

send_message_with_slack(TOKEN, channel_id, "wow")