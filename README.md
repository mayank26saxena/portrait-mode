# Portrait Mode
This project implements the portrait mode effect on images using Neural Networks.

## How it works?
Traditionally, the portrait mode effect has been achieved using 2 lenses which detect ojects present in the foreground and in the background.
With advances in the field of ML, this effect can also be implemented using only image segmentation. Using the pretrained [DeepLab-v3+](https://github.com/tensorflow/models/tree/master/research/deeplab) open source model, we can find the objects in the foreground of the image and blur the background to replicate this effect.

Check out the demo website - [Demo](http://portraitmode.herokuapp.com/) (Source Code: [https://github.com/mudit9/portraitmode-flask](https://github.com/mudit9/portraitmode-flask))


## Setup
This project relies on a handful of dependencies, use the following command to install your dependencies:

```shell
pip install -r requirements.txt
```

_Note_: Depending on your environment, you may need to use `sudo`. You may also want to use virtualenv.

## Usage

Portrait Mode Effect is used from the command line:

```shell
python portrait-mode.py -i samples/input-1.jpg
```

`-i/--image`: specifies the image file.

The script outputs one image in the same directory with the name: `input-1-portrait.jpg` 

## Examples

```shell
python portrait-mode.py -i samples/input-1.jpg
```

<img src="samples/input-1.jpg" width="425"/> <img src="samples/input-1-portrait.jpg" width="425"/> 

```shell
python portrait-mode.py -i samples/input-2.jpg
```

<img src="samples/input-2.jpg" width="425"/> <img src="samples/input-2-portrait.jpg" width="425"/> 

```shell
python portrait-mode.py -i samples/input-3.jpg
```

<img src="samples/input-3.jpg" width="425"/> <img src="samples/input-3-portrait.jpg" width="425"/> 


## To Do
- [ ] Develop API.
- [ ] Develop website.

## Developers
This project has been developed by:
- [Mudit Saxena](https://github.com/mudit9): [https://github.com/mudit9/portraitmode-flask](https://github.com/mudit9/portraitmode-flask)
- [Mayank Saxena](https://github.com/mayank26saxena)

## License
MIT License - see the [LICENSE](https://github.com/mayank26saxena/portrait-mode/blob/master/LICENSE) file for details.

## Credits
1) [https://ai.googleblog.com/2018/03/semantic-image-segmentation-with.html](https://ai.googleblog.com/2018/03/semantic-image-segmentation-with.html)
2) [https://github.com/tensorflow/models/tree/master/research/deeplab](https://github.com/tensorflow/models/tree/master/research/deeplab)
3) [https://github.com/minimaxir/person-blocker](https://github.com/minimaxir/person-blocker)
