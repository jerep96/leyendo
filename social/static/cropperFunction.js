$(document).ready(function() {

    const alertBox = document.getElementById('alert-box')
    const imageForm = document.getElementById('image-form')
    const imageBox = document.getElementById('image-box')
    const inputB = document.getElementById('id_imageB')
    const inputS = document.getElementById('id_imageS')
    const inputO = document.getElementById('id_imageO')
    const csrf = document.getElementsByName('csrfmiddlewaretoken')
    const confirmBtn = document.getElementById('confirm-btn')

    inputB.addEventListener('change', () =>{
        alertBox.innerHTML = ""
        confirmBtn.classList.remove('not-visible')
        const img_data = inputB.files[0]
        const url = URL.createObjectURL(img_data)
        imageBox.innerHTML = `<img src="${url}" id=imageB width="500px">`

        let $imageB = $('#imageB')

        $imageB.cropper({
            aspectRatio: 9 / 9,
            crop: function (event) {
                console.log(event.detail.x);
                console.log(event.detail.y);
                console.log(event.detail.width);
                console.log(event.detail.height);
                console.log(event.detail.rotate);
                console.log(event.detail.scaleX);
                console.log(event.detail.scaleY);
            }
        });

        let cropper = $imageB.data('cropper')

        confirmBtn.addEventListener('click', () => {
            cropper.getCroppedCanvas().toBlob((blob) => {
                const fd = new FormData()
                fd.append('csrfmiddlewaretoken', csrf[0].value)
                fd.append('file', blob, 'my-image.png')

                console.log(fd)

                $.ajax({
                    type: 'POST',
                    url: imageForm.action,
                    enctype: 'multipart/form-data',
                    data: fd,
                    success: function(){
                        console.log('success')
                        alertBox.innerHTML = `<div class="alert alert-success" role="alert">
                                                Guardado exitosamente
                                            </div>`
                    },
                    error: function(error){
                        console.log('error', error)
                        alertBox.innerHTML = `<div class="alert alert-danger" role="alert">
                                                Ups...algo salio mal
                                            </div>`
                    },
                cache: false,
                contentType: false,
                processData: false,
                })
            })
        })

    })
})
