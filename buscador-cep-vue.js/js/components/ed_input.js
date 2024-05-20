import {ref,watch} from 'vue'

export const ed_input = {


    props:['input_data'],
    emits:['update_input_data'],

    setup(props,ctx){

        const content = ref(props.input_data);

        const exibir_erro = ref(false)

        watch(

            () => content.value.value,
            (newValue, oldValue)=>{

                const cepSemMascara = newValue.replace(/\D/g, ''); // Remove caracteres não numéricos

                let cepComMascara = cepSemMascara.replace(/^(\d{5})(\d)/, '$1-$2'); // Aplica a máscara

                content.value.value = cepComMascara;

                if(cepSemMascara.length == 8){

                    consultarCEP(cepSemMascara);

                }

            }

        )

        function consultarCEP(cep){

            fetch(`https://nominatim.openstreetmap.org/search?addressdetails=1&postalcode=${cep}&country_code=br&format=json&limit=1`)
                        .then(response => {

                        if (!response.ok) {

                        throw new Error('Erro ao obter os dados da API');

                        }
                        return response.json(); // Converte os dados da resposta para JSON

                    })
                    .then(data => {

                        exibir_erro.value = false

                        let dados = {};

                        dados.cep = cep;
                        dados.bairro = data[0].address.suburb;
                        dados.cidade = data[0].address.city_district;
                        dados.estado = data[0].address.state;
                        dados.uf = data[0].address['ISO3166-2-lvl4'].split('-')[1];

                        ctx.emit('update_input_data', dados);

                    })
                    .catch(error => {

                        exibir_erro.value = true
                    
                    })

        }

        return {

            content,
            watch,
            exibir_erro
        }

    },
    template: `

        <label style="color:#68B281" class="mb-2">{{content.label}} :</label>
        <input v-model="content.value" :type="content.type" class="form-control" maxlength="9" :placeholder="content.placeholder" style="color:#68B281">
        <small  class="text-danger" v-show="exibir_erro">Falha ao buscar cep</small>

    `


}