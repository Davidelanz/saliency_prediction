# Deep Gaze 2 & ICF - Saliency Prediction

> **Copyright Disclaimer**: the following code is adapted from https://deepgaze.bethgelab.org/ 
> © Copyright 2016 by [Matthias Kümmerer](http://www.bethgelab.org/).

## Getting started

### Requirements

- Docker image:
    ```
    docker pull tensorflow/tensorflow
    ```
- Python 3.6 + Tensorflow
- Python requirements: see ``requirements.txt``

### Tutorials
- `Demo.ipynb` 
- `CreateCenterbias.ipynb`

## Results


|Input | Deep Gaze II | | ICF | |
|---|---|---|---|---|
|<img src="./test_imgs/degas-ballet-class.jpg" width="100px"/>|<img src="./deep_gaze_2_example/degas-ballet-class_prediction.png" width="100px"/>|<img src="./deep_gaze_2_example/degas-ballet-class_density.png" width="100px"/>|<img src="./ICF_example/degas-ballet-class_prediction.png" width="100px"/>|<img src="./ICF_example/degas-ballet-class_density.png" width="100px"/>|
