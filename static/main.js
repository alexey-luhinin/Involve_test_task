// let response = fetch('/', {
//     method: 'POST',
//     body: `{"amount": "10.0", "description": "hello"}`
// });

// console.log(response)

document.addEventListener('DOMContentLoaded', function(){
    let btn = document.querySelector('input[type=submit]');
    btn.addEventListener('click', function(event){
        event.preventDefault();
    })
})
