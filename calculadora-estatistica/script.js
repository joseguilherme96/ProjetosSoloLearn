function organizar(){
    let sequenciaNumeros = document.getElementById("sequenciaNumeros").value

    let sequencia = sequenciaNumeros.split(",");

    // Organiza em ordem crescente
    limite = Number(sequencia.length) - 1;
    processamento = 1000 // O numero de vezes que vai se repetir para garantir que os numeros e organizem
        
    for(let k=0; k < processamento; k++){

        for(let z = 0; z < limite;z++){

                if(Number(sequencia[z]) > Number(sequencia[z+1])){
                    
                    let temp = Number(sequencia[z+1]);
                    sequencia[z+1] = Number(sequencia[z]);
                    sequencia[z] = temp;

                }
        }
        z = 0
        
    }
   
    let numerosOrganizados = document.getElementById("numerosOrganizados");

    numerosOrganizados.innerHTML = sequencia;
    
    media(sequencia)
    mediana(sequencia)
    moda(sequencia)

}


function media(sequencia){

    let tamanhoLista = sequencia.length;

    let soma = 0

    for(let i=0; i < tamanhoLista;i++){

        soma += Number(sequencia[i]);

    }

    media = soma / tamanhoLista;

    let somatoriaNumeros = document.getElementById("media");

    somatoriaNumeros.innerHTML = media;

}

function mediana(sequencia){
    
    let tamanhoLista = Number(sequencia.length);

    if(tamanhoLista % 2 == 0){

        primeiroElementoCentral = tamanhoLista/2;
        segundoElementoCentral =  (tamanhoLista/2) + 1

        media = (sequencia[primeiroElementoCentral-1] + sequencia[segundoElementoCentral-1]) / 2
        

    }else{

        elementoCentral = ((tamanhoLista - 1) / 2) + 1
        media = sequencia[elementoCentral-1] / 2;

    }

    let mediaSequencia = document.getElementById("mediana");

    mediaSequencia.innerHTML = Number(media).toFixed(2);

}

function moda(sequencia){

    let conta = 1; // Armazena a quantidade de vezes que o mesmo numero se repete dentro da sequência

    let agrupamentoSequencia = []; // Agrupa sequencias de mesmo valor que se repetem na lista valor
    let quantidade = []; // Armazena a quantidade de vezes que o numero se repete na sequência
    
    
    // Agrupamento numeros repetidos
    for(let i=0;i< sequencia.length;i++){

        if(sequencia[i] == sequencia[i+1] ){
            
            conta +=1
        
        }else{
            
            quantidade.push(conta)
            agrupamentoSequencia.push(sequencia[i]);
            conta = 1
        }

    }

    let modaTemp = "";
    let repeteTemp = 0;

    for(let x=0; x< agrupamentoSequencia.length;x++){
        
        if(quantidade[x] > repeteTemp){
            repeteTemp = quantidade[x];
            modaTemp = agrupamentoSequencia[x];
        }else if(quantidade[x] == repeteTemp){
            modaTemp += ","+agrupamentoSequencia[x];
        }

    }


    let moda = document.getElementById("moda");
    moda.innerHTML = modaTemp;

    let mensagemModa = document.getElementById("mensagemModa");
    mensagemModa.innerHTML = mensagem;

}
