#!/bin/bash
mkdir -p results
if [ ! -d "results/user_study_dataset" ]; then
	cd results
	echo "Downloading result files."
	wget https://zenodo.org/record/321599/files/user_study_dataset.zip
	echo "Extracting result files, please wait"
	unzip -q user_study_dataset.zip
	rm user_study_dataset.zip
	cd ..
fi


mkdir -p bin
if [ "$(uname)" = "Linux" ] && [ ! -d "bin/ReplayInterfaceLinux" ]; then
	cd bin
	echo "Downloading graphical interface binary for Linux system"
	wget https://github.com/3rdHand-project/PosturalOptimizationDataReader/releases/download/v1.0/ReplayInterfaceLinux.tar.gz
	tar -xzf ReplayInterfaceLinux.tar.gz
	rm ReplayInterfaceLinux.tar.gz
	cd ..
elif [ "$(uname)" = "Darwin" ] && [ ! -d "bin/ReplayInterfaceMac" ]; then
	cd bin
	echo "Downloading graphical interface binary for Mac system"
	wget https://github.com/3rdHand-project/PosturalOptimizationDataReader/releases/download/v1.0/ReplayInterfaceMac.tar.gz
	tar -xzf ReplayInterfaceMac.tar.gz
	rm ReplayInterfaceMac.tar.gz
	cd ..
fi