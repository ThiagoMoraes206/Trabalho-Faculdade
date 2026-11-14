
document.addEventListener("DOMContentLoaded", () => {

    const formulario = document.querySelector(".form-calculo");

    if (!formulario) return;

    formulario.addEventListener("submit", async (evento) => {

        evento.preventDefault();

        const resultado = document.querySelector(".resultado");

        const valor1 = formulario.elements.valor1.value;
        const valor2 = formulario.elements.valor2.value;

        try {

            const resposta = await fetch(formulario.dataset.endpoint, {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    valor1: valor1,
                    valor2: valor2
                })

            });

            const dados = await resposta.json();

            if (!resposta.ok) {
                throw new Error(dados.erro || "Erro no cálculo.");
            }

            resultado.textContent = `Resultado: ${dados.resultado}`;

            resultado.classList.remove("erro");

        } catch (erro) {

            resultado.textContent = erro.message;

            resultado.classList.add("erro");

        }

    });

});