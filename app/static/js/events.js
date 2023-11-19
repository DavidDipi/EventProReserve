


// Definir variables
let typeEvent, numberPerson, adMob, adDec, adAli, others, dataMob, dataDec, dataAli, dataOtServ;

dataMob = '';
dataDec = '';
dataAli = '';
dataOtServ = '';

// Función para agregar mobiliario
function agregarMobiliario() {
    $('input[name="mobiliario[]"]:checked').each(function() {
        const idMobiliario = $(this).val();
        const cantidadMobiliario = $('#quantity' + idMobiliario).val();
        
        dataMob += `${idMobiliario}:${cantidadMobiliario};`;
        // console.log(dataMob);
    });
}

// Función para agregar decoración
function agregarDecoracion() {
    $('input[name="decoracion[]"]:checked').each(function() {
        const idDecoracion = $(this).val();
        const cantidadDecoracion = $('#quantity' + idDecoracion).val();

        dataDec += `${idDecoracion}:${cantidadDecoracion};`;

        // console.log(`Decoracion seleccionado con ID ${idDecoracion}, Cantidad: ${cantidadDecoracion}`);
        // Aquí podrías ejecutar lógica adicional, como enviar estos datos al servidor para procesar la orden.
        // $.ajax({ ... });
    });
}

// Agregar alimentos
function agregarAlimentos() {
    // Obtener los elementos seleccionados
    $('input[name="alimentos[]"]:checked').each(function() {
        const idAlimento = $(this).val();
        const cantidad = $('#quantity' + idAlimento).val();

        dataAli += `${idAlimento}:${cantidad};`;

        // Realizar alguna lógica con los datos capturados
        // console.log(`Alimento seleccionado con ID ${idAlimento}, Cantidad: ${cantidad}`);

        // Aquí podrías ejecutar lógica adicional, por ejemplo, enviar estos datos al servidor para procesar la orden.
        // $.ajax({ ... });
    });
}

// Agregar otros servicios
function agregarServicios() {
    // Obtener los elementos seleccionados
    $('input[name="servicios[]"]:checked').each(function() {
        others = $(this).val();

        // Realizar alguna lógica con los datos capturados
        // console.log(`Servicio seleccionado con ID ${others}`);

        // Aquí podrías ejecutar lógica adicional, por ejemplo, enviar estos datos al servidor para procesar la orden.
        // $.ajax({ ... });
    });
}



$( document ).ready(function() {

    // Seleccion de tipo de evento
    $(document).on("click", ".typeEvent", function(){

        typeEvent = $(this).attr("id");

        console.log(typeEvent);
        
        $(document).find(".typeEvent").removeClass("active-event");

        $(this).toggleClass("active-event");

        setTimeout(function() {
            // El código que deseas ejecutar después de un retraso de 8 segundos
            $("#nav-cant-tab").click();
        }, 600);    
    });

    // Seleccion de la cantidad de personas
    $(document).on('click', '.numberPerson', function () {
        numberPerson = $(this).attr("id");

        console.log(numberPerson);

        $(document).find(".numberPerson").removeClass("active-event");

        $(this).toggleClass("active-event");

        setTimeout(function() {
            // El código que deseas ejecutar después de un retraso de 8 segundos
            $("#nav-admob-tab").click();
        }, 600);

    });

});

// Función para deshabilitar todos los botones de pestañas
function disableTabs() {
    const tabs = document.querySelectorAll('.select-tab');
    tabs.forEach(tab => {
        tab.classList.add('disabled');
    });
}
// Función para habilitar un botón de pestaña específico
function enableTab() {
    const tabs = document.querySelectorAll('.select-tab-resume');
    tabs.forEach(tab => {
        tab.classList.remove('disabled');
    });
}


function sendForm() {

    const idUser = $('#idUser').val();
    // Aquí se recopilan todos los datos

    // console.log(idUser + " " + typeEvent + " " + numberPerson + " " + dataMob + " " + dataDec + " " + dataAli + " " + others );

    
    if (typeEvent != null || numberPerson != null){

        const datosParaEnviar = {
            idUser: idUser,
            typeEvent: typeEvent,
            numberPerson: numberPerson,
            dataMob: dataMob || '',
            dataDec: dataDec || '',
            dataAli: dataAli || '',
            others: others || ''
        };


        console.log('Datos a enviar:', datosParaEnviar);

        // Enviar los datos al servidor usando AJAX
        $.ajax({
            type: 'POST',
            url: 'c_event',
            data: JSON.stringify(datosParaEnviar),  // Convertir a JSON
            contentType: 'application/json',  // Establecer Content-Type a application/json
            success: function(response) {
                console.log('Datos enviados correctamente:', response);
                disableTabs();
                enableTab();
                // ... Puedes hacer algo más con la respuesta si es necesario
            },
            error: function(error) {
                console.error('Error al enviar datos:', error);
            }
        });
    } else{
        Swal.fire({
            position: 'center',
            icon: 'error',
            title: 'Opps, ocurrió un error',
            text: 'Debes seleccionar por lo menos un tipo de evento, y la cantidad de personas',
            showConfirmButton: false,
            timer: 1500
          });
    
    }
}


$('#sendForm').on('click', function() {
    sendForm();
    setTimeout(function() {
        // El código que deseas ejecutar después de un retraso de 8 segundos
        $("#nav-resume-tab").click();
    }, 500);   
});


/*
function mostrarResumen() {
    // Desactivar el evento click temporalmente para evitar disparos repetitivos
    // $(document).off("click", "#nav-resume-tab");

    // Obtener el elemento donde se mostrará el resumen
    const resumenElement = $('#resume');
    var rTypeEvent = $('#rTypeEvent').val(typeEvent);
    console.log(rTypeEvent);

    // Limpiar el contenido previo del resumen
    // resumenElement.empty();

    // Crear una lista para agregar cada elemento seleccionado
    // const listaResumen = $('<div class="mb-3">');
    
    // Mostrar la lista en el elemento de resumen
    // resumenElement.append(listaResumen);

    // Reactivar el evento click después de realizar las operaciones
    /*$(document).on("click", "#nav-resume-tab", function(){
        mostrarResumen();
    });
}

$(document).on("click", "#nav-resume-tab", function(){
    mostrarResumen();
});*/

