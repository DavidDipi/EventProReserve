document.addEventListener('DOMContentLoaded', function () {

    const form = document.querySelector('.form_registro');
    console.log(form);
    const submitButton = form.querySelector('.btn');
    console.log("Hollaaaa");

    
    console.log(submitButton);
    submitButton.addEventListener('click', function (event) {
         // Evita que el formulario se envíe de forma predeterminada
        
            
        console.log('ENVIADOOOOOOOOO ANTES');
        
        fetch('/admin/events/new_event', {
            method: 'POST',
            // ...
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                Swal.fire({
                    title: 'Éxito',
                    text: data.message,
                    icon: 'success',
                });
                window.location.href("/new_event")
            } else {
                Swal.fire({
                    title: 'Error',
                    text: data.message,
                    icon: 'error',
                });
            }
        })
        
        

        console.log("despues del fetch")
        
        
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
