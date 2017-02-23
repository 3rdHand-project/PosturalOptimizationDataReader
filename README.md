# Postural Optimization Data Reader

This repository contains all the necessary materials to replay and/or reuse the data collected during the experiment made in the context of the publication Postural Optimization for a Safe and Comfortable Human-Robot Interaction.

The first necessary step is to download the data that are published on a [Zenodo repository](https://zenodo.org/record/321599) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.321599.svg)](https://doi.org/10.5281/zenodo.321599)

At the project root you can create the results folder and unzip the data folder inside it.
If you are on Linux you can also directly use the script [get_results_data.sh](get_results_data.sh) that will perform the necessary steps.

```
chmod +x get_results_data.sh && ./get_results_data.sh
```

Several scripts to analyze the data are available in the [scripts](scripts) folder.
Especially, the script [replay_data](scripts/replay_data) will read the replay files for a specific user.
You can run it by specifying the user id (name of folder in the results file) as parameter.
For example, to replay the data of user 17 run:

```
python replay_data 17
```

The recorded data are made to be viewed with the [graphical interface](https://github.com/3rdHand-project/PosturalFeedbackInterface) we have developped.
In this repository we have [realeased](https://github.com/3rdHand-project/PosturalOptimizationDataReader/releases/latest) the executables of a modified version of the interface adapted for replaying recorded data.
Download the executable depending on your OS and extract the archive.
We recommand you to extract it in a bin folder.
After extraction you can run the executable and follow the instructions on screen.

For Windows user run:
```
ReplayInterface.exe
```

For Linux user run:
```
./ReplayInterface.x86_64
```

For more information on the graphical interface, please refer to its [own repository](https://github.com/3rdHand-project/PosturalFeedbackInterface)
