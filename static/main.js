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
            shop_order_id: '109'
        };

        fetch('/', {
            method: 'POST',
            body: JSON.stringify(entry),
            headers: new Headers({
                'content-type': 'application/json'
            })
        }).then(function(response) {
            response.json().then(function(value) {
                Object.keys(value).forEach(function(key) {
                    field = document.getElementById(key)
                    if (field == null) {
                        let input = document.createElement('input');
                        input.setAttribute('type', 'hidden');
                        input.setAttribute('name', key);
                        input.setAttribute('value', value[key]);
                        form = document.getElementById('pay')
                        form.appendChild(input)
                        form.submit()
                    }
                });
            });
        });
    });
});
