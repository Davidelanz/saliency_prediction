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


|Input || Deep Gaze II | || ICF | |
|---|---|---|---|---|---|---|
|![](./test_imgs/degas-ballet-class.jpg)||![](./deep_gaze_2_example/degas-ballet-class_prediction.png)|![](./deep_gaze_2_example/degas-ballet-class_density.png)||![](./ICF_example/degas-ballet-class_prediction.png)|![](./ICF_example/degas-ballet-class_density.png)|
|![](./test_imgs/degas-dancer.jpg)||![](./deep_gaze_2_example/degas-dancer_prediction.png)|![](./deep_gaze_2_example/degas-dancer_density.png)||![](./ICF_example/degas-dancer_prediction.png)|![](./ICF_example/degas-dancer_density.png)|
|![](./test_imgs/eagles.jpg)||![](./deep_gaze_2_example/eagles_prediction.png)|![](./deep_gaze_2_example/eagles_density.png)||![](./ICF_example/eagles_prediction.png)|![](./ICF_example/eagles_density.png)|
|![](./test_imgs/ihme_zentrum.jpg)||![](./deep_gaze_2_example/ihme_zentrum_prediction.png)|![](./deep_gaze_2_example/ihme_zentrum_density.png)||![](./ICF_example/ihme_zentrum_prediction.png)|![](./ICF_example/ihme_zentrum_density.png)|

