![FAST](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQR_ubDgmrhzWsr6VESmhjUQukf__nsOejPig&usqp=CAU)

<h1>Sejam muito bem vindos ao meu projeto de FastAPI com docker e Postgres!</h2>

<p>Neste projeto se encontra todos os requisitos solicitados, mas para poder executa-los, é necessário que o ambiente seja preparado seguindos os passos abaixo.</p>.

<h3>Instalando Docker</h2>
<p> Neste passo vamos instalar o famoso Docker, e para que isso seja possivel, é necessário que você siga a a documentação e faça a instalação de acordo com o seu sistema operacional.</p>
 <a href=https://learn.microsoft.com/pt-br/virtualization/windowscontainers/manage-docker/configure-docker-daemon> Windows</a>
 <br>
 <a href=https://docs.docker.com/desktop/install/linux-install/>Linux</a>
 <br>
 <a href=https://docs.docker.com/desktop/install/mac-install/>Mac</a>
 <br>

<h3>Instalando VSCode</h3>
<p>A IDE utilizada neste projeto é o "VSCode", por ser uma IDE mais interativa com a nossa aplicação e suas extensões. Mas você pode utilizar outra IDE de sua escolha.</p>
 <a href=https://code.visualstudio.com/download> Windows</a>
  <br>
  <a href=https://code.visualstudio.com/download/>Linux</a>
  <br>
  <a href=https://code.visualstudio.com/download/>Mac</a>
  
  <br>
  <br>
  <p>Após a instalação, vamos configurar o VSCode para que possamos rodar a nossa aplicação.</p>
  <h3>Primeiro Passo</h3>
  
  ![docker](https://brianchristner.io/content/images/2019/03/vs-code-docker-2.png)
  ![dev_container](https://code.visualstudio.com/assets/docs/devcontainers/tutorial/dev-containers-extension.png)
  
  <p> Após a instalação, abra o VSCode e selecione a pasta da sua aplicação, após de aberto, vá na barra a esquerda do VSCode e clique no icone "     Extensões" ou se preferir "Crtl+Shift+X" para abrir, e digite na barra de pesquisa "Docker" e instale. Após a instalação da extensão "Docker", repita os passos para instalar o "Dev-Container".</p>
 
 <h3>Segundo Passo</h3>
 <p>Agora vamos configurar as extensões para que possamos rodar a aplicação, vou listar os passos deste procedimento abaixo para que você consiga configurar.</P
<br>
 <p>1° Pressione "CRTL+SHIT+P" para abrir uma caixa de configuração bem a cima, apos isso, você tem que digitar "Dev Container" Add Dev Container   Configuration Files".</p>
 <br>
 <p>2° Agora você digita "Python" e escolha a segunda opção "Python3 & Postgres" e pressione enter</p>
 <br>
 <p>3° Escolha a versão do python 3.7 ou superior, depois de ter escolhido, é só pressionar "Enter" e clicar em "Ok".</p>
 
 <p> Depois de seguir todas as configurações a cima, ele vai criar o ambiente, e partir dai  você vai estar dentro do container e pronto para iniciar a aplicação. Caso você tenha dificuldades ou duvidas sobre como configurar o ambiente a cima, é só clicar no link, que você vai ser direcionado ao videos de como configurar o "Dev Container".</p>

<a href='https://www.youtube.com/watch?v=61M2takIKl8&list=PLj6YeMhvp2S5G_X6ZyMc8gfXPMFPg3O31'>Dev Container Configuration</a>

<br>

<h3>Executando a Aplicação</h3>

<p> 1° Abra o terminal dentro da sua IDE e digite o seguinte comando "pip install --user -r requirements.txt", este comando irá instalar todos os apcotes necessários para que a aplicação rode.
 <br>
<p> 2° No terminal novamente, digite o comando "uvicorn main:app --reload" para que se inicie a aplicação, logo em seguida ele irá subir uma caixa de dialogo perguntando se você deseja abrir no Browser.
 <br>
 <p> 3° Após ele abrir no terminal, adicione no final do link um "/docs" igual o link a seguir "http://127.0.0.1:8000/docs", ele vai abrir um swagger para que você possa interagir com a aplicação.
 <br>
<p> 4° No Swagger você tem 4 "GETS" para que você possa testar as funcionalidades e ver o retorno que cada uma tras, para que você possa utilizar, você clica no "get" que vocês quer e logo após de aberto, você clica numa botão escrito "Try Out" para que ele te permita adicionar uma saida diferente, após ele permitir, você digita o que é requisitado, como no exemplo da imagem abaixo.
