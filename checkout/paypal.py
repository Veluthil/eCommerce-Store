import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment

from core.settings.base import PAYPAL_CLIENT_ID, PAYPAL_SECRET


class PayPalClient:
    def __init__(self):
        self.client_id = PAYPAL_CLIENT_ID
        self.client_secret = PAYPAL_SECRET
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
