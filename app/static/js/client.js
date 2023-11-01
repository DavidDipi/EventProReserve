document.addEventListener("DOMContentLoaded", function() {

    const toggleButton = document.getElementById("toggleSidebar");
    const sidebar = document.getElementById("sidebar");

    toggleButton.addEventListener("click", function () {
        // Alternar la clase 'hidden' en la barra lateral para mostrar u ocultar
        sidebar.classList.toggle("hidden");
    });

});