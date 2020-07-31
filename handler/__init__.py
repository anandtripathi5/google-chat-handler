import json
import logging
from concurrent.futures.thread import ThreadPoolExecutor

from httplib2 import Http


class GoogleChatHandler(logging.Handler):
    """
    A handler class which sends an Google Chat message for each logging event.
    """
    def __init__(self, webhook_url, threaded=False, threaded_workers=1):
        """
        Initialize the handler.

        webhook_url: Add a webhook url to the google chat and provide the url
        into this parameter

        threaded: default value -> false. As the handler is pushing the logs
        to Google Chat that might take time so this flag will make the process
        threaded

        threaded_workers: default value -> 1. Applicable if threaded value is True.
        """
        logging.Handler.__init__(self)
        if not webhook_url:
            raise ValueError("Webhook url not provided")
        self.webhook_url = webhook_url
        self.http_obj = Http()
        self.threaded = threaded
        if threaded:
            self.pool = ThreadPoolExecutor(max_workers=threaded_workers)

    def emit(self, record):
        """
        Emit a record.

        Format the record and send it to the specified addressees.
        """
        try:
            kwargs = dict(
                uri=self.webhook_url,
                method='POST',
                headers={'Content-Type': 'application/json; charset=UTF-8'},
                body=json.dumps(dict(
                    text=self.format(record)
                ))
            )
            if self.threaded:
                self.pool.submit(
                    fn=self.http_obj.request,
                    **kwargs
                )
            else:
                self.http_obj.request(**kwargs)
        except Exception:
            try:
                self.handleError(record)
            except Exception as e:
                print(e)
