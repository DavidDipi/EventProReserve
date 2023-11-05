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

$(".form_edit").submit(function(e) {
    e.preventDefault();
    const form = this;
    const eventId = $(form).find('input[name="editTypeEvent"]').val(); // Obtén el valor del campo oculto

    Swal.fire({
        title: '¿Está seguro de editar?',
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, editar!',
        cancelButtonText: 'No, cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            form.action = 'edit_event/' + eventId;
      
            // Muestra la alerta de éxito
            Swal.fire({
              position: 'top-end',
              icon: 'success',
              title: 'El registro se ha editado con éxito',
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


