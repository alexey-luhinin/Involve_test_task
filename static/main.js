document.addEventListener('DOMContentLoaded', function(){
    let btn = document.querySelector('input[type=submit]');
    btn.addEventListener('click', function(event){
        event.preventDefault();
        let amount = document.querySelector('input[name=amount]').value;
        let currency = document.querySelector('select[name=currency]').value;
        let shop_id = document.querySelector('input[name=shop_id]').value;
        let shop_order_id = document.querySelector('input[name=shop_order_id]').value;

        fetch('/', {
            method: 'POST',
            body: `{"amount": "${amount}", "currency": "${currency}", "shop_id": "${shop_id}", "shop_order_id": "${shop_order_id}"}`
        }).then(function(response) {
            response.json().then(function(value) {
                document.querySelector('input[name=sign]').value = value.sign
                document.forms['pay'].submit()
            });
        });
        

    });
});
