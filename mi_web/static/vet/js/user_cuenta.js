//--------------------------------------------------------------------------------------------

function contra_1() {
    var contraseña = document.getElementById("vali_contra").value;
    var mensajeError = document.getElementById("mensajeErrorvali_contra");

    if (contraseña === "") {
        mensajeError.innerText = "Por favor, ingrese una contraseña";
        mensajeError.style.color = "red";
        return false;// Evita que se envíe el formulario si la contraseña está vacía
    } else if (contraseña.length < 6) {
        mensajeError.innerText = "La contraseña debe tener al menos 6 caracteres";
        mensajeError.style.color = "red";
        return false;// Evita que se envíe el formulario si la contraseña tiene menos de 6 caracteres
    } else {
        mensajeError.innerText = "Contraseña ingresada ✅";
        mensajeError.style.color = "green";
        return true;
    }
}


function nombre_v() {
    var nombre = document.getElementById("vali_nombre").value;
    var mensajeError = document.getElementById("mensajeErrorvali_nombre");

    if (nombre === "") {
        mensajeError.innerText = "Por favor, ingrese su nombre.";
        mensajeError.style.color = "red";
        return false; // Evita que se envíe el formulario si el nombre está vacío
    } else {
        mensajeError.innerText = "Nombre correcto ✅";
        mensajeError.style.color = "green";
        return true;
    }
}

function apellido_v() {
    var apellido = document.getElementById("vali_ape").value;
    var mensajeError = document.getElementById("mensajeErrorvali_ape");

    if (apellido === "") {
        mensajeError.innerText = "Por favor, ingrese su apellido.";
        mensajeError.style.color = "red";
        return false; // Evita que se envíe el formulario si el apellido está vacío
    } else {
        mensajeError.innerText = "Apellido correcto ✅";
        mensajeError.style.color = "green";
        return true;
    }
    
}

function telefono() {
    var telefono = document.getElementById("vali_fono").value;
    var mensajeError = document.getElementById("mensajeErrorvali_fono");

    if (telefono === "") {
        mensajeError.innerText = "Por favor, ingrese su número telefónico";
        mensajeError.style.color = "red";
        return false;
    } else if (telefono.length !== 9) {
        mensajeError.innerText = "Por favor, ingrese un número válido";
        mensajeError.style.color = "red";
        return false;
    } else {
        mensajeError.innerText = "Número válido ✅";
        mensajeError.style.color = "green";
        return true;
    }
    
}

function tageta_v() {
    var numeroTarjeta = document.getElementById("vali_targe").value;
    var mensajeError = document.getElementById("mensajeErrorvali_targe");

    if (numeroTarjeta === "") {
        mensajeError.innerText = "Por favor, ingrese su targeta.";
        mensajeError.style.color = "red";
        return false;
    } else if (!/^[0-9]+$/.test(numeroTarjeta)) {
        mensajeError.innerText = "Por favor, no ingrese letras";
        mensajeError.style.color = "red";
        return false;
    } else if (numeroTarjeta.length !== 16) {
        mensajeError.innerText = "Por favor, ingrese una targeta válida ";
        mensajeError.style.color = "red";
        return false;
    } else {
        mensajeError.innerText = "Targeta válida ✅";
        mensajeError.style.color = "green";
        return true;
    }
    
}

function vencimiento_v() {
    var fechaups = document.getElementById("vali_fv");
    var fechaIngresada = document.getElementById("vali_fv").value;
    var mensajeError = document.getElementById("mensajeErrorvali_fv");

    // Obtiene el mes y el año actuales del sistema
    var fechaActual = new Date();
    var mesActual = fechaActual.getMonth() + 1; // Se suma 1 porque los meses van de 0 a 11
    var añoActual = fechaActual.getFullYear().toString().slice(-2);
    
    // Obtiene el mes y el año de la fecha ingresada por el usuario
    var partesFecha = fechaIngresada.split('/');
    var mesIngresado = parseInt(partesFecha[0], 10);
    var añoIngresado = parseInt(partesFecha[1], 10);

    // Expresión regular para verificar si el mes está en el rango de 01 a 12
    var regex = /^(0[1-9]|1[0-2])$/;

    if (fechaIngresada === "") {
        mensajeError.innerText = "Por favor, ingrese una fecha";
        mensajeError.style.color = "red";
        fechaups.setCustomValidity("no valido");
        return false;
    } else if (fechaIngresada.length !== 5) {
        mensajeError.innerText = "Por favor, ingrese una fecha válida (mes/año)";
        mensajeError.style.color = "red";
        fechaups.setCustomValidity("no valido");
        return false;
    } else if (!regex.test(partesFecha[0])) {
        mensajeError.innerText = "Por favor, ingrese un mes válido (01-12)";
        mensajeError.style.color = "red";
        fechaups.setCustomValidity("no valido");
        return false;
    } else if (añoIngresado < añoActual || (añoIngresado === añoActual && mesIngresado < mesActual)) {
        mensajeError.innerText = "Su tarjeta ya expiró, pruebe con otra.";
        mensajeError.style.color = "red";
        fechaups.setCustomValidity("no valido");
        return false; // Evita que se envíe el formulario
    }  else {
        mensajeError.innerText = "Fecha válida ✅";
        mensajeError.style.color = "green";
        fechaups.setCustomValidity("");
        return true;
    }
}

function codigo_v() {
    var cs = document.getElementById("vali_cs").value;
    var mensajeError = document.getElementById("mensajeErrorvali_cs");

    if (cs === "") {
        mensajeError.innerText = "Por favor, ingrese una código de seguridad ";
        mensajeError.style.color = "red";
        return false;
    } else if (cs.length !== 3) {
        mensajeError.innerText = "Por favor, ingrese una código de seguridad válido";
        mensajeError.style.color = "red";
        return false;
    } else {
        mensajeError.innerText = "Código de seguridad válido ✅";
        mensajeError.style.color = "green";
        return true;
    }
    
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



// Función para agregar la barra automáticamente después de ingresar el mes
document.getElementById('fecha').addEventListener('input', function (e) {
    var input = e.target;
    if (input.value.length === 2 && !input.value.includes('/')) {
        input.value += '/';
    }
});
document.getElementById('fecha').addEventListener('input', function (e) {
    var input = e.target;
    input.value = input.value.replace(/[^\d\/]|^\/$/g, ''); // Elimina cualquier carácter que no sea dígito o "/" y evita una barra solitaria al inicio
});

function soloNumeros(event) {
    var charCode = (event.which) ? event.which : event.keyCode;
    if (charCode > 31 && (charCode < 48 || charCode > 57)) {
        event.preventDefault();
        return false;
    }
    return true;
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


function validarvali1(){
    contra_1();

}
function validarvali2(){
    nombre_v();
    apellido_v();
    
}
function validarvali3(){
    tageta_v();
    vencimiento_v();
    codigo_v();
    telefono();
    
}
