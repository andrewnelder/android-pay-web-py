
## Run the demo

This demo requires that [ngrok](https://ngrok.io/) be installed or that you have some means of accessing the local web service from an Android device.  This is a demonstration only and absolutely should *NOT* be used in a production environment (as Flask is set to run in debug-mode for auto-reload).

To deploy directly to Heroku, click this button:

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

### Step #0: Install the Requirements via PIP

```
pip install -r requirements.txt
```

### Step #1: Turn on your Python web server (listening on localhost:5000)

Replace the keys below and run the following command in your terminal.

```bash
STRIPE_SECRET_KEY=sk_test_XXX STRIPE_PUBLISHABLE_KEY=pk_test_XXX GOOGLE_MERCHANT_ID=XXX python run.py
```

### Step #2: Route ngrok to host port 5000

Start an ngrok route to your machine.

```bash
ngrok http 5000
```

### Step #3: Access the demo from the browser on your Android device

```bash
https://<YOURNGROKADDRESS>.ngrok.io/
```

You will want to make sure that your device has developer tools and usb debugging enabled, so that you may view the device and its console from your Chrome browser and it's developer tools suite.

*NOTE: This is over HTTPS!*
