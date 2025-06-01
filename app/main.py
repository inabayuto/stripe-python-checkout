import os
import stripe
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='templates')
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")


@app.route('/')
def index():
    return render_template('index.html', public_key=os.getenv("STRIPE_PUBLISHABLE_KEY"))


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'jpy',
                'product_data': {'name': 'テスト商品'},
                'unit_amount': 500
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:4242/success',
        cancel_url='http://localhost:4242/cancel',
    )
    return jsonify(id=session.id)


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/cancel')
def cancel():
    return render_template('cancel.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4242)
