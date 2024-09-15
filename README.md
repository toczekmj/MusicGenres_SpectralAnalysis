<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" />
</p>
<p align="center">
    <h1 align="center">Spectral Analysis</h1>
</p>
<p align="center">
    <em><code>► University project</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/license-GNU AGPLv3.0-green" alt="license">
	<img src="https://img.shields.io/github/last-commit/toczekmj/MusicGenres_SpectralAnalysis?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/toczekmj/MusicGenres_SpectralAnalysis?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/toczekmj/MusicGenres_SpectralAnalysis?style=flat&color=0080ff" alt="repo-language-count">
<p>

<hr>

## Credits 
Please note that Music.ipynb and MuscGenresShaderPlot are NOT created by me. 
All the credits belongs to their authors:
- MusicGenresShaderPlot created by [Adam Migdalski](https://www.facebook.com/metix558)
- Music.ipynb created by [Dawid Pałka](https://www.linkedin.com/in/dawid-pa%C5%82ka-1525b0270/)

##  Quick Links

> - [ Overview](#overview)
> - [ Features](#features)
> - [ Repository Structure](#repository-structure)
> - [ Modules](#modules)
> - [ Getting Started](#getting-started)
>   - [ Installation](#installation)
>   - [ Running MusicGenres_SpectralAnalysis](#running-SpectralAnalysis)
> - [ Contributing](#contributing)
> - [ License](#license)
> - [ Acknowledgments](#acknowledgments)

---

## Overview

The goal of this project was to prove that we can differentiate music genres, based only on frequencies, or average 
frequencies of the music files. Previously we thought about analyzing plots and drawing conclusions, but as we went down the 
rabbithole, we thought that no brain is better in analyzing numbers, than AI brain.

--- 
## Features
There are three main modules of this app, namely 
- music downloader 
- analyzer
- csv exporter

First of all, we need to gather data, and since there is no better source than youtube, we decided to go this way. 
Secondly, after downloading tons of data, we need to process them, and the processed data are written to csv files. 


### Misc
There are three additional misc scripts, that were not ment to help us automate the proces. 
They are designed to get some particular data, from already processed files, for some particular purposes, and we run them when needed.
- mergeCSV - as the name suggests it merges all CSV files in given folder into one .csv file, which is later given to feed the model
- genresaverage - traverse all folders in given path, that ends with CSV (because that's how our main script creates the folder tree) and averages the valeus 
---
##  Repository Structure

```sh
└── MusicGenres_SpectralAnalysis/
    ├── Libraries
    │   ├── CvsExport.py
    │   ├── FftPreparation.py
    │   ├── GraphPloter.py
    │   ├── PlaylistDownloder.py
    │   └── SoundAnalyzer.py
    ├── README.md
    ├── SampleModel
    │   ├── model.py
    │   └── predict.py
    ├── main.py
    └── misc
        ├── MergeCSV.py
        └── genresaverage.py
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                    | Summary                                                   |
| ---                                                                                     |-----------------------------------------------------------|
| [main.py](https://github.com/toczekmj/MusicGenres_SpectralAnalysis/blob/master/main.py) | <code>► Main app, used to gather and process data.</code> |

</details>

<details closed><summary>misc</summary>

| File                                                                                                                       | Summary                                                                                                                   |
| ---                                                                                                                        |---------------------------------------------------------------------------------------------------------------------------|
| [genresaverage.py](https://github.com/toczekmj/MusicGenres_SpectralAnalysis/blob/master/misc/genresaverage.py)             | <code>► Calculates average from one of the genres. <br/>It operates on already generated .csv files, not on mp3's.</code> |
| [MergeCSV.py](https://github.com/toczekmj/MusicGenres_SpectralAnalysis/blob/master/misc/MergeCSV.py)                       | <code>► It meregs .csv files for later usage in ML.</code>                                                                |

</details>

<details closed><summary>Libraries</summary>

| File                                                                                                                        | Summary                                                   |
| ---                                                                                                                         |-----------------------------------------------------------|
| [SoundAnalyzer.py](https://github.com/toczekmj/MusicGenres_SpectralAnalysis/blob/master/Libraries/SoundAnalyzer.py)         | <code>► Load songs, and preform Fourier transform.</code> |
| [FftPreparation.py](https://github.com/toczekmj/MusicGenres_SpectralAnalysis/blob/master/Libraries/FftPreparation.py)       | <code>► Prepare data to Fourier Transform.</code>         |
| [GraphPloter.py](https://github.com/toczekmj/MusicGenres_SpectralAnalysis/blob/master/Libraries/GraphPloter.py)             | <code>► Plot graphs using matplotlib.</code>              |
| [PlaylistDownloder.py](https://github.com/toczekmj/MusicGenres_SpectralAnalysis/blob/master/Libraries/PlaylistDownloder.py) | <code>► Download files from youtube.</code>               |
| [CvsExport.py](https://github.com/toczekmj/MusicGenres_SpectralAnalysis/blob/master/Libraries/CvsExport.py)                 | <code>► Exports data into .csv files.</code>              |

</details>

<details closed><summary>Sample Model</summary>

| File                                                                                                      | Summary                                                                                                     |
| ---                                                                                                        |-------------------------------------------------------------------------------------------------------------|
| [model.py](https://github.com/toczekmj/MusicGenres_SpectralAnalysis/blob/master/SampleModel/model.py)     | <code>► WARNING - FULLY AI GENERATED CONTENT<br/> Creates model which can recognise music genres.</code>    |
| [predict.py](https://github.com/toczekmj/MusicGenres_SpectralAnalysis/blob/master/SampleModel/predict.py) | <code>► WARNING - FULLY AI GENERATED CONTENT<br/> Uses previously created model to recognise genres.</code> |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version 3.12`
* **FFMPEG** `installed and added into PATH`

###  Installation

1. Clone the MusicGenres_SpectralAnalysis repository:

```sh
git clone https://github.com/toczekmj/MusicGenres_SpectralAnalysis
```

2. Change to the project directory:

```sh
cd MusicGenres_SpectralAnalysis
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

###  Running SpectralAnalysis

Use the following command to run SpectralAnalysis:

```sh
Downloading single video:
python main.py -g "genre name" -u "url to yt single video" 

Downloading whole playlist:
python main.py -g "genre name" -p -u "url to yt playlist"

Options: 
-g or --genre -> determines folder where downloaded files are stored
-u or --url -> url to youtube playlist or video
-p or --playlist -> add this when you provided link to a playlist insted of single video in previous step
-d or --delete -> if folder with identical name exists it is deleted before the download starts 
```


---


##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/toczekmj/MusicGenres_SpectralAnalysis/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/toczekmj/MusicGenres_SpectralAnalysis/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/toczekmj/MusicGenres_SpectralAnalysis/issues)**: Submit bugs found or log feature requests for Musicgenres_spectralanalysis.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/toczekmj/MusicGenres_SpectralAnalysis
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  License

This project is protected under the [GNU AGPLv3.0](https://choosealicense.com/licenses/agpl-3.0/#) License. 
For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

Please keep in mind, that this repo consists 3 different projects. 
- Music.ipynb
- MusicGenresSharedPlot
- SpectralAnalysis

In order to use any other part than SpectralAnalysis please contact with author of the projec (listed at the top of this file).

[**Return**](#-quick-links)

---
