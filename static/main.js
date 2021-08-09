document.addEventListener('DOMContentLoaded', function(){
    let form = document.getElementById('form');
    form.addEventListener('submit', function(event){
        event.preventDefault();
        let amount = document.getElementById('amount').value
        let currency = document.getElementById('currency').value
        let description = document.getElementById('description').value

        let entry = {
            amount: amount,
            currency: currency,
            description: description,
        };

        fetch('/', {
            method: 'POST',
            body: JSON.stringify(entry),
            headers: new Headers({
                'content-type': 'application/json'
            })
        }).then(function(response) {
            response.json().then(function(data) {
                let method = data['method']
                let action = data['action']
                delete data.method
                delete data.action
                let form = document.createElement('form')
                form.method = method
                form.action = action
                for (let key in data) {
                    let element = document.createElement('input')
                    element.setAttribute('type', 'hidden') 
                    element.setAttribute('name', key)
                    element.setAttribute('value', data[key])
                    form.appendChild(element)
                }
                document.body.appendChild(form)
                form.submit()
            });
        });
    });
});
