function limpiar() {
    document.getElementById("password").value = "";
    document.getElementById("passwordc").value = "";
}

function validateForm() {
    var nombre = document.forms["myForm"]["nombre"].value;
    var apellidos = document.forms["myForm"]["apellidos"].value;
    var email = document.forms["myForm"]["email"].value;
    var telefono = document.forms["myForm"]["telefono"].value;
    var sexo = document.forms["myForm"]["sexo"].value;
    var empresa = document.forms["myForm"]["empresa"].value;
    var ejecutivo = document.forms["myForm"]["ejecutivo"].value;

    if (nombre == "") {
        alert("Introduzca su Nombre(s)");
        return false;
    }
    if (apellidos == "") {
        alert("Introduzca sus Apellidos");
        return false;
    }
    if (email == "") {
        alert("Introduzca su Correo Electrónico");
        return false;
    }
    if (telefono == "") {
        alert("Introduzca su Número de Teléfono");
        return false;
    }
    if (empresa == "") {
        alert("Introduzca el nombre de su Empresa");
        return false;
    }
    if (ejecutivo == "") {
        alert("Introduzca el nombre de su Ejecutivo");
        return false;
    }
    if (password == "") {
        alert("Introduzca una Contraseña");
        return false;
    }
    else {
      return true;
    }

}



document.addEventListener("DOMContentLoaded", function () {
    var phoneMask = new IMask(document.getElementById('telefono'), {
      mask: '(00) 0000-0000'
    }).on('accept', function() {
      document.getElementById('phone-complete').style.display = '';
      document.getElementById('phone-unmasked').innerHTML = phoneMask.unmaskedValue;
    }).on('complete', function() {
      document.getElementById('phone-complete').style.display = 'inline-block';
    });
    var cellphoneMask = new IMask(document.getElementById('celular'), {
      mask: '+{52} (00) 0000-0000'
    }).on('accept', function() {
      document.getElementById('phone-complete').style.display = '';
      document.getElementById('phone-unmasked').innerHTML = phoneMask.unmaskedValue;
    }).on('complete', function() {
      document.getElementById('phone-complete').style.display = 'inline-block';
    });
    var phoneMask = new IMask(document.getElementById('nombre_modelo'), {
      mask: '00-00'
    }).on('accept', function() {
      document.getElementById('phone-complete').style.display = '';
      document.getElementById('phone-unmasked').innerHTML = phoneMask.unmaskedValue;
    }).on('complete', function() {
      document.getElementById('phone-complete').style.display = 'inline-block';
    });
  });

  $(document).ready(function () {
    $("#modelo").change(function () {
      var value = $(this).val();
      $("#modelore").val(value);
    });
  });



function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('txt').innerHTML =
    h + ":" + m + ":" + s;
    var t = setTimeout(startTime, 500);
}
function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}

$(document).ready(function () {
  var element = document.getElementsByClassName("checkbox")[0];
  element.classList.remove("checkbox");
  var elemento = document.getElementsByClassName("checkbox")[0];
  elemento.classList.remove("checkbox");
  var elemen = document.getElementsByClassName("checkbox")[0];
  elemen.classList.remove("checkbox");
});

 $('#cantidad').bind('input', function() {
   qty = $(this).val() // get the current value of the input field.
   document.getElementById("total1").value = ({{producto.precio}}*qty);
 });
