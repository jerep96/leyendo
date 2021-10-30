function copiarAlPortapapeles(id_elemento) {

	  // Crea un campo de texto "oculto"
	  var aux = document.createElement("input");

	  // Asigna el contenido del elemento especificado al valor del campo
	  aux.setAttribute("value", document.getElementById(id_elemento).innerHTML);


	  // Añade el campo a la página
	  document.body.appendChild(aux);

	  // Selecciona el contenido del campo
	  aux.select();

	  // Copia el texto seleccionado
	  document.execCommand("copy");

	  // Elimina el campo de la página
	  document.body.removeChild(aux);

	  alert("Copiado con éxito")
	}

$(document).ready(function(){
    let select = document.getElementById("id_modo");
    let selectedOption = select.options[select.selectedIndex];
    $("#formNameB").hide();
    $("#formNameS").hide();
    $("#formNameO").hide();
    if (selectedOption.value === 'Business') {
        $("#id_imageB").show();
        $("#id_portadaB").show();
        $("#nombreB").show();
        $("#id_nombreB").show();
        $("#id_imageS").hide();
        $("#id_portadaS").hide();
        $("#nombreS").hide();
        $("#id_nombreS").hide();
        $("#id_imageO").hide();
        $("#id_portadaO").hide();
        $("#nombreO").hide();
        $("#id_nombreO").hide();
    } else if (selectedOption.value === 'Social') {
        $("#id_imageB").hide();
        $("#id_portadaB").hide();
        $("#nombreB").hide();
        $("#id_nombreB").hide();
        $("#id_imageS").show();
        $("#id_portadaS").show();
        $("#nombreS").show();
        $("#id_nombreS").show();
        $("#id_imageO").hide();
        $("#id_portadaO").hide();
        $("#nombreO").hide();
        $("#id_nombreO").hide();
    } else {
        $("#id_imageB").hide();
        $("#id_portadaB").hide();
        $("#nombreB").hide();
        $("#id_nombreB").hide();
        $("#id_imageS").hide();
        $("#id_portadaS").hide();
        $("#nombreS").hide();
        $("#id_nombreS").hide();
        $("#id_imageO").show();
        $("#id_portadaO").show();
        $("#nombreO").show();
        $("#id_nombreO").show();
    }
    $('#id_modo').on('change',function(){
        let form = document.getElementById("form");
        if (this.value === 'Business') {
            $("#id_imageB").show();
            $("#id_portadaB").show();
            $("#nombreB").show();
            $("#id_nombreB").show();
            $("#id_imageS").hide();
            $("#id_portadaS").hide();
            $("#nombreS").hide();
            $("#id_nombreS").hide();
            $("#id_imageO").hide();
            $("#id_portadaO").hide();
            $("#nombreO").hide();
            $("#id_nombreO").hide();
            form.submit();
        } else if (this.value === 'Social') {
            $("#id_imageB").hide();
            $("#id_portadaB").hide();
            $("#nombreB").hide();
            $("#id_nombreB").hide();
            $("#id_imageS").show();
            $("#id_portadaS").show();
            $("#nombreS").show();
            $("#id_nombreS").show();
            $("#id_imageO").hide();
            $("#id_portadaO").hide();
            $("#nombreO").hide();
            $("#id_nombreO").hide();
            form.submit();
        } else {
            $("#id_imageB").hide();
            $("#id_portadaB").hide();
            $("#nombreB").hide();
            $("#id_nombreB").hide();
            $("#id_imageS").hide();
            $("#id_portadaS").hide();
            $("#nombreS").hide();
            $("#id_nombreS").hide();
            $("#id_imageO").show();
            $("#id_portadaO").show();
            $("#nombreO").show();
            $("#id_nombreO").show();
            form.submit();
        }
    })
});
function changeNameB() {

  $("#nombreB").hide();
  $("#nombreS").hide();
  $("#nombreO").hide();
  $("#formNameB").show();
  $("#formNameS").hide();
  $("#formNameO").hide();
}
function changeNameS() {

  $("#nombreB").hide();
  $("#nombreS").hide();
  $("#nombreO").hide();
  $("#formNameB").hide();
  $("#formNameS").show();
  $("#formNameO").hide();
}
function changeNameO() {

  $("#nombreB").hide();
  $("#nombreS").hide();
  $("#nombreO").hide();
  $("#formNameB").hide();
  $("#formNameS").hide();
  $("#formNameO").show();
}
function saveB(){
    let formB = document.getElementById("formNameB");
    formB.submit();
}
function saveS(){
    let formS = document.getElementById("formNameS");
    formS.submit();
}
function saveO(){
    let formO = document.getElementById("formNameO");
    formO.submit();
}

function capturarGuardar() {
    let navegador = navigator.userAgent.toLowerCase();
    let tipoCadena = 0
    if(navegador.indexOf('chrome') > -1){
        tipoCadena = 1
    } else if(navegador.indexOf('firefox') > -1){
        tipoCadena = 1
    } else if(navegador.indexOf('opera') > -1){
        tipoCadena = 1
    } else {
        tipoCadena = 2
    }
    console.log(navegador)
    console.log(tipoCadena)

    let nombre = document.getElementById("nombre").textContent
    let company = document.getElementById("company").textContent
    let location = document.getElementById("location").textContent
    let phone = document.getElementById("phone").textContent
    let mail = document.getElementById("mail").textContent
    let website = document.getElementById("website").textContent
    if (tipoCadena === 1) {
        cadena = 'BEGIN:VCARD\n'
        cadena += 'VERSION:3.0\n'
        cadena += 'N:' + nombre +'\n'
        cadena += 'FN:' + nombre + '\n'
        cadena += 'ORG:' + company + '\n'
        cadena += 'TEL;waid='+ phone + ':' + phone + '\n'
        // cadena += 'X-ABLabel:M&oacute;vil' + '\n'
        cadena += 'ADR:' + location + '\n'
        cadena += 'URL:' + website + '\n'
        cadena += 'EMAIL;type=INTERNET:' + mail + '\n'
        // cadena += 'item2.X-ABLabel:Casa' + '\n'
        cadena += 'END:VCARD'

        console.log(cadena)
        let blob = new Blob([cadena]);
        saveAs(blob, `${nombre}.vcf`)
    } else if (tipoCadena === 2) {
        cadena = 'BEGIN:VCARD\n'
        cadena += 'VERSION:3.0\n'
        cadena += 'N:' + nombre +'\n'
        cadena += 'FN:' + nombre + '\n'
        cadena += 'ORG:' + company + '\n'
        cadena += 'TEL;waid='+ phone + ':' + phone + '\n'
        // cadena += 'X-ABLabel:M&oacute;vil' + '\n'
        cadena += 'ADR:' + location + '\n'
        cadena += 'URL:' + website + '\n'
        cadena += 'CORREO ELECTRÓNICO,INTERNET:' + mail + '\n'
        // cadena += 'item2.X-ABLabel:Casa' + '\n'
        cadena += 'END:VCARD'
        console.log(cadena)
        let blob = new Blob([cadena]);
        let fileLink = document.createElement("a");

        fileLink.href = window.URL.createObjectURL(blob);
        fileLink.setAttribute("download", `${nombre}.vcf`);
        document.body.appendChild(fileLink);

        fileLink.click();
        // saveAs(blob, `${nombre}.vcf`)
    }
}
