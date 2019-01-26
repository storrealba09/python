# Python

This is a framework for a basic python project. Clone  whenever you're ready to start a fresh python3 project.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
python3.7
node v10.15.0
```

### Installing

A step by step series of examples that tell you how to get a development env running

Step 1 - Install Python3.7
```
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
tar -xzf Python-3.7.2.tgz
cd Python-3.7.2
yum -y install openssl-devel zlib libffi-devel
yum -y install python37-devel
./configure
make
make altinstall
git clone git@github.com:DevManTillis/python.git 
cd python/
pip install -r python/requirements.txt
```

Step 2 - Install nodejs (optional)
```
sudo /python/sample/python-nodejs/node_setup
npm -i python-shell
```

Step 3 - Configure VIM as an IDE
```
cp python/vimrc ~/.vimrc
mkdir -p ~/.vim/syntax/
cp python/python.vim !/.vim/syntax/
```

Example:
```
python/sample/python/script.py
```

## Running the tests
```
pytest python/tests/test_basic.py
```

## Authors

* **Miguel Tillis Jr.** - *Initial work* - [Tillis IT Automation](https://tillisautomation.com)

## License

This project is licensed under the Apace License - see the [LICENSE.md](LICENSE.md) file for details
