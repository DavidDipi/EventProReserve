document.addEventListener('DOMContentLoaded', function () {
/*
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
    });*/


});

$(".confirmar").submit(function(e) {
    e.preventDefault();
    const form = this;
    const eventId = $(form).find('input[name="deleteRecord"]').val(); // Obtén el valor del campo oculto

    Swal.fire({
        title: '¿Está seguro de eliminar?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, eliminar!',
        cancelButtonText: 'No, cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            form.action = 'delete_event/' + eventId;
      
            // Muestra la alerta de éxito
            Swal.fire({
              position: 'top-end',
              icon: 'success',
              title: 'El registro se ha borrado con éxito',
              showConfirmButton: false,
              timer: 1500
            });
      
            // Envía el formulario con la nueva URL después de un breve retraso
            setTimeout(function() {
              form.submit();
            }, 1500);
        }
    })
});
