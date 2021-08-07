document.addEventListener('DOMContentLoaded', function(){
    let btn = document.querySelector('input[type=submit]');
    btn.addEventListener('click', function(event){
        event.preventDefault();
        let amount = document.getElementById('amount')
        let currency = document.getElementById('currency')
        let description = document.getElementById('description')

        let entry = {
            amount: amount.value,
            currency: currency.value,
            description: description.value,
            shop_id: '5',
            shop_order_id: '109',
            shop_amount: amount.value,
            shop_currency: currency.value,
            payer_currency: currency.value,
            payer_account: 'support@piastrix.com'
        };

        fetch('/', {
            method: 'POST',
            body: JSON.stringify(entry),
            headers: new Headers({
                'content-type': 'application/json'
            })
        }).then(function(response) {
            response.json().then(function(value) {
                uri = value['url']
                method = value['method']
                delete value['url']
                delete value['method']
                Object.keys(value).forEach(function(key) {
                    field = document.getElementById(key)
                    form = document.getElementById('pay')
                    if (field == null) {
                        let input = document.createElement('input');
                        input.setAttribute('type', 'hidden');
                        input.setAttribute('name', key);
                        input.setAttribute('value', value[key]);
                        form.appendChild(input);
                    };

                    form.setAttribute('action', uri);
                    form.setAttribute('method', method);
                    form.submit();
                });
            });
        });
    });
});
