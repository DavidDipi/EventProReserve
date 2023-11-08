// EDITAR TIPO DE EVENTO
$(".form_edit_tEvent").submit(function(e) {
    e.preventDefault();
    const form = this;
    const eventId = $(form).find('input[name="editTypeEvent"]').val(); // Obtén el valor del campo oculto
    const nameTypeEvent = $(form).find('input[name="nameTypeEvent"]').val();
    const descriptionTypeEvent = $(form).find('input[name="descriptionTypeEvent"]').val();

    console.log(nameTypeEvent);
    console.log(descriptionTypeEvent);


    if (nameTypeEvent == '' || descriptionTypeEvent == ''){
        Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: 'Campos no validos!',
        });
    }else{
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
    }
});

// ELIMINAR TIPO DE EVENTO
$(".confirmar_tEvent").submit(function(e) {
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

// EDITAR CANTIDAD DE PERSONAS
$(".form_edit_cPer").submit(function(e) {
  e.preventDefault();
  const form = this;
  const cantPersId = $(form).find('input[name="editCantPers"]').val(); // Obtén el valor del campo oculto
  const AmountPe = $(form).find('input[name="AmountPe"]').val();
  const costAmountPe = $(form).find('input[name="costAmountPe"]').val();

  if (AmountPe == '' || costAmountPe == ''){
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: 'Campos no validos!',
    });
  }else{
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
            form.action = 'e_cant_pers/' + cantPersId;
      
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
  }
});

// ELIMINAR CANTIDAD DE PERSONAS
$(".confirmar_cPer").submit(function(e) {
  e.preventDefault();
  const form = this;
  const cantPersId = $(form).find('input[name="deleteRecord"]').val(); // Obtén el valor del campo oculto

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
          form.action = 'd_cant_pers/' + cantPersId;
    
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
