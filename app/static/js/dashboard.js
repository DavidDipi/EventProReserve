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
                        {"data": "name"},
                        {"data": "descrip"},
                        {"data": "estado"},
                        {
                            "data": null,
                            "defaultContent": ' <button type="button" class="btn editar btn-warning" data-bs-toggle="modal" data-bs-target="#editAdMob" style="margin-left: 4%;margin-right: 9%;">EDITAR<i class="fa-solid fa-pen-to-square"></i></button><button type="submit" class="btn btn-danger">BORRAR<i class="fa-regular fa-trash-can"></i></button>'
                        }
                    ]
                });

                        // Asigna funcionalidad a los botones (Editar y Borrar)
                $('#evento').on('click', 'button.editar', function () {
                    var data = tabla.row($(this).parents('tr')).data();

                    $("#modalEditar .modal-body").append()
                    // Implementa la lógica para editar utilizando 'data'
                    console.log('Editar:', data);

                    tabla.ajax.reload();

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