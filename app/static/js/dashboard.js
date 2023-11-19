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
   
        $.ajax({
            url: 'get_event',
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
                            "defaultContent": ' <button type="button" class="btn editar btn-warning" style="margin-left: 4%;margin-right: 9%;">EDITAR<i class="fa-solid fa-pen-to-square"></i></button><button type="submit" class="btn btn-danger">BORRAR<i class="fa-regular fa-trash-can"></i></button>'
                        }
                    ]
                });

                        // Asigna funcionalidad a los botones (Editar y Borrar)
                $('#evento').on('click', 'button.editar', function () {
                    var data = tabla.row($(this).parents('tr')).data();
                    $("#modalEditar .modal-body #formulario_edicion_eventos").empty();
                    $.each(data,function(index, elemento) {
                        
                      
                        if(index=='Estado'){
                            

                            $("#modalEditar .modal-body #formulario_edicion_eventos").append('<label for="'+index+'">'+index+':</label> <select class="form-select" aria-label="Default select" name="state" id="miSelect"> <option >ACTIVO</option>  <option>INACTIVO</option>  </select>')
                        }else if(index =="id"){

                            $("#modalEditar .modal-body #formulario_edicion_eventos").append('<input type="hidden" value="'+index+'" name="editTypeEvent">');
                        }
                        else if(index =="Descripción"){

                            $("#modalEditar .modal-body #formulario_edicion_eventos").append('<label for="'+index+'">'+index+':</label>   <input name= "descriptionTypeEvent" type="text" id="'+index+'" class="form-control" value="'+elemento+'">');
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
                    borrarRegistro(id);
                    tabla.ajax.reload();
                });
               
            },
            error: function(error) {
                console.log(error);
            }
        });

    
    
    
});