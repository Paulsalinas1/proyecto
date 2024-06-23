$("#correo").after("<div id='mensajeErrorCorreoCrear'></div>");
$("#Rut").after("<div id='mensajeErrorRut'></div>");
$("#contraseña").after("<div id='mensajeErrorContraseña'></div>");
$("#repetirContraseña").after("<div id='mensajeErrorRepetirContraseña'></div>");
$("#nombre").after("<div id='mensajeErrorNombre'></div>");
$("#apellido").after("<div id='mensajeErrorApellido'></div>");
$("#fono2").after("<div id='mensajeErrorTelefono'></div>");
$("#comuna").after("<div id='mensajeErrorComuna'></div>");
$("#direc").after("<div id='mensajeErrorDirec'></div>");


$("#correo").on("input", validarCorreoCrear);
$("#contraseña").on("input", contra_1);
$("#repetirContraseña").on("input", contra_2);
$("#nombre").on("input", nombre_v);
$("#apellido").on("input", apellido_v);
$("#comuna").on("input", comuna);
$("#direc").on("input", direc);
$("#fono").on("input", telefono);

$("#Rut").on("input", function () {
    formatRut();
    validaRut();
});

$("#fono").on("keypress", function (event) {
    return soloNumeros(event);
});



function validarCorreoCrear() {
    var coreoinp = document.getElementById("correo");
    var correo = document.getElementById("correo").value;
    var mensajeError = document.getElementById("mensajeErrorCorreoCrear");

    if (correo === "") {
        mensajeError.innerText = "Por favor, ingrese su correo.";
        mensajeError.style.color = "red";
        coreoinp.setCustomValidity("no valido");
        return false; // Evita que se envíe el formulario si el correo está vacío
    }else if (correo.includes("@trabajador.com")) {
        mensajeError.innerText = "Correo electrónico de trabajador válido ✅";
        mensajeError.style.color = "green";
        coreoinp.setCustomValidity("");
        return true; // Envía el formulario si el correo contiene "@trabajador.com"
    }else if (correo.includes("@gmail.com") || correo.includes("@hotmail.com")) {
        mensajeError.innerText = "Correo electrónico válido ✅";
        mensajeError.style.color = "green"; 
        coreoinp.setCustomValidity("");
        return true; // correo valido
    }else if (correo.includes("@gmail.cl") || correo.includes("@hotmail.cl")) {
        mensajeError.innerText = "Correo electrónico válido ✅";
        mensajeError.style.color = "green"; 
        coreoinp.setCustomValidity("");
        return true; // correo valido
    }else {
        mensajeError.innerText = "Ingrese un correo válido.";
        mensajeError.style.color = "red";
        coreoinp.setCustomValidity("no valido");
        return false; // Evita que se envíe el formulario si el correo no contiene "@gmail o @hotmail .com o .cl" 
    }
}
// Valida el rut con su cadena completa "XXXXXXXX-X"
function validaRut() {
    var rutinp = document.getElementById("Rut");
    var rutCompleto = document.getElementById("Rut").value;
    var mensajeError = document.getElementById("mensajeErrorRut");

    if (rutCompleto === "") {
        mensajeError.innerText = "Por favor, ingrese su run ";
        mensajeError.style.color = "red";
        rutinp.setCustomValidity("no");
        return false;
    }else if (/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rutCompleto)){
        var tmp = rutCompleto.split('-');
        var digv = tmp[1];
        var rut = tmp[0];
        if (digv == 'K') {
            digv = 'k';
        }
        
        if (dv(rut) == digv){
            mensajeError.innerText = "Run válido ✅";
            mensajeError.style.color = "green";
            rutinp.setCustomValidity("");
            return true;
        }else {
            mensajeError.innerText = "Por favor, ingrese un run válido ";
            mensajeError.style.color = "red";
            rutinp.setCustomValidity("no");
            return false;
        }    
    }else {
        mensajeError.innerText = "Por favor, ingrese un run válido ";
        mensajeError.style.color = "red";
        rutinp.setCustomValidity("no");
        return false;
    }   
}
function dv(T) {
    var M = 0, S = 1;
    for (; T; T = Math.floor(T / 10))
        S = (S + T % 10 * (9 - M++ % 6)) % 11;
    return S ? S - 1 : 'k';
}
function formatRut() {
    let rutInput = document.getElementById("Rut");
    let rut = rutInput.value.replace(/[^\dkK]/g, ''); // Elimina cualquier caracter que no sea un dígito o 'k' (mayúscula o minúscula)
    rut = rut.replace(/^0+/, ''); // Elimina ceros a la izquierda
    
    let formattedRut = '';
    let rutLength = rut.length;
    
    if (rutLength > 1) {
        for (let i = 0; i < rutLength - 1; i++) {
            formattedRut += rut.charAt(i);
            if (i === rutLength - 2) {
                formattedRut += '-';
            }
        }
        formattedRut += rut.charAt(rutLength - 1);
    } else {
        formattedRut = rut;
    }
    
    rutInput.value = formattedRut;
}
function contra_1() {
    var coninp = document.getElementById("contraseña");
    var contraseña = document.getElementById("contraseña").value;
    var mensajeError = document.getElementById("mensajeErrorContraseña");

    if (contraseña === "") {
        mensajeError.innerText = "Por favor, ingrese una contraseña";
        mensajeError.style.color = "red";
        coninp.setCustomValidity("no");
        return false;// Evita que se envíe el formulario si la contraseña está vacía
    } else if (contraseña.length < 6) {
        mensajeError.innerText = "La contraseña debe tener al menos 6 caracteres";
        mensajeError.style.color = "red";
        coninp.setCustomValidity("no");
        return false;// Evita que se envíe el formulario si la contraseña tiene menos de 6 caracteres
    } else {
        mensajeError.innerText = "Contraseña ingresada ✅";
        mensajeError.style.color = "green";
        coninp.setCustomValidity("");
        return true;
    }
}
function contra_2() {
    var con2inp = document.getElementById("repetirContraseña");
    var contraseña = document.getElementById("contraseña").value;
    var repetirContraseña = document.getElementById("repetirContraseña").value; // Obtener el valor del campo de repetir contraseña
    var mensajeError = document.getElementById("mensajeErrorRepetirContraseña");

    if (contraseña === "") {
        mensajeError.innerText = "Por favor, ingrese una contraseña";
        mensajeError.style.color = "red";
        con2inp.setCustomValidity("no");
        return false;
    } else if (contraseña.length < 6) {
        mensajeError.innerText = "La contraseña debe tener al menos 6 caracteres";
        mensajeError.style.color = "red";
        con2inp.setCustomValidity("no");
        return false;// Evita que se envíe el formulario si la contraseña tiene menos de 6 caracteres
    }else if (repetirContraseña !== contraseña) {
        mensajeError.innerText = "Las contraseñas no coinciden.";
        mensajeError.style.color = "red";
        con2inp.setCustomValidity("no");
        return false;
    } else {
        mensajeError.innerText = "Contraseñas iguales ✅";
        mensajeError.style.color = "green";
        con2inp.setCustomValidity("");
        return true;
    }
    
}
function nombre_v() {
    var nombinp = document.getElementById("nombre");
    var nombre = document.getElementById("nombre").value;
    var mensajeError = document.getElementById("mensajeErrorNombre");

    if (nombre === "") {
        mensajeError.innerText = "Por favor, ingrese su nombre.";
        mensajeError.style.color = "red";
        nombinp.setCustomValidity("no");
        return false; // Evita que se envíe el formulario si el nombre está vacío
    } else {
        mensajeError.innerText = "Nombre correcto ✅";
        mensajeError.style.color = "green";
        nombinp.setCustomValidity("");
        return true;
    }
}
function apellido_v() {
    var apeinp = document.getElementById("apellido");
    var apellido = document.getElementById("apellido").value;
    var mensajeError = document.getElementById("mensajeErrorApellido");

    if (apellido === "") {
        mensajeError.innerText = "Por favor, ingrese su apellido.";
        mensajeError.style.color = "red";
        apeinp.setCustomValidity("no");
        return false; // Evita que se envíe el formulario si el apellido está vacío
    } else {
        mensajeError.innerText = "Apellido correcto ✅";
        mensajeError.style.color = "green";
        apeinp.setCustomValidity("");
        return true;
    }
    
}
function telefono() {
    var fono2 = document.getElementById("fono");
    var telefono = document.getElementById("fono").value;
    var mensajeError = document.getElementById("mensajeErrorTelefono");

    if (telefono === "") {
        mensajeError.innerText = "Por favor, ingrese su número telefónico";
        mensajeError.style.color = "red";
        fono2.setCustomValidity("telefono no valido");
        return false;
    } else if (telefono.length !== 9) {
        mensajeError.innerText = "Por favor, ingrese un número válido";
        mensajeError.style.color = "red";
        fono2.setCustomValidity("telefono no valido");
        return false;
    } else {
        mensajeError.innerText = "Número válido ✅";
        mensajeError.style.color = "green";
        fono2.setCustomValidity("");
        return true;
    }
    
}
function comuna() {
    var comubinp = document.getElementById("comuna");
    var nombre = document.getElementById("comuna").value;
    var mensajeError = document.getElementById("mensajeErrorComuna");

    if (nombre === "") {
        mensajeError.innerText = "Por favor, ingrese una comuna.";
        mensajeError.style.color = "red";
        comubinp.setCustomValidity("no");
        return false; // Evita que se envíe el formulario si el nombre está vacío
    } else {
        mensajeError.innerText = "direccion correcta ✅";
        mensajeError.style.color = "green";
        comubinp.setCustomValidity("");
        return true;
    }
}
function direc() {
    var direcinp = document.getElementById("direc");
    var nombre = document.getElementById("direc").value;
    var mensajeError = document.getElementById("mensajeErrorDirec");

    if (nombre === "") {
        mensajeError.innerText = "Por favor, ingrese una direccion.";
        mensajeError.style.color = "red";
        direcinp.setCustomValidity("no");
        return false; // Evita que se envíe el formulario si el nombre está vacío
    } else {
        mensajeError.innerText = "Nombre correcto ✅";
        mensajeError.style.color = "green";
        direcinp.setCustomValidity("");
        return true;
    }
}






function soloNumeros(event) {
    var charCode = (event.which) ? event.which : event.keyCode;
    if (charCode > 31 && (charCode < 48 || charCode > 57)) {
        event.preventDefault();
        return false;
    }
    return true;
}
// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault()
                event.stopPropagation()
            }

            form.classList.add('was-validated')
        }, false)
    })
})()