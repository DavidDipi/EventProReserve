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