# WGen
This is an implementation of algorithm similar to the [diamond-square](https://en.wikipedia.org/wiki/Diamond-square_algorithm) algorithm, that can generate natural-looking heightmaps.

## Installation
You can download this repo and then install required libraries by running this command in the project directory:
```
pip3 install -r requirements.txt
```

## Usage
To generate new image, run this command in project directory:
```
python generate.py [iterations] [smoothness]
```
* `iterations` - number of iterations. After each iteration image size is roughly doubled.
* `smoothness` - smoothing factor. The bigger it is, the smoother the end picture.

After running this command, the `generated.png` file should appear in the working directory.

## Examples
* `python generate.py 10 1.5` - generates 1025x1025 image.

![](https://i.imgur.com/uBb7gV0.png)

* `python generate.py 10 10`

![](https://i.imgur.com/9EGmbzU.png)

* `python generate.py 10 0.9`

![](https://i.imgur.com/RKdO7Yf.png)

## License
[MIT](https://choosealicense.com/licenses/mit/)
