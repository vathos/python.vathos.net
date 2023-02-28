# Vathos Python

## Installation

### Dependencies

- [Python](https://www.python.org/) version 3.8 or higher
- [requests](https://requests.readthedocs.io/en/latest/)
- [numpy](https://numpy.org/)
- [mayavi](https://docs.enthought.com/mayavi/mayavi/) (optional for 3d visualization) 

### Build from source

To get a nightly build, first, clone this repository:

```bash
git clone https://github.com/vathos/python.vathos.net.git
```

Then, build the Python wheel:

```bash
./setup build bdist_wheel
```

The result is put in the subfolder `./dist`. Install it with the following command:

```bash
pip install ./dist/vathos-0.0.0_latest-py3-none-any.whl
```

### Installation with pip

The latest official version of the library is available on PyPi and can be installed by calling

```bash
pip install vathos
```

## Quick start

[Get in touch with us](https://www.vathos-robotics.com) to receive a test account. Make sure your client id and secret are exported to the two eponymous environment varibales `CLIENT_ID` and `CLIENT_SECRET`. Now you are ready to run the examples in the [demos folder](./demos/).

## Further reading

- [API documentation](./docs/)
- [Developers Guide](https://docs.vathos.net/guides)