#!/usr/bin/env bash

# Colours
declare -r greenColour="\e[0;32m\033[1m"
declare -r endColour="\033[0m\e[0m"
declare -r redColour="\e[0;31m\033[1m"
declare -r blueColour="\e[0;34m\033[1m"
declare -r yellowColour="\e[0;33m\033[1m"
declare -r purpleColour="\e[0;35m\033[1m"
declare -r turquoiseColour="\e[0;36m\033[1m"
declare -r grayColour="\e[0;37m\033[1m"

# Variables globales
declare -a dependencies=(python3 git tput build-essential python3-dev libssl-dev libffi-dev sqlite3)

# Variables globales de buildbot
declare -r buildbot_master_dir="master"
declare -r buildbot_worker_dir="worker"
declare -r buildbot_environ="source"


# Trap del Ctrl_C
trap ctrl_c INT
function ctrl_c(){
	echo -e "${redColour}[ERROR]${endColour} ${yellowColour}Saliendo...${endColour}"
	tput cnorm
	exit 1
}

# Instalamos las dependencias
function install_dependencies(){
	echo -e "${yellowColour}[+]${endColour} ${grayColour}Checking dependencies...${endColour}"
	echo -e "${dependencies[@]}\n"
	for prog in ${dependencies[@]}; do
		if ! command -v $prog > /dev/null 2>&1; then
			echo -e "${yellowColour}[-]${endColour} ${grayColour}Tool:${endColour} ${blueColour}$prog${endColour}"
			apt-get install -y $prog &> /dev/null
		fi
		sleep 1
	done
}


## ===> Buildbot master
function buildbot_master(){
	echo -e "\n${yellowColour}[*]${endColour} ${grayColour}Generating master node...${endColour}"
	source "$buildbot_environ/bin/activate"
	echo -e "\n${purpleColour}[+]${endColour} ${grayColour}Installing${endColour} ${blueColour}buildbot${endColour}${grayColour}...${endColour}"
	pip install --upgrade pip
	pip install 'buildbot[bundle]'
	echo -e "\n${purpleColour}[+]${endColour} ${grayColour}Starting buildbot master node...${endColour}"
	buildbot start $buildbot_master_dir
	if [ $? -ne 0 ]; then echo -e "\n${redColour}[ERROR]${endColour} ${yellowColour}Cannot startup buildbot $buildbot_master_dir${endColour}\n"; exit 1; fi
}

## ===> Buildbot worker
function buildbot_worker(){
	echo -e "\n${yellowColour}[*]${endColour} ${grayColour}Generating worker node...${endColour}"
	# source "$buildbot_environ/bin/activate"
	echo -e "\n${purpleColour}[+]${endColour} ${grayColour}Installing${endColour} ${blueColour}buildbot-worker${endColour} ${grayColour}and${endColour} ${blueColour}setuptools-trial${endColour}${grayColour}...${endColour}"
	pip install --upgrade pip
	pip install buildbot-worker setuptools-trial
	echo -e "\n${purpleColour}[+]${endColour} ${grayColour}Starting buildbot worker node...${endColour}"
	buildbot-worker start $buildbot_worker_dir
	if [ $? -ne 0 ]; then echo -e "\n${redColour}[ERROR]${endColour} ${yellowColour}Cannot startup buildbot-worker $buildbot_worker_dir${endColour}\n"; exit 1; fi
}

# Programa principal
tput civis
install_dependencies
buildbot_master
buildbot_worker
tput cnorm
