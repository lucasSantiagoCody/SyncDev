

function show(element){
    $(element).fadeIn()
}
function hide(element, fast){
    if(fast='true'){
        $(element).fadeOut()
    }else{
        $(element).fadeOut(2000) 
    }
}



if(document.querySelectorAll('.alert')){
    setTimeout(()=>{
        $('.alert').fadeOut(2000)
    }, 10000)
}