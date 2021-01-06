# DesafioTesterHw-Fw
Repositório para desafio Tester HW/FW - Raspberry -Python

### Programas necessários ###

* Pycharm
* Raspbian
* PuTTY
* Etcher
* Arquivo de imagem do sistema operacional linux 

### Configurando o ambiente ###

1 - Instale todos os programas acima

2 - Insira o cartão SD e grave o arquivo de imagem no mesmo, utilzando o Etcher.

3 - É necessário inserir as configurações de uma ou mais redes WiFi, criando um arquivo txt com o nome wpa_supplicant.conf, basta abri-lo e copiar o codigo
abaixo e preencher os campos ssid com o nome da rede e o psk com a chave da rede,e copiar esse arquivo para o cartão SD. 

```
#network config
country = BR
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network= {
    ssid = "RedeInatel "
    psk = "inatelsemfio"
    key_mgmt=WPA-PSK
}
```
4 - Habilite o ssh - criando um arquivo de texto no cartão sd com nome ssh 

5 - Ejete o cartao e insira no raspberry pi, ligue-o e em seguida abra o PuTTY (inseri o IP dado no desafio 192.168.0.110)

6 - Faça o login q por padrão é login: pi e senha: "raspberry" e está pronta toda configuração do raspberry.

7 - Abra o pycharm crie um projeto, mude a configuração do seu interpretador para ssh, inserindo novamente o ip (192.168.0.110) e senha "raspberry" e
selecione a versão do python a ser utilizada(python3) assim finalize a criação do projeto dentro do diretório do raspberry.
 
### Componentes necessarios ###

* 1 LED 

* 1 push-button

* 1 resistor de 1k 

* 1 protoboard 

* Fios para integração do raspberry com o protoboard
