


// Definir variables
let typeEvent, numberPerson, adMob, adDec, adAli, others, dataMob, dataDec, dataAli, dataOtServ, dateSelect;

dataMob = '';
dataDec = '';
dataAli = '';
dataOtServ = '';
dateSelect = '';

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

function enableEdit(selectId) {
    // Obtén el elemento select por su ID
    var selectElement = document.getElementById(selectId);
    selectElement.disabled = !selectElement.disabled;

}



$( document ).ready(function() {

    // Seleccion de tipo de evento
    $(document).on("click", ".typeEvent", function(){

        typeEvent = $(this).attr("id");

        console.log(typeEvent);
        
        $(document).find(".typeEvent").removeClass("active-event");
        $(document).find(".card-events-front").removeClass("select");
        $(document).find(".card-events-back").removeClass("select");

        $(this).toggleClass("active-event");
        $(document).find(".card-events-front").addClass("select");
        $(document).find(".card-events-back").addClass("select");


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
        tab.classList.add('bg-body-secondary')
    });
}
// Función para habilitar un botón de pestaña específico
function enableTab() {
    const tabs = document.querySelectorAll('.select-tab-resume');
    tabs.forEach(tab => {
        tab.classList.remove('disabled');
        tab.classList.remove('bg-body-secondary')
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



document.addEventListener('DOMContentLoaded', function() {
    var today = new Date().toISOString().slice(0, 10);
    var blockedDates = [];
    var maxSelectableDate = new Date();
    maxSelectableDate.setDate(maxSelectableDate.getDate() + 15);
    var dateNotAvailable = [];

    $.ajax({
        type: 'POST',
        url: 'get_date',  // Actualiza la URL según tu configuración
        success: function(response) {
            var dateEvents = response.dateEvent;
            dateNotAvailable = dateEvents.map(fecha => fecha.value);
            // Ahora dateNotAvailable contiene las fechas en formato 'YYYY-MM-DD'

            // Agregar fechas de dateNotAvailable a blockedDates
            blockedDates = blockedDates.concat(dateNotAvailable);

            // Crear un array de fechas bloqueadas (hasta 15 días desde hoy)
            for (var i = 0; i <= 15; i++) {
                var blockedDate = new Date();
                blockedDate.setDate(blockedDate.getDate() + i);
                blockedDates.push(blockedDate.toISOString().slice(0, 10));
            }
            // Verificar y eliminar duplicados si es necesario
            blockedDates = [...new Set(blockedDates)];

            var events = blockedDates.map(function(date) {
                return {
                    title: 'No disponible',
                    start: date,
                    display: 'background',
                    color: '#ff9f89',
                    editable: false 
                };
            });

            var calendarEl = document.getElementById('calendar');
            var calendar = new FullCalendar.Calendar(calendarEl, {
                initialView: 'dayGridMonth',
                selectable: true,
                events: events,
                select: function(info) {
                    var selectedDate = info.startStr;
                    var dataDateElement = document.querySelector('.dataDate');
                    if (!blockedDates.includes(selectedDate)) {
                        dateSelect = selectedDate;
                    } else {
                        alert('Selecciona una fecha posterior a los próximos 15 días.');
                    }
                },
            });

            calendar.render();
        },
        error: function(error) {
            console.error('Error al obtener fechas:', error);
        }
    });
});



$(document).ready(function() {
    $('#myForm').on('submit', function(event) {
        event.preventDefault(); // Evitar el comportamiento predeterminado del formulario (recarga de la página)

        const idUser = $('#idUser').val();
        const eventId = $('#eventId').val();
        typeEvent = $('#typeEvent').val();
        numberPerson = $('#cantPers').val();
        others = $('#ots').val();

        console.log(typeEvent)
        console.log(numberPerson)
        console.log(others)
        // Crear objeto con datos a enviar
        const datosParaEnviar = {
            idUser: idUser,
            typeEvent: typeEvent,
            numberPerson: numberPerson,
            dataMob: dataMob,
            dataDec: dataDec,
            dataAli: dataAli,
            others: others,
            eventId: eventId,
            dateSelect: dateSelect
        };

        // Realizar la solicitud AJAX
        $.ajax({
            type: 'POST',
            url: 'e_event/' + eventId,
            data: datosParaEnviar,
            success: function(response) {
                console.log('Datos actualizados correctamente:', response);
                // Haz algo con la respuesta si es necesario

              
                // Muestra la alerta de éxito
                Swal.fire({
                  position: 'top-end',
                  icon: 'success',
                  title: 'Cotización realizada con exito',
                  showConfirmButton: false,
                  timer: 1500
                });
              
                
            },
            error: function(error) {
                console.error('Error al actualizar datos:', error);
            }
        });
    });
});

$('#sendForm').on('click', function() {
    // sendForm();
    setTimeout(function() {
        // El código que deseas ejecutar después de un retraso de 8 segundos
        $("#nav-resume-tab").click();
    }, 500);   
});

$('#editEvent').on('click', function() {
    setTimeout(function() {
        // El código que deseas ejecutar después de un retraso de 8 segundos
        // $("#nav-resume-tab").click();
    }, 500);   
});