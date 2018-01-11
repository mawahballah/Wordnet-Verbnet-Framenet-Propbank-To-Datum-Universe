# Wordnet to Datum Universe

Using DatumTron Python API, a datum universe of wordnet is generated

## Getting Started

Download the files in this repository

### Prerequisites

Python 2.7 must be installed

```
https://www.python.org/downloads/
```

After installing Python, there is a package required to run PyDatumTron. To install open Command Prompt and type:

```
pip install pythonnet
```

Make sure that clr package is not installed. To do so open the Command Prompt and type:

```
pip uninstall clr
```

Get Wordnet python API
Download and install nltk from:

```
https://pypi.python.org/pypi/nltk
```

### Installing

Open the Command prompt and change directory to the folder called “wordnet-datum”
Then type:
```
python wordnetgenerator.py
```

This will generate a datum universe in a file called:

```
wordnet.datum
```


## Testing

Using the DUV open wordnet.datum, the file should be opened correctly and should have all data from wordnet

## Built With

* [Datumtron](http://www.datumtron.com/) - The Datumtron API used

## Authors

* **Mohamed Wahballah** - *Initial work* - [mawahballah](https://github.com/mawahballah)
