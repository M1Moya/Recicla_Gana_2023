
class RutValidador{
    constructor(rut){
        this.rut = rut;
        //Obtenemos el último caracter del Rut
        this.dv = this.rut.substring(this.rut.length -1);
        //Limpiar el rut, dejando solo los números
        this.rut = this.rut.substring(0, this.rut.length -1).replace(/\D/g,'');
        this.esValido = this.validarRut();
    }

    validarRut() {
        let numerosArray = this.rut.split('').reverse
        let acumulador = 0;
        let multiplicador = 2;

        for(let numero of numerosArray){
            acumulador += parseInt(numero) * multiplicador;
            multiplicador++;

            if (multiplicador == 8){
                multiplicador=2;
            }
        }

        let dv = 11 - (acumulador %11);

        if (dv == 11)
            dv = '0'
        if (dv == 10)
            dv ='K'
        return dv === this.dv
    }

    formato(){
        if (!this.esValido) return '';
        return this.rut.toString().replace(/\B(?=(\d{3})+(?!\d))/g,'.') + '-' + this.dv;
    }
}