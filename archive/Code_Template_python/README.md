# NLP Project – Python Template

This repository contains the Python implementation of the NLP class algorithms
---

## 📦 Setup Instructions

### 1. Install miniconda

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
```

Run the installer:

```bash
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```

Initialize Miniconda (only first time):

```bash 
source ~/miniconda3/bin/activate
conda init 
```
### 2. Create a Conda Environment

Make sure you have [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed.

```bash
conda create -n nlp_env python=3.10 -y
conda activate nlp_env
```