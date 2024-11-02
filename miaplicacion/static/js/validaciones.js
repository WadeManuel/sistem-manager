const monto=document.getElementById("monto");
const boton=document.getElementById("btn-enviar");
const resultado=document.querySelector(".resultado");


boton.addEventListener("click",(e)=>{
    if(error[0]){
        alert("hola ");
        e.preventDefault();
        resultado.innerHTML=error[1];
        resultado.classList.add("red");
    }else{
        resultado.innerHTML="Datos  creado correctamente";
        resultado.classList.remove("red");
        resultado.classList.add("green");
    }
});

const validarCampos=()=>{
    let error=[];
    if(monto.value > 500000 && monto.value < 10000 ){
        error[0]=[true];
        error[1]="El monto no puede ser mayor a 500k o menor a 10k";
        return error;
    }
    return false;
    return error;
}