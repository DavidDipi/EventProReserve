document.addEventListener("DOMContentLoaded", function() {

    const toggleButton = document.getElementById("toggleSidebar");
    const sidebar = document.getElementById("sidebar");
    const content = document.getElementById("content");
    const iconBtn = document.getElementById("btnIcon");


    toggleButton.addEventListener("click", function () {
        // Alternar la clase 'hidden' en la barra lateral para mostrar u ocultar
        sidebar.classList.toggle("hidden");
        // Expandir contenido
        content.classList.toggle("expand");

        if (iconBtn.classList.contains("bxs-arrow-to-left")){
            iconBtn.classList.remove("bxs-arrow-to-left");
            iconBtn.classList.add("bxs-arrow-to-right");
        }else if(iconBtn.classList.contains("bxs-arrow-to-right")){
            iconBtn.classList.add("bxs-arrow-to-left");
            iconBtn.classList.remove("bxs-arrow-to-right");
        }

    });

});

$(document).ready(function() {
   

        //-- funcion para los eventos
        $.ajax({
            url: 'get_event',
            type: 'POST',
            success: function(response) {
                
                console.log(response.events)

                // Inicializa DataTable
                var tabla = $('#evento').DataTable({
                    "dom": 'Bfrtip',
                    "data":response.events,
                    "buttons": [
                        'pdf',
                        {
                            extend: 'excel',
                            title: 'Nombre_del_archivo',
                            exportOptions: {
                                columns: [1, 2,3]
                            },
                        },
                        
                      
                    ],
                    "columns": [
                        {"data": "id"},
                        {"data": "Nombre"},
                        {"data": "Descripción"},
                        {"data": "Estado"},
                        {
                            "data": null,
                            "defaultContent": ' <button type="button" class="btn editar btn-warning" style="margin-left: 4%;margin-right: 9%;">EDITAR<i class="fa-solid fa-pen-to-square"></i></button><button type="submit" class="btn borrar btn-danger">BORRAR<i class="fa-regular fa-trash-can"></i></button>'
                        }
                    ],
                    "language": {
                        "url": "//cdn.datatables.net/plug-ins/1.10.15/i18n/Spanish.json"
                    },
                });

                // Asigna funcionalidad a los botones (Editar y Borrar)
                $('#evento').on('click', 'button.editar', function () {
                    var data = tabla.row($(this).parents('tr')).data();
                    $("#modalEditar .modal-body #formulario_edicion_eventos").empty();
                    $.each(data,function(index, elemento) {
                        console.log(elemento);
                      
                        if(index=='Estado'){
                            $("#modalEditar .modal-body #formulario_edicion_eventos").append('<label for="'+index+'">'+index+':</label> <select class="form-select" aria-label="Default select" name="state" id="miSelect"> <option value="1">ACTIVO</option>  <option value="2">INACTIVO</option>  </select>')
                        }else if(index =="id"){
                            $("#modalEditar .modal-body #formulario_edicion_eventos").append('<input type="hidden" value="'+elemento+'" name="editTypeEvent">');
                        }
                        else if(index =="Descripción"){
                            console.log(elemento)
                            $("#modalEditar .modal-body #formulario_edicion_eventos").append('<label for="' + index + '">' + index + ':</label><label class="form-control" name="descriptionTypeEvent" id="' + index + '">' + elemento + '</label>');


                        }
                        else if(index =="Nombre"){
                            $("#modalEditar .modal-body #formulario_edicion_eventos").append('<label for="'+index+'">'+index+':</label>   <input  name= "nameTypeEvent" type="text" id="'+index+'" class="form-control" value="'+elemento+'">');
                        }

                     

                      
                      });
                      $("#modalEditar").modal('show');            
                      $("#modalEditar .modal-body #formulario_edicion_eventos").append('<br> <button class="w-50 btn btn-outline-success">Guardar</button>')
                     
                });

                $('#evento').on('click', 'button.borrar', function () {
                    var fila = tabla.row($(this).parents('tr')).data();
                    var id = fila.id;
                   console.log(id);
                    $("#modalEditar .modal-body #borrar_evento").append('<input type="hidden" value="'+id+'" name="deleteRecord">           <button id="borrar_evento_btn" type="submit" class="btn btn-danger">    BORRAR<i class="fa-regular fa-trash-can"></i></button>')
                  
                    $("#borrar_evento_btn").click();

                });
               
            },
            error: function(error) {
                console.log(error);
            }
        });

        //--- funcion  para cantidad de personas
        $.ajax({
            url: 'get_personas',
            type: 'POST',
            success: function(response) {
                
                console.log(response.pers)

                // Inicializa DataTable
                var tabla = $('#personas').DataTable({
                    "data":response.pers,
                    "columns": [
                        {"data": "id"},
                        {"data": "Cantidad"},
                        {"data": "Costo"},
                        {"data": "Estado"},
                        {
                            "data": null,
                            "defaultContent": ' <button type="button" class="btn editar btn-warning" style="margin-left: 4%;margin-right: 9%;">EDITAR<i class="fa-solid fa-pen-to-square"></i></button><button type="submit" class="btn borrar btn-danger">BORRAR<i class="fa-regular fa-trash-can"></i></button>'
                        }
                    ]
                });

                // Asigna funcionalidad a los botones (Editar y Borrar)
                $('#personas').on('click', 'button.editar', function () {
                    var data = tabla.row($(this).parents('tr')).data();
                    $("#modalEditar .modal-body #form_personas").empty();
                    $.each(data,function(index, elemento) {
                        
                        console.log(index);
                        if(index=='Estado'){
                            

                            $("#modalEditar .modal-body #form_personas").append('<label for="'+index+'">'+index+':</label> <select class="form-select" aria-label="Default select" name="state" id="miSelect"> <option value="1">ACTIVO</option>  <option value="2">INACTIVO</option>  </select>')
                        }else if(index =="id"){

                            $("#modalEditar .modal-body #form_personas").append('<input type="hidden" value="'+elemento+'" name="editCantPers">');
                        }
                        else if(index =="Cantidad"){

                            $("#modalEditar .modal-body #form_personas").append('<label for="'+index+'">'+index+':</label>   <input name= "AmountPe" type="text" id="'+index+'" class="form-control" value="'+elemento+'">');
                        }
                        else if(index =="Costo"){

                            $("#modalEditar .modal-body #form_personas").append('<label for="'+index+'">'+index+':</label>   <input  name= "costAmountPe" type="text" id="'+index+'" class="form-control" value="'+elemento+'">');
                        }

                    

                    
                    });
                    $("#modalEditar").modal('show');            
                    $("#modalEditar .modal-body #form_personas").append('<br> <button class="w-50 btn btn-outline-success">Guardar</button>')
                    
                });

                $('#personas').on('click', 'button.borrar', function () {
                    var fila = tabla.row($(this).parents('tr')).data();
                    var id = fila.id;
                console.log(id);
                    $("#modalEditar .modal-body #form_personas_eliminar").append('<input type="hidden" value="'+id+'" name="deleteRecord">           <button id="borrar_personas_btn" type="submit" class="btn btn-danger">    BORRAR<i class="fa-regular fa-trash-can"></i></button>')
                
                    $("#borrar_personas_btn").click();

                });
            
            },
            error: function(error) {
                console.log(error);
            }
        });

        //-- Mobiliario adicional
        $.ajax({
            url: 'get_mobiliario',
            type: 'POST',
            success: function(response) {
                
                console.log(response.adMobs)

                 // Inicializa DataTable
                var tabla = $('#mobiliario').DataTable({
                    "data":response.adMobs,
                    "columns": [
                        {"data": "id"},
                        {"data": "Nombre"},
                        {"data": "Costo"},
                        {"data": "Estado"},
                        {
                            "data": null,
                            "defaultContent": ' <button type="button" class="btn editar btn-warning" style="margin-left: 4%;margin-right: 9%;">EDITAR<i class="fa-solid fa-pen-to-square"></i></button><button type="submit" class="btn borrar btn-danger">BORRAR<i class="fa-regular fa-trash-can"></i></button>'
                        }
                    ]
                });
  
                // Asigna funcionalidad a los botones (Editar y Borrar)
                $('#mobiliario').on('click', 'button.editar', function () {
                    var data = tabla.row($(this).parents('tr')).data();
                    $("#modalEditar .modal-body #editar_adMob").empty();
                    $.each(data,function(index, elemento) {
                        
                      
                        if(index=='Estado'){
                            

                            $("#modalEditar .modal-body #editar_adMob").append('<label for="'+index+'">'+index+':</label> <select class="form-select" aria-label="Default select" name="state" id="miSelect"> <option value="1">ACTIVO</option>  <option value="2">INACTIVO</option>  </select>')
                        }else if(index =="id"){

                            $("#modalEditar .modal-body #editar_adMob").append('<input type="hidden" value="'+elemento+'" name="editAdMob">');
                        }
                        else if(index =="Costo"){

                            $("#modalEditar .modal-body #editar_adMob").append('<label for="'+index+'">'+index+':</label> <input name="costAdMob" type="number" id="'+index+'" class="form-control" value="'+elemento+'">');
                        }
                        else if(index =="Nombre"){

                            $("#modalEditar .modal-body #editar_adMob").append('<label for="'+index+'">'+index+':</label>   <input  name="nameAdMob" type="text" id="'+index+'" class="form-control" value="'+elemento+'">');
                        }

                     

                      
                      });
                      $("#modalEditar").modal('show');            
                      $("#modalEditar .modal-body #editar_adMob").append('<br> <button class="w-50 btn btn-outline-success">Guardar</button>')
                     
                });

                $('#mobiliario').on('click', 'button.borrar', function () {
                    var fila = tabla.row($(this).parents('tr')).data();
                    var id = fila.id;
                   console.log(id);
                    $("#modalEditar .modal-body #borrar_adMob").append('<input type="hidden" value="'+id+'" name="deleteRecord">           <button id="borrar_adMob_btn" type="submit" class="btn btn-danger">    BORRAR<i class="fa-regular fa-trash-can"></i></button>')
                  
                    $("#borrar_adMob_btn").click();

                });
               
            },
            error: function(error) {
                console.log(error);
            }
        });

        //-- decoracion adicional
        $.ajax({
            url: 'get_additional_dec',
            type: 'POST',
            success: function(response) {
                console.log(response.additional_dec);

                var tablaDecoracion = $('#decoracion').DataTable({
                    "data": response.additional_dec,
                    "columns": [
                        {"data": "id"},
                        {"data": "Nombre"},
                        {"data": "Costo"},
                        {"data": "Estado"},
                        {
                            "data": null,
                            "defaultContent": '<button type="button" class="btn editar btn-warning" style="margin-left: 4%;margin-right: 9%;">EDITAR<i class="fa-solid fa-pen-to-square"></i></button><button type="submit" class="btn borrar btn-danger">BORRAR<i class="fa-regular fa-trash-can"></i></button>'
                        }
                    ]
                });

                $('#decoracion').on('click', 'button.editar', function () {
                    var data = tablaDecoracion.row($(this).parents('tr')).data();
                    $("#modalEditar .modal-body #form_decoracion").empty();
                    $.each(data,function(index, elemento) {
                        
                        if(index=='Estado'){
                            $("#modalEditar .modal-body #form_decoracion").append('<label for="'+index+'">'+index+':</label> <select class="form-select" aria-label="Default select" name="state" id="miSelect"> <option value="1">ACTIVO</option>  <option value="2">INACTIVO</option>  </select>')
                        }else if(index =="id"){

                            $("#modalEditar .modal-body #form_decoracion").append('<input type="hidden" value="'+elemento+'" name="editAdDec">');
                        }
                        else if(index =="Costo"){

                            $("#modalEditar .modal-body #form_decoracion").append('<label for="'+index+'">'+index+':</label> <input name="costAdDec" type="number" id="'+index+'" class="form-control" value="'+elemento+'">');
                        }
                        else if(index =="Nombre"){

                            $("#modalEditar .modal-body #form_decoracion").append('<label for="'+index+'">'+index+':</label>   <input  name="nameAdDec" type="text" id="'+index+'" class="form-control" value="'+elemento+'">');
                        }

                    

                    
                    });
                    $("#modalEditar").modal('show');            
                    $("#modalEditar .modal-body #form_decoracion").append('<br> <button class="w-50 btn btn-outline-success">Guardar</button>')
                });

                $('#decoracion').on('click', 'button.borrar', function () {
                    var fila = tablaDecoracion.row($(this).parents('tr')).data();
                    var id = fila.id;
                    console.log(id);
                    $("#modalEditar .modal-body #borrar_adDec").append('<input type="hidden" value="'+id+'" name="deleteRecord">           <button id="borrar_adDec_btn" type="submit" class="btn btn-danger">    BORRAR<i class="fa-regular fa-trash-can"></i></button>')
                  
                    $("#borrar_adDec_btn").click();
                });
            },
            error: function(error) {
                console.log(error);
            }
        });

        //-- Alimentos adicionales
        $.ajax({
            url: 'get_additional_ali',
            type: 'POST',
            success: function(response) {
                console.log(response.additional_ali);

                var tablaAlimentos = $('#alimentos').DataTable({
                    "data": response.additional_ali,
                    "columns": [
                        {"data": "id"},
                        {"data": "Nombre"},
                        {"data": "Costo"},
                        {"data": "Estado"},
                        {
                            "data": null,
                            "defaultContent": '<button type="button" class="btn editar btn-warning" style="margin-left: 4%;margin-right: 9%;">EDITAR<i class="fa-solid fa-pen-to-square"></i></button><button type="submit" class="btn borrar btn-danger">BORRAR<i class="fa-regular fa-trash-can"></i></button>'
                        }
                    ]
                });

                $('#alimentos').on('click', 'button.editar', function () {
                    var data = tablaAlimentos.row($(this).parents('tr')).data();
                    $("#modalEditar .modal-body #editar_adAli").empty();
                    $.each(data,function(index, elemento) {
                        
                        if(index=='Estado'){
                            $("#modalEditar .modal-body #editar_adAli").append('<label for="'+index+'">'+index+':</label> <select class="form-select" aria-label="Default select" name="state" id="miSelect"> <option value="1">ACTIVO</option>  <option value="2">INACTIVO</option>  </select>')
                        }else if(index =="id"){

                            $("#modalEditar .modal-body #editar_adAli").append('<input type="hidden" value="'+elemento+'" name="editAdAli">');
                        }
                        else if(index =="Costo"){

                            $("#modalEditar .modal-body #editar_adAli").append('<label for="'+index+'">'+index+':</label> <input name="costAdAli" type="number" id="'+index+'" class="form-control" value="'+elemento+'">');
                        }
                        else if(index =="Nombre"){

                            $("#modalEditar .modal-body #editar_adAli").append('<label for="'+index+'">'+index+':</label>   <input  name="nameAdAli" type="text" id="'+index+'" class="form-control" value="'+elemento+'">');
                        }

                    
                        $("#modalEditar").modal('show');            
                        $("#modalEditar .modal-body #editar_adAli").append('<br> <button class="w-50 btn btn-outline-success">Guardar</button>')
                    
                    });
                });

                $('#alimentos').on('click', 'button.borrar', function () {
                    var fila = tablaAlimentos.row($(this).parents('tr')).data();
                    var id = fila.id;
                    console.log(id);
                    // Resto del código para borrar
                });
            },
            error: function(error) {
                console.log(error);
            }
        });



        //--- otros servicios
        $.ajax({
            url: 'get_others_serv',
            type: 'POST',
            success: function(response) {
                
                console.log(response.events)

                 // Inicializa DataTable
                var tabla = $('#evento').DataTable({
                    "data":response.events,
                    "columns": [
                        {"data": "id"},
                        {"data": "Nombre"},
                        {"data": "Descripción"},
                        {"data": "Estado"},
                        {
                            "data": null,
                            "defaultContent": ' <button type="button" class="btn editar btn-warning" style="margin-left: 4%;margin-right: 9%;">EDITAR<i class="fa-solid fa-pen-to-square"></i></button><button type="submit" class="btn borrar btn-danger">BORRAR<i class="fa-regular fa-trash-can"></i></button>'
                        }
                    ]
                });

                        // Asigna funcionalidad a los botones (Editar y Borrar)
                $('#evento').on('click', 'button.editar', function () {
                    var data = tabla.row($(this).parents('tr')).data();
                    $("#modalEditar .modal-body #formulario_edicion_eventos").empty();
                    $.each(data,function(index, elemento) {
                        
                      
                        if(index=='Estado'){
                            

                            $("#modalEditar .modal-body #formulario_edicion_eventos").append('<label for="'+index+'">'+index+':</label> <select class="form-select" aria-label="Default select" name="state" id="miSelect"> <option value="1">ACTIVO</option>  <option value="2">INACTIVO</option>  </select>')
                        }else if(index =="id"){

                            $("#modalEditar .modal-body #formulario_edicion_eventos").append('<input type="hidden" value="'+elemento+'" name="editTypeEvent">');
                        }
                        else if(index =="Descripción"){

                            $("#modalEditar .modal-body #formulario_edicion_eventos").append('<label for="'+index+'">'+index+':</label>   <textarea name= "descriptionTypeEvent" type="text" id="'+index+'" class="form-control" value="'+elemento+'">');
                        }
                        else if(index =="Nombre"){

                            $("#modalEditar .modal-body #formulario_edicion_eventos").append('<label for="'+index+'">'+index+':</label>   <input  name= "nameTypeEvent" type="text" id="'+index+'" class="form-control" value="'+elemento+'">');
                        }

                     

                      
                      });
                      $("#modalEditar").modal('show');            
                      $("#modalEditar .modal-body #formulario_edicion_eventos").append('<br> <button class="w-50 btn btn-outline-success">Guardar</button>')
                     
                });

                $('#evento').on('click', 'button.borrar', function () {
                    var fila = tabla.row($(this).parents('tr')).data();
                    var id = fila.id;
                   console.log(id);
                    $("#modalEditar .modal-body #borrar_evento").append('<input type="hidden" value="'+id+'" name="deleteRecord">           <button id="borrar_evento_btn" type="submit" class="btn btn-danger">    BORRAR<i class="fa-regular fa-trash-can"></i></button>')
                  
                    $("#borrar_evento_btn").click();

                });
               
            },
            error: function(error) {
                console.log(error);
            }
        });
    
});

