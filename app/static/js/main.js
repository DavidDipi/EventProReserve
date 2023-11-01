document.addEventListener("DOMContentLoaded", function() {

    // Mostrar elementos al hacer scroll
    var elementos = document.querySelectorAll(".animacion-fadeup");

    function mostrarElementos() {
        elementos.forEach(function(elemento) {
            var posicion = elemento.getBoundingClientRect().top;
            var alturaVentana = window.innerHeight;

            if (posicion < alturaVentana) {
                elemento.style.opacity = "1";
                elemento.style.transform = "translateY(0)";
            }
        });
    }

    mostrarElementos(); // Mostrar elementos iniciales en la carga
    
    
    window.addEventListener("scroll", mostrarElementos);

    const emailInput = document.getElementById('emailInput');
    const passwordInput = document.getElementById('passwordInput');
    const textInputs = document.getElementsByClassName('input-text');

    emailInput.addEventListener('input', handleInput);
    passwordInput.addEventListener('input', handleInput);
    // Agregar el evento a todos los elementos con la clase 'input-text'
    for (let i = 0; i < textInputs.length; i++) {
        textInputs[i].addEventListener('input', handleInput);
    }

    console.log(emailInput);
    console.log(passwordInput);

    function handleInput() {
        const value = this.value.trim();
        if (value !== '') {
          this.classList.add('has-value');
        } else {
          this.classList.remove('has-value');
        }
    }


  

/*
    // Cambiar color de la barra de navegación
    var nav = document.querySelector(".navbar");
    var btnLogin = document.querySelector(".btn-ingresar");

    var params = new URLSearchParams(window.location.search);
    var currentURL = window.location.href;

    if (currentURL.endsWith("index.php") || params.get("navegacion") === "inicio" ) {
        window.addEventListener("scroll", function() {
            if (window.scrollY > 50) {
                nav.classList.add("bg-warning");
                nav.classList.remove("bg-transparent");
                btnLogin.classList.add("btn-outline-dark");
                btnLogin.classList.remove("btn-warning");

            } else {
                nav.classList.remove("bg-warning");
                nav.classList.add("bg-transparent");
                btnLogin.classList.remove("btn-outline-dark");
                btnLogin.classList.add("btn-warning");
            }
        });
    } else {
        nav.classList.add("bg-warning");
        nav.classList.remove("bg-transparent", "fixed-top");
    }*/

    
});
