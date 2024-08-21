from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual Open Exchange Rates API key
API_KEY = 'YOUR_API_KEY'

@app.route('/', methods=['GET', 'POST'])
def currency_converter():
    if request.method == 'POST':
        source_currency = request.form['source_currency']
        target_currency = request.form['target_currency']
        amount = float(request.form['amount'])

        # Fetch exchange rates from Open Exchange Rates API
        url = f'https://openexchangerates.org/api/latest.json?app_id={API_KEY}'
        response = requests.get(url)
        data = response.json()
        rates = data['rates']

        if source_currency in rates and target_currency in rates:
            converted_amount = amount * (rates[target_currency] / rates[source_currency])
            return render_template('result.html', amount=amount, source=source_currency,
                                   target=target_currency, converted=converted_amount)
        else:
            return 'Invalid currency codes. Please try again.'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
