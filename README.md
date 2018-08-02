# Wordnet, Verbnet, Framenet, and Propbank to Datum Universe

Using DatumTron Python API, a datum universe of wordnet, verbnet, framenet and propbank is generated

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

Get Wordnet, Verbnet, Framenet and Propbank python API
Download and install nltk from:

```
https://pypi.python.org/pypi/nltk
```

### Installing

Open the Command prompt and change directory to the current folder
Then type the following commands in turn:
```
python wordnet.py
python wordnet-hyponyms.py
python wordnet-topicdomains.py
python wordnet-addinglemmas.py
python wordnet-addinghas.py
python wordnet-addingSister.py
python verbnet.py
python framenet.py
python framenet-addingframerelations.py
python framenet-frameelements.py
python framenet-semantictype.py
python framenet-semtypesFELU.py
python propbank.py
python framenet-wordnet-linker.py
```

This will generate a datum universe in a file called:

```
wordnet-verbnet-framenet-propbank-linked.datum
```


## Testing

Using the DUV open wordnet-verbnet-framenet-propbank.datum, the file should be opened correctly and should have all data from these lexicons

## Built With

* [Datumtron](http://www.datumtron.com/) - The Datumtron API used

## Authors

* **Mohamed Wahballah** - *Initial work* - [mawahballah](https://github.com/mawahballah)
