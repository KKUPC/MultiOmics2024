
# **R program**

## **R program installation**

### **Windows**

1. Go to the [CRAN website](https://cran.r-project.org/bin/windows/base/) and click on `Download R for Windows`.
2. Click on `base` and then on `Download R 4.1.1 for Windows`. (The version number may vary depending on the latest release.)
3. Open the downloaded file and follow the installation instructions.
4. Once the installation is complete, you can open R by searching for it in the Start menu.

### **Mac**

1. Go to the [CRAN website](https://cran.r-project.org/bin/macosx/) and click on `R-4.1.1.pkg`. (The version number may vary depending on the latest release.)
2. Open the downloaded file and follow the installation instructions.
3. Once the installation is complete, you can open R by searching for it in the Applications folder.


## **RStudio installation**

### **Windows**

1. Go to the [RStudio website](https://www.rstudio.com/products/rstudio/download/#download) and click on `Download RStudio for Windows`.
2. Click on `Download` under the `RStudio Desktop` section.
3. Open the downloaded file and follow the installation instructions.
4. Once the installation is complete, you can open RStudio by searching for it in the Start menu.

### **Mac**

1. Go to the [RStudio website](https://www.rstudio.com/products/rstudio/download/#download) and click on `Download RStudio for Mac`.
2. Click on `Download` under the `RStudio Desktop` section.
3. Open the downloaded file and follow the installation instructions.
4. Once the installation is complete, you can open RStudio by searching for it in the Applications folder.


## **R packages installation**

1. Open R or RStudio.
2. To install a package, use the `install.packages()` function. For example, to install the `ggplot2` package, run:
   ```R
   install.packages("ggplot2")
   ```
3. To load a package, use the `library()` function. For example, to load the `ggplot2` package, run:
   ```R
    library(ggplot2)
    ```
4. You can now use the installed package in your R code.

### Requuired R packages

1. metabom8
    How to install:
    Note: Please ensure that the R programming version matches the Rtool version.
    ```R
    library(devtools)
    devtools::install_github("tkimhofer/metabom8")
    ```
    or 
    ```R
    library(remotes)
    remotes::install_github("tkimhofer/metabom8")
    ```

2. dada2
    How to install:
    ```R
    if (!requireNamespace("BiocManager", quietly = TRUE))
        install.packages("BiocManager")
    BiocManager::install("dada2")
    ```
    [DADA2 installation guide](https://benjjneb.github.io/dada2/dada-installation.html)

3. phyloseq
    How to install:
    ```R
    if (!requireNamespace("BiocManager", quietly = TRUE))
        install.packages("BiocManager")
    BiocManager::install("phyloseq")
    ```
    [phyloseq installation guide](https://joey711.github.io/phyloseq/install.html)
    
4. packMBPLSDA
    How to install:
    ```R
    install.packages("packMBPLSDA")
    ```
5. o2plsda
    How to install:
    ```R
    install.packages("o2plsda")
    ```



# **Python**
## **Python installation**
We recommend using Anaconda (https://www.anaconda.com/products/individual) to install Python and manage packages. Anaconda is a free and open-source distribution of Python that includes many popular packages for data science and machine learning.

### **Windows**

1. Go to the [Anaconda website](https://www.anaconda.com/products/individual) and click on `Download`.
2. Download the Anaconda installer for Windows.
3. Open the downloaded file and follow the installation instructions.
4. Once the installation is complete, you can open Anaconda Navigator to launch Jupyter Notebook or other tools.

### **Mac**

1. Go to the [Anaconda website](https://www.anaconda.com/products/individual) and click on `Download`.
2. Download the Anaconda installer for macOS.
3. Open the downloaded file and follow the installation instructions.

## **Python packages installation**

1. Open Anaconda Navigator and launch Jupyter Notebook or JupyterLab.
2. To install a package, use the `!pip install` command in a Jupyter Notebook cell. For example, to install the `pandas` package, run:
   ```python
   !pip install pandas
   ```
3. To import a package, use the `import` statement. For example, to import the `pandas` package, run:
   ```python
    import pandas as pd
    ```



## **Install Jupyter  notebook in python using pip (optional)**
python
```python
!pip install jupyter
```

## **Install Jupyter  notebook in python using conda (optional)**
python
```python
!conda install -c conda-forge jupyter
```

## **Install JupyterLab in python using pip (optional)**
python
```python
!pip install jupyterlab
```

## **Install JupyterLab in python using conda (optional)**
python
```python
!conda install -c conda-forge jupyterlab
```

# **Chenomx**
## **Chenomx installation**

1. Go to the [Chenomx website](https://www.chenomx.com/) and click on `Download`.
2. Download the Chenomx installer for Windows or macOS.
3. Open the downloaded file and follow the installation instructions.
4. Once the installation is complete, you can open Chenomx to analyze NMR spectroscopy data.



# **MaxQuant**
## **MaxQuant installation**

1. Go to the [MaxQuant website](https://www.maxquant.org/) and click on `Download`.
2. Download the MaxQuant installer for Windows or macOS.
3. Open the downloaded file and follow the installation instructions.
4. Once the installation is complete, you can open MaxQuant to analyze mass spectrometry data.

Note: MaxQuant is a Windows-based software, but it can be run on macOS using virtualization software like Parallels Desktop or Boot Camp.
[Installation guide](https://www.maxquant.org/static/main/pdf/net7_MQ_installation.pdf)

