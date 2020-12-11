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
|<img src="./test_imgs/degas-ballet-class.jpg" width="1000px"/>|<img src="./deep_gaze_2_example/degas-ballet-class_prediction.png" width="1000px"/>|<img src="./deep_gaze_2_example/degas-ballet-class_density.png" width="1000px"/>|<img src="./icf_example/degas-ballet-class_prediction.png" width="1000px"/>|<img src="./icf_example/degas-ballet-class_density.png" width="1000px"/>|
|<img src="./test_imgs/degas-dancer.jpg" width="1000px"/>|<img src="./deep_gaze_2_example/degas-dancer_prediction.png" width="1000px"/>|<img src="./deep_gaze_2_example/degas-dancer_density.png" width="1000px"/>|<img src="./icf_example/degas-dancer_prediction.png" width="1000px"/>|<img src="./icf_example/degas-dancer_density.png" width="1000px"/>|
|<img src="./test_imgs/eagles.jpg" width="1000px"/>|<img src="./deep_gaze_2_example/eagles_prediction.png" width="1000px"/>|<img src="./deep_gaze_2_example/eagles_density.png" width="1000px"/>|<img src="./icf_example/eagles_prediction.png" width="1000px"/>|<img src="./icf_example/eagles_density.png" width="1000px"/>|
|<img src="./test_imgs/ihme_zentrum.jpg" width="1000px"/>|<img src="./deep_gaze_2_example/ihme_zentrum_prediction.png" width="1000px"/>|<img src="./deep_gaze_2_example/ihme_zentrum_density.png" width="1000px"/>|<img src="./icf_example/ihme_zentrum_prediction.png" width="1000px"/>|<img src="./icf_example/ihme_zentrum_density.png" width="1000px"/>|
|<img src="./test_imgs/moca-chirico-hero.jpg" width="1000px"/>|<img src="./deep_gaze_2_example/moca-chirico-hero_prediction.png" width="1000px"/>|<img src="./deep_gaze_2_example/moca-chirico-hero_density.png" width="1000px"/>|<img src="./icf_example/moca-chirico-hero_prediction.png" width="1000px"/>|<img src="./icf_example/moca-chirico-hero_density.png" width="1000px"/>|
|<img src="./test_imgs/nord_lb.jpg" width="1000px"/>|<img src="./deep_gaze_2_example/nord_lb_prediction.png" width="1000px"/>|<img src="./deep_gaze_2_example/nord_lb_density.png" width="1000px"/>|<img src="./icf_example/nord_lb_prediction.png" width="1000px"/>|<img src="./icf_example/nord_lb_density.png" width="1000px"/>|
|<img src="./test_imgs/santelia-citta-nuova.jpg" width="1000px"/>|<img src="./deep_gaze_2_example/santelia-citta-nuova_prediction.png" width="1000px"/>|<img src="./deep_gaze_2_example/santelia-citta-nuova_density.png" width="1000px"/>|<img src="./icf_example/santelia-citta-nuova_prediction.png" width="1000px"/>|<img src="./icf_example/santelia-citta-nuova_density.png" width="1000px"/>|
|<img src="./test_imgs/uni_hannover_lichthof.jpg" width="1000px"/>|<img src="./deep_gaze_2_example/uni_hannover_lichthof_prediction.png" width="1000px"/>|<img src="./deep_gaze_2_example/uni_hannover_lichthof_density.png" width="1000px"/>|<img src="./icf_example/uni_hannover_lichthof_prediction.png" width="1000px"/>|<img src="./icf_example/uni_hannover_lichthof_density.png" width="1000px"/>|
|<img src="./test_imgs/uni_hannover.jpg" width="1000px"/>|<img src="./deep_gaze_2_example/uni_hannover_prediction.png" width="1000px"/>|<img src="./deep_gaze_2_example/uni_hannover_density.png" width="1000px"/>|<img src="./icf_example/uni_hannover_prediction.png" width="1000px"/>|<img src="./icf_example/uni_hannover_density.png" width="1000px"/>|


