




document.querySelector('[name=file]').addEventListener('change', ()=>
{
    
    const input_file = document.querySelector('[name=file]')
    var image_preview = document.querySelector('#image-preview')

    if (image_preview == null){
        image_preview = document.querySelector('#profile-picture')
    }
    const [file] = input_file.files
    image_preview.src = URL.createObjectURL(file)
    $('#preview-default').fadeOut()
    setTimeout(()=>{
        $(image_preview).fadeIn('1000')
    }, 1000)
    setTimeout(()=>{
        $('#btn-send-picture').fadeIn()
    }, 2000)
    

})

function back_to_top(){
    $('html, body').animate({scrollTop:0}, 'slow')

}