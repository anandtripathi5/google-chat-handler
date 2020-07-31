# Google Chat Handler
Python logging handler to push the logs to google chat root using the webhook
url. Just create a room or use existing room and create a webhook url of a bot 
and pass the URL to this GoogleChatHandler library.



Installation Instruction!
===================

>- Activate your Virtual Environment.
>- `pip install google-chat-handler`

----------

# Features

 1. Google chat handler library give us the GoogleChatHandler class that we have to use
 and attach the handler to any logger of class logging. It is also compatible with flask and django logger.

# Usage

 1. Import Google Chat Handler
	 -  `from google_chat import GoogleChatHandler`

 2. Initialize the chat handler
     -  `handler = GoogleChatHandler('https://chat.googleapis.com/v1/spaces/xxxxxxx')`

 3. Set the level of the handler
     - let say if we want to push only error logs to google chat as a alert
     -  `handler.setLevel(logging.ERROR)`
     
 4. Add the handler to the existing logger
     -  `logger.addHandler(handler)`
     
 5. Now use the google chat handler
     -  `logger.error("This message will appear in google chat")`
# Example

```python
import logging
from handler import GoogleChatHandler
# logger of your project

# Get default logger
logger = logging.getLogger()
# set default level of the logger
logger.setLevel(logging.DEBUG)

# Create handler for google chat handler
handler = GoogleChatHandler(webhook_url="https://chat.googleapis.com/v1/spaces/XXXXXXXXX")
# Set level of the Google chat handler for which loglevel we have to send logs to google
handler.setLevel(logging.ERROR)
# Add the handler to the logger
logger.addHandler(handler)

logger.info("normal logger info")
logger.debug("normal logger debug")

# Only below log will be pushed to google chat
logger.error("google chat logger error")

```
