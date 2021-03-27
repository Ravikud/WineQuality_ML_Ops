create env
```bash
conda create -n winequal python=3.7 -y
```
activate env
```bash
activate winequal
```
create requirements.txt & install it
```bash
pip install -r requirements.txt
```
```bash
download the wine.csv from kaggle
```
```bash
git init
```
```bash
dvc init
```
```bash
dvc add data_given/wine.csv
```
```bash
git add .
```
```bash
git commit -m "Initial Commit"
```
```bash
git branch -M main
```
```bash
git remote add origin https://github.com/Ravikud/WineQuality_ML_Ops.git
```
```bash
git push -u origin main
```
tox command -
```bash
tox
```
pytest command -
```bash
pytest -v
```
Build your own package commands -
```bash
python setup.py install.
```
