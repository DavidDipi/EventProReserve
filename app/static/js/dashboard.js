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
                var tabla = $('#miTabla').DataTable({
                    "data":response.events,
                    "columns": [
                        {"data": "id"},
                        {"data": "name"},
                        {"data": "descrip"},
                        {"data": "estado"},
                        {
                            "data": "id",
                            "defaultContent": ' <button type="button" class="btn editar btn-warning" data-bs-toggle="modal" data-bs-target="#editAdMob">EDITAR<i class="fa-solid fa-pen-to-square"></i></button><button type="submit" class="btn btn-danger">BORRAR<i class="fa-regular fa-trash-can"></i></button>'
                        }
                    ]
                });

               
            },
            error: function(error) {
                console.log(error);
            }
        });

        $('#miTabla tbody').on('click', 'button.editar', function () {
            // Obtén la fila actual
            var fila = tabla.row($(this).parents('tr')).data();
            
            // Extrae el ID de la fila
            var id = fila.id;
    
            // Ahora puedes utilizar el ID como desees (por ejemplo, pasarlo a una función de edición)
            console.log('ID a editar:', id);
            // Llama a una función de edición pasando el ID
            editarRegistro(id);
        });
    
        function editarRegistro(id) {
            // Lógica para editar el registro con el ID proporcionado
            // Puedes implementar aquí la lógica que desees
            console.log('Editar registro con ID:', id);
        }
    
    
});