import os
import stripe
from flask import Flask, render_template, jsonify, request, Response

STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")
STRIPE_PUBLISHABLE_KEY = os.environ.get("STRIPE_PUBLISHABLE_KEY")
GOOGLE_MERCHANT_ID = os.environ.get("GOOGLE_MERCHANT_ID")

app = Flask(__name__)
stripe.api_key = STRIPE_SECRET_KEY


@app.route("/")
def index():
    return render_template("index.html", **{
        "STRIPE_PUBLISHABLE_KEY": STRIPE_PUBLISHABLE_KEY,
        "GOOGLE_MERCHANT_ID": GOOGLE_MERCHANT_ID
    })


@app.route("/charge", methods=["POST"])
def charge():
    token = request.form.get("token")
    amount = int(float(request.form.get("amount")) * 100)  # convert to int for Stripe

    if token == 'TEST_GATEWAY_TOKEN':
        print 'Android Pay Test Environment Token Provided.  Mocking it out...'
        token = stripe.Token.create(
            card={
                "number": '4242424242424242',
                "exp_month": 12,
                "exp_year": 2018,
                "cvc": '123'
            },
        )

    if not token or not amount:
        return "ERROR", 400

    # Create Customer
    cus = stripe.Customer.create(
        description="Android Pay for the Web Test",
        source=token,
        email="test@test.test",
        metadata={
            "token": token,
        }
    )

    # Create Charge
    ch = stripe.Charge.create(
        amount=amount,
        customer=cus.id,
        currency="usd"
    )
    return jsonify({'charge': ch, 'customer': cus})


if __name__ == "__main__":

    if not STRIPE_SECRET_KEY:
        raise ValueError("Please pass the `STRIPE_SECRET_KEY` envionment variable.")

    if not STRIPE_PUBLISHABLE_KEY:
        raise ValueError("Please pass the `STRIPE_PUBLISHABLE_KEY` envionment variable.")

    app.run(debug=True)
