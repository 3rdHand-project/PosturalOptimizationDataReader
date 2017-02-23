#!/bin/bash
mkdir -p results
if [ ! -d "results/user_study_dataset" ]; then
	cd results
	echo "Downloading result files"
	wget https://zenodo.org/record/321599/files/user_study_dataset.zip
	unzip user_study_dataset.zip
	rm user_study_dataset.zip
	cd ..
fi


mkdir -p bin
if [ ! -d "bin/ReplayInterfaceLinux" ]; then
	cd bin
	echo "Downloading graphical interface binary"
	wget https://github.com/3rdHand-project/PosturalOptimizationDataReader/releases/download/v1.0/ReplayInterfaceLinux.tar.gz
	tar -xvzf ReplayInterfaceLinux.tar.gz
	rm ReplayInterfaceLinux.tar.gz
	cd ..
fi