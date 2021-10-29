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

	  alert("URL copiada")
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
