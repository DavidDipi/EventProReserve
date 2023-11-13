/* ----------------- TIPO DE EVENTO -------------- */

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

/* ----------------- CANTIDAD DE PERSONAS -------------- */

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

/* ----------------- MOBILIARIO ADICIONAL -------------- */
// EDITAR MOBILIARIO ADICIONAL
$(".form_edit_adMob").submit(function(e) {
  e.preventDefault();
  const form = this;
  const idAdMob = $(form).find('input[name="editAdMob"]').val(); // Obtén el valor del campo oculto
  const nameAdMob = $(form).find('input[name="nameAdMob"]').val();
  const costAdMob = $(form).find('input[name="costAdMob"]').val();

  if (nameAdMob == '' || costAdMob == ''){
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
            form.action = 'e_ad_mob/' + idAdMob;
      
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

// ELIMINAR MOBILIARIO ADICIONAL
$(".confirmar_adMob").submit(function(e) {
  e.preventDefault();
  const form = this;
  const idAdMob = $(form).find('input[name="deleteRecord"]').val(); // Obtén el valor del campo oculto

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
          form.action = 'd_ad_mob/' + idAdMob;
    
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

/* ----------------- DECORACION ADICIONAL -------------- */
// EDITAR DECORACION ADICIONAL
$(".form_edit_adDec").submit(function(e) {
  e.preventDefault();
  const form = this;
  const idAdDec = $(form).find('input[name="editAdDec"]').val(); // Obtén el valor del campo oculto
  const nameAdDec = $(form).find('input[name="nameAdDec"]').val();
  const costAdDec = $(form).find('input[name="costAdDec"]').val();

  if (nameAdDec == '' || costAdDec == ''){
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
            form.action = 'e_ad_dec/' + idAdDec;
      
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

// ELIMINAR DECORACION ADICIONAL
$(".confirmar_adDec").submit(function(e) {
  e.preventDefault();
  const form = this;
  const idAdDec = $(form).find('input[name="deleteRecord"]').val(); // Obtén el valor del campo oculto

  console.log(idAdDec)

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
          form.action = 'd_ad_dec/' + idAdDec;
    
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


/* ----------------- ALIMENTO ADICIONAL -------------- */
// EDITAR ALIMENTO ADICIONAL
$(".form_edit_adAli").submit(function(e) {
  e.preventDefault();
  const form = this;
  const idAdAli = $(form).find('input[name="editAdAli"]').val(); // Obtén el valor del campo oculto
  const nameAdAli = $(form).find('input[name="nameAdAli"]').val();
  const costAdAli = $(form).find('input[name="costAdAli"]').val();

  if (nameAdAli == '' || costAdAli == ''){
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
            form.action = 'e_ad_ali/' + idAdAli;
      
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

// ELIMINAR ALIMENTO ADICIONAL
$(".confirmar_adAli").submit(function(e) {
  e.preventDefault();
  const form = this;
  const idAdAli = $(form).find('input[name="deleteRecord"]').val(); // Obtén el valor del campo oculto

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
          form.action = 'd_ad_ali/' + idAdAli;
    
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