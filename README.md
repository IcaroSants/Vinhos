# Vinhos

O projeto consiste em uma página que determina a qualidade do vinho a partir de atributos que o usuario preenche no formulario.

## Tabela de conteúdos

* Sobre
* Como usar
    * Pré-requisitos
    * Como executar

## Sobre 
O projeto usa uma pagina web com um formulario para pegar os dados que serão utilizados como entrada em um modelo de machine learning que ira classificar se o vinho é bom ou ruim. 

O funcionamento consiste em um usuário  que insere informações depois o formulário envia as informações para o back-end que organiza as informações e se comunica com a API que faz o processo de classificação. 

O arquivo  **app** tem todas as configurações do back-end. Ele foi  desenvolvido em  python e utilizando o microframework **flask**. O modelo de classifiação escolhido inicialmente foi o de regressão logística, usando sklearn e mlflow.

A página foi feita com html e estilizado com css(bootstrap). Se ápos o processo de classificação o vinho for classificado como bom a página exibi um foto de um emoji positivo, caso contrário um emoji negativo.

## Como usar
### Pré-Requisitos
Para rodar o projeto é necessario ter as seguintes bibliotecas instaladas:

* Flask;
* Scikit-Learn;
* Pandas;
* MLFlow;
* Numpy;
* Matplotlib;
* Json;
* Requests;

O arquivo **requiriments.txt** contem as versões das bibliotecas usadas.

### Como executar

Primeiramente terá que ser inicializado o servido do MLFlow, para o sistema poder consumir o modelo de classificação. Para isso temos que executar o comando: **mlflow models serve --model-uri runs:/3255027ab4ce4371a7afffc56c70e562/LR -p porta --env-manager local**. A única alteração é na troca do nome **porta** pelo número da porta que você irá usar. Ápos isso, será gerado um link que você copiará e colocará  no arquivo **app** no local especificado.

Depois disso, é so executar o arquivo **app**, abrir  o link e usar.



