form = document.querySelector('form')

form.addEventListener('submit', ()=>{
    document.querySelector('[type=submit]').innerHTML = 'Loading...'
})


function show_and_hide_password(input){
    if(document.querySelector(input).type == 'password'){
        document.querySelector(input).type = 'text'
    }else{
        document.querySelector(input).type = 'password'
    }
}

