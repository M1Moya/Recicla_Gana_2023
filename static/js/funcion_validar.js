$(document).on('click', '#registrar', () => {
    let rut = $('#id_rut').val();

    let rutValidador = new RutValidador(rut);

    if (rutValidador.esValido) {
       $('#validar_rut').text("Rut válido")
       return; 
    }
    $('#validar_rut').text('Rut inválido')
})