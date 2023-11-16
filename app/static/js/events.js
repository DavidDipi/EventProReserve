// Definir variables
let typeEvent, numberPerson, adMob, adDec, adAli, others;

// Función para agregar mobiliario
function agregarMobiliario() {
    $('input[name="mobiliario[]"]:checked').each(function() {
        const idMobiliario = $(this).val();
        const cantidadMobiliario = $('#quantity' + idMobiliario).val();
        console.log(`Mobiliario seleccionado con ID ${idMobiliario}, Cantidad: ${cantidadMobiliario}`);
        // Aquí podrías ejecutar lógica adicional, como enviar estos datos al servidor para procesar la orden.
        // $.ajax({ ... });
    });
}

// Función para agregar decoración
function agregarDecoracion() {
    $('input[name="decoracion[]"]:checked').each(function() {
        const idDecoracion = $(this).val();
        const cantidadDecoracion = $('#quantity' + idDecoracion).val();
        console.log(`Decoracion seleccionado con ID ${idDecoracion}, Cantidad: ${cantidadDecoracion}`);
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

        // Realizar alguna lógica con los datos capturados
        console.log(`Alimento seleccionado con ID ${idAlimento}, Cantidad: ${cantidad}`);

        // Aquí podrías ejecutar lógica adicional, por ejemplo, enviar estos datos al servidor para procesar la orden.
        // $.ajax({ ... });
    });
}

// Agregar otros servicios
function agregarServicios() {
    // Obtener los elementos seleccionados
    $('input[name="servicios[]"]:checked').each(function() {
        const idServicio = $(this).val();

        // Realizar alguna lógica con los datos capturados
        console.log(`Servicio seleccionado con ID ${idServicio}`);

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

function mostrarResumen() {
    // Desactivar el evento click temporalmente para evitar disparos repetitivos
    // $(document).off("click", "#nav-resume-tab");

    // Obtener el elemento donde se mostrará el resumen
    const resumenElement = $('#resume');

    // Limpiar el contenido previo del resumen
    resumenElement.empty();

    // Crear una lista para agregar cada elemento seleccionado
    const listaResumen = $('<div class="mb-3">');

    // Agregar cada elemento seleccionado a la lista
    if (typeEvent) {
        listaResumen.append(`<input class="form-control" type="text" value="${typeEvent}" aria-label="readonly" readonly> `);
    }
    if (numberPerson) {
        listaResumen.append(`<input class="form-control" type="text" value="${numberPerson}" aria-label="readonly" readonly>  `);
    }
    // Agregar aquí las selecciones de mobiliario, decoración, alimentos, y otros servicios
    
    // Mostrar la lista en el elemento de resumen
    resumenElement.append(listaResumen);

    // Reactivar el evento click después de realizar las operaciones
    /*$(document).on("click", "#nav-resume-tab", function(){
        mostrarResumen();
    });*/
}

$(document).on("click", "#nav-resume-tab", function(){
    mostrarResumen();
});

