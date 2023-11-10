$( document ).ready(function() {

    // Definir variables
    let typeEvent, numberPerson, adMob, adDec, adAli, others;

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
        /*
        if ($(this).class("active-event")){
            $(this).removeClass("active-event")
        }else {
            $(this).addClass("active-event")
        }*/       
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