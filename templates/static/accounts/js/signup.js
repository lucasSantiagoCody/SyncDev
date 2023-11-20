input_username =  document.querySelector('#id_username')
input_email =  document.querySelector('#id_email')
input_password1 = document.querySelector('#id_password1')
input_password2 = document.querySelector('#id_password2')
signup_form = document.querySelector('#signup-form')



function ValidateEmail(){

  const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]')  
  data = new FormData()
  data.append('email', input_email.value)

  fetch('/accounts/validate_email/', {
    method: 'POST',
    headers: {
      'X-CSRFToken': csrf_token.value,
    },
    body: data,
  }).then((result)=>{
    return result.json()
  }).then((data)=>{
    if (data['email_status'] !== 'valid'){

      div_email_status = document.querySelector('#div_email_status')
      var timeleft = 8;
      var countdown = setInterval(function()
      {
        if(timeleft <= 0){
          clearInterval(countdown);
        } else {
            div_email_status.innerHTML = data['email_status'] + ' ' + timeleft + 'secs'
          }
          timeleft -= 1;
      }, 1000);
      $('#div_email_status').fadeIn()
    }
    
  })
  
  
  
}



input_email.addEventListener('keyup', (e)=>{
  if(input_email.value.trim().indexOf('.com') !== -1){

    ValidateEmail()
  }
})


function signup(){

  const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]')
  data = new FormData()
  data.append('username', input_username)
  data.append('email', input_email)
  data.append('password1', input_password1)
  data.append('password2', input_password2)

  fetch('/accounts/signup/',{
    method: 'POST',
    headers: {
      'X-CSRFToken': csrf_token.value,
    },
    body: data,
  }).then((result)=>{
    return result.json()
  }).then((data)=>{
    signup_status = data['status']
    fields = data['context']

    console.log(signup_status)
    console.log(fields['username'])
  })


}

signup_form.addEventListener('submit', (e)=>{
  e.preventDefault()
  signup()
})