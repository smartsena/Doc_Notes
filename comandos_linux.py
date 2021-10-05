***COMANDOS LINUX***

links úteis
	https://www.hostinger.com.br/tutoriais/comandos-linux

whoami
	Comando quem sou eu que lista qual é o usuário que esta logado
sudo su
	loga como usuário root
ls 
	listar documentos dentro do diretório
	ls -A
		mostra pastas e documentos ocultas
	ls -l
		mostra a extrutura de permissões
	ls -lha
		lista pastas e arquivos ocultos

cd
	chandger directory - navega para dentro de um diretório
	cd..
		retorna um nível acima

mkdir 'xpto'
	make directory - cria pastas

rmdir ''
	remove directory - apaga pastas - exclui - delete
	rm -r
		remove recursivamente mesmo que tenha arquivos dentro do repositório
find 'diretórioDaBusca' -iname *'nomeDaBusca'*
	procura trecho do nome de uma busca
pwd
	print work directory - mostra  o caminho completo

touch
	cria arquivos
	acrescentar a extenção
		EX. script_temp.txt
nano 'nome do arquivo'
	abre o arquivo dentro do terminal para edição
cat 'nome do arquivo'
	mostra o que está escrito dentro do arquivo
man 'nome do comando'
	abre o manual do comando
'nome do comando' --help
	menu de ajuda mais simplificado

'Contrl' + C
	interrompe qualquer execução


sudo snap install [pycharm-professional|pycharm-community] --classic

-------------------------------------------------
sudo add-apt-repository ppa:deadsnakes/ppa


tar -xJvf [nome do arquivo]
tar -xvf [nome do arquivo]
	descompactar zip arquivos compactado


apt
	Advanced Packaging Tool (Ferramenta de Empacotamento Avançada, normalmente referida como "apt” apenas)


sudo apt install apt-transport-https ca-certificates curl software-properties-common
	Update the apt package list and install the dependencies necessary to fetch packages from https sources:

sudo apt update
	parametro para atualizar o sistema
	update list of available packages
apt list --upgradable
	visualizar quais programas e pacotes tem para serem atualizados

sudo apt upgrade - upgrade the system by installing/upgrading packages
sudo apt full-upgrade - upgrade the system by removing/installing/upgrading packages


ps -e
	lista todos os processos que estão rodando no linux
kill [número_do_processo]
	encerra a execução do prcesso na máquina
	
--------------------------------------
dpkg -i 'nome do executável .deb'
	instalação de programas .deb
	dpkg 
		utilitário de instalação de pacotes .deb 
		os que não são distribuidos no repositório linux

apt
	advanced package tools
	gerenciador de pacotes e distribuição Debian basid



Tudo o que tem 'sudo' na frente significa para dar permissões de super usuário para o comando a seguir


Qual a versão estou utilizando (softwares)
	EX.
		python3 -V
	https://www.vivaolinux.com.br/dica/Verificando-a-versao-do-Python

vi [nome do arquivo]
	precionando ESC 
		sai do mode de edição
	:w
		salva as alterações no arquivo
	:q 
		para sair do vi

source [nome do arquivo]
	faz a releitura do arquivo para pegar as alterações realizadas para rodar
	
Listar todos os serviços
	sudo systemctl list-unit-files --type service --all
	https://www.hostinger.com.br/tutoriais/listar-servicos-linux
	netstat -anp | grep 8080
	Todos os serviços e portas detalhado
		sudo ss -tulpn
		sudo netstat -tulpn


Na expressão condicional do while é possível utilizar qualquer operador de comparação (< [menor], > [maior], <= [menor ou igual], >= [maior ou igual], == [igual a] e != [diferente de]) e qualquer operador lógico (&& [and], || [ou]).
Isso aí, aluno! Todos os operadores de comparação e lógicos são válidos na expressão condicional do while! Use-os com sabedoria!
O while sempre precisará de uma expressão condicional que definirá quando o laço deve ser interrompido.
------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------

'------------------------------------------------------------------------------------------------------------'

------SOFTWRES----------------------------------------------------------------------------------------------

'------------------------------------------------------------------------------------------------------------'	

------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------


Módulos Matemáticos em Python: Math e Cmath
	Funções Aritiméticas
	Funções Trigonométricas
	Funções Hiperbólicas
	Funções de Logarítimicas e de Potência
	Números Complexos
		Números complexos são presentados internamente por coordenadas polares ou Cartesianas. Um número complexo z será representado em coordenadas Cartesianas como z = x + iy, onde x representa a parte real e y representa a imaginária. Outra forma de representá-los é por coordenadas polares.




Rede
	NMAP 
		apt-get install nmap
		nmap localhost
			depois verifique as portas abertas

Downloads

	Placa mãe
		http://www.huananzhi.com/html/1//184/185/551.html?view=drivers#anchor
		https://askubuntu.com/questions/899420/no-sound-ubuntu-16-04-lts
		Driver de audio
			Realtek High definition audio driver R2.76
			Realtek High definition audio driver (4.23) R2.76

			Modelo:
				Realtek ALC662
				Alc662 5.1 soundtrack 
			Comandos linux:
				alsamixer
				pavucontrol

	--'verificar antes Python 3 '
		Criação de ambiente virtual no Python 3
			sudo apt install -y python3-venv
			https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server-pt
		How to install Flat-Remix Theme on Any Linux Distribution? 
			Exibição de outra interface grafica do linux 

	Sublime-text3
		https://www.sublimetext.com/docs/3/linux_repositories.html
		https://www.youtube.com/watch?v=5jKdPlTqpY4
		Comandos:
			wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
			sudo apt-get install apt-transport-https
			echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
			sudo apt-get update
			sudo apt-get install sublime-text

	Driver placa de vídeo
		https://www.amd.com/pt/support/graphics/radeon-500-series/radeon-rx-500-series/radeon-rx-570
		Comandos:
			Após realizar o download
			cd ~/Downloads
			tar -xJvf amdgpu-pro-20.50-1234664-ubuntu-20.04.tar.xz
			cd amdgpu-pro-20.50-1234664-ubuntu-20.04/
			./amdgpu-pro-install -y

	Virtualbox
		sudo apt get install virtualbox
	
	Tp-Link AC600 [Archer T2U V3] (Wi-fi Wireless USB)
		sudo apt update
		sudo apt install dkms		
		sudo apt install git 
		git clone https://github.com/aircrack-ng/rtl8812au.git
		cd rtl8812au
		sudo make dkms_install
	

	Postgres
		https://www.postgresql.org/download/linux/ubuntu/
		sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
			# Create the file repository configuration:
		wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
			# Import the repository signing key:		
		sudo apt-get update
			# Update the package lists:
		sudo apt-get -y install postgresql
			# Install the latest version of PostgreSQL.
			# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
		service postgresql status
			ver se o serviço do postgresql está rodando
		Configurando o superuser postgres 
			sudo -i -u postgres 
				psql 
				\password
					trocar para usuário postgres
				\conninfo
					quem está conectado
				\l 
					lista datbases
				\q 
					sai do psql
				\du
				\c [datbases]
				\d \dS
				\!
					retorna para o terminal, escrevendo exit retorna para o postgresql
				\h  
				\?

	PGAdmin4
		https://www.digitalocean.com/community/tutorials/como-instalar-e-configurar-o-pgadmin-4-no-modo-servidor-pt#passo-5-%E2%80%94-configurando-seu-usu%C3%A1rio-do-postgresql
		https://www.youtube.com/watch?v=I0FJevUrK0E
		https://www.pgadmin.org/download/pgadmin-4-apt/
		PGAdmin4 WebBrowser
			http://127.0.0.1:53336/browser
		
	Apache2
		https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-18-04
		Verificar se já essta instalado
			systemctl status apache2
		Comandos:
			Após realizar o download
			sudo apt install apache2sudo
				sudo ufw app list
				

	Java JDK
		Direto pelo prompt
			sudo add-apt-repository ppa:openjdk-r/ppa
			sudo apt-get update
			sudo apt-get install openjdk-8-jdk
		Fazendo Download 
			Java™ Platform, Standard Edition Development Kit (JDK™).
			https://www.oracle.com/br/java/technologies/javase/javase-jdk8-downloads.html
				Linux x64 Compressed Archive 
					jdk-8u281-linux-x64.tar.gz
		Obs.:
			Não tem instalador para o Java JDK, depois de descompactar basta mover o diretório para 
			Por padrão mover para a pasta /opt/jdk
				Comando:
					tar -xvf jdk-8u281-linux-x64.tar.gz
					sudo mv jdk-8u281-linux-x64 /opt/jdk
				Adicionar no ~/ .bashrc as seguintes variáveis de ambiente
					# JDK
					export JAVA_HOME=/opt/jdk
					export PATH=$JAVA_HOME/bin:$PATH
		ou por repositório
			Versão 8
				sudo apt install openjdk-8-jre-headless
			Versão 13
				sudo apt install openjdk-13-jre-headless
			Versão 14
				sudo apt install openjdk-14-jre-headless
		javac -version
		java -version
	Apache TomCat
		Realizar o download do Core .zip no site do Apache TomCat
			https://tomcat.apache.org/download-10.cgi
		Extrair o arquivo e mover a pasta descompactada para o diretório /opt/
		Adicionar permissão de execução nos arquivos .sh dentro do diretório BIN 
			sudo chmod +x *.sh
		Startar o serviço do Apache TomCat
			sudo ./startup.sh
		Para confirmar digite no browser:
			localhost:8080
			ou no terminal
				sudo service apache2 status
	Anaconda IDE
		https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-20-04-pt
		https://docs.anaconda.com/anaconda/install/linux/
		https://www.anaconda.com/products/individual#linux
		Prerequisitos
			apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
		Comandos:
			Após realizar o download
			bash ~/Downloads/Anaconda3-2020.02-Linux-x86_64.sh
		Erros
			python não ativado (Quando coloca python no shell não mostra a vesão do python que o Anaconda está usando)
				https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-20-04-pt
		Comands - Anaconda
			conda info --envs
				Você pode inspecionar todos os ambientes que você configurou
					o sina de ' * ' indica o ambiente ativo no momento
			conda upadate conda
				Atualiza o Anaconda com as versões mais recentes dos pacotes
				conda upadate anaconda
					Assim que a atualização do conda estiver concluída, pode atualizar a distribuição do Anaconda3-2020
					Garantia de utilização da Versão mais recente do conda e do Anaconda
			conda activate [nome da variável Ex: my_env]
				Para ativar a variavel de ambiente desejada
			conda deactivate
				Para desativar a variavel de ambiente
		prompt
			jupyter notebook
				abre o jupyter notebook no browser


	Spark Apache
		https://spark.apache.org/downloads.html
		https://www.apache.org/dyn/closer.lua/spark/spark-2.4.7/spark-2.4.7-bin-hadoop2.7.tgz
		Obs.:
			O Apache Spark foi desenvolvido em linguagem SCALA e roda em cima da linguagem Java.
			O Apache Spark não vem com o Hadoop. Foi preparado para rodar no sistema de arquivos distribuido do Hadoop que é o HDFS  
			Não tem instalador igual ao Java, depois de descompactar basta mover o diretório para 
				Por padrão mover para a pasta /opt/jdk
				Comando:
					tar -xvf 
					sudo mv spark-2.4.7-bin-hadoop2.7 /opt/spark
				Adicionar no ~/ .bashrc as seguintes variáveis de ambiente
					# Spark
					export SPARK_HOME=/opt/spark
					export PATH=$SPARK_HOME/bin:$PATH
					#Utiliza o Spark via browser e não por linha de comando
					export PYSPARK_DRIVER_PYTHON=jupyter
					export PYSPARK_DRIVER_PYTHON_OPTS=notebook

	Eclipse IDE
		https://sempreupdate.com.br/como-instalar-o-eclipse-no-ubuntu/
		criar diretório para colocar o eclipsena área de trabalho do Ubuntu
			sudo vi usr/share/applications/eclipse.desktop 
			inserir essas informações no arquivo criado
				[Desktop Entry]
				Name=Eclipse
				Type=Application
				Exec=/home/lucas/eclipse/java-2021-03/eclipse/eclipse
				Icon=/home/lucas/eclipse/java-2021-03/eclipse/icon.xpm
				Terminal=false
				Comment=Eclipse IDE
				Categories=IDE;Application;Development;


	ToolBox JetBrains
		https://www.jetbrains.com/pt-br/toolbox-app/
			Obser var os prerequisitos na opção de download
				https://github.com/AppImage/AppImageKit/wiki/FUSE

	GitHub 
		já vem instalado nas novas versões do linux
			digitar git no prompt
		caso contrário 
			https://git-scm.com/download/linux
	R no Ubuntu 20.04
		links
			http://leg.ufpr.br/~fernandomayer/aulas/ce083-2016-2/R-instalacao.html
			https://www.digitalocean.com/community/tutorials/how-to-install-r-on-ubuntu-20-04-pt
		Forma recomendada
			$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
				adicionar a chave GPG relevante.
			$ sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'
				Adicionar o repositório do R CRAN
				Nome da partição linux Ubuntu
					Focal Fossa (20.04; LTS and amd64 only)
					no R o Ubuntu 20.04 é conhecido como Focal Fossa
			$ sudo su
			$ cd /usr/local/src  
			$ sudo wget https://cran.r-project.org/src/base/R-4/R-4.1.1.tar.gz
				Repositório oficial de outras instalções do R 
					https://cran.r-project.org/src/base/R-4/R-4.1.1.tar.gz
					https://cran.r-project.org/src/base/R-3/R-3.6.3.tar.gz
			$ tar zxvf R-4.1.1.tar.gz
			$ cd R-4.1.1
			$ ./configure 
				não usar ./configure --enable-R-shlib #opcional (utiliza a interface no Linux é necessário compilar o como um shared library)
			$ make
			$ sudo make install
			$ sudo make install-info
			$ sudo make install-pdf
			$ cd ..
			$ rm -rf R-4.1.1*
			$ exit
			$ cd
		Forma prática
			sudo apt install r-base-core
		Adicionar repository do CRAN Packages do R 4.0 ou superior
			sudo add-apt-repository ppa:c2d4u.team/c2d4u4.0+
	RStudio
		Realizar o download
			https://www.rstudio.com/products/rstudio/download/#download
		sudo apt update
		sudo apt install ./rstudio-1.4.1717-amd64.deb
		Remover instalaçao
			sudo apt-get remove rstudio
			sudo apt-get remove r-base-core
		Pacotes R  
			install.packages("readxl")
	
export PATH=~/anaconda3/bin:$PATH
pyspark 

export PYSPARK_DRIVER_PYTHON
export PYSPARK_DRIVER_PYTHON_OPTS
exec "${SPARK_HOME}"/bin/spark-submit pyspark-shell-main --name "PySparkShell" "$@"


jupyter



plot(ecdf(hh$HDI)); grid()

Para faze o download das video aulas  
plugin do chorme
	vido download plus
	zoom record downloadr
quando tenta baixar da um pau  
	mas é so voltar para a pagina e rodar de novo
R