import glob
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import image
from scipy.ndimage import zoom
from scipy.special import logsumexp
# Disable tensorflow 2.0 (DeepGazeII supports Tensorflow1)
from tensorflow.compat import v1 as tf


def load_centerbias(npy_file):
    # load precomputed log density over a 1024x1024 image
    centerbias_template = np.load(npy_file)
    # rescale to match image size
    centerbias = zoom(centerbias_template,
                      (img.shape[0]/1024, img.shape[1]/1024), order=0, mode='nearest')
    # renormalize log density
    centerbias -= logsumexp(centerbias)
    return centerbias


def process_img(img: np.array, centerbias: np.array, check_point: str):

    # BHWC, three channels (RGB)
    image_data = \
        img[np.newaxis, :, :, :]

    # BHWC, 1 channel (log density)
    centerbias_data = \
        centerbias[np.newaxis, :, :, np.newaxis]

    from tensorflow.python.framework import ops
    ops.reset_default_graph()

    # Load checkpoint
    new_saver = tf.train.import_meta_graph('{}.meta'.format(check_point))

    input_tensor =\
        tf.get_collection('input_tensor')[0]
    centerbias_tensor = \
        tf.get_collection('centerbias_tensor')[0]
    log_density = \
        tf.get_collection('log_density')[0]
    log_density_wo_centerbias =\
        tf.get_collection('log_density_wo_centerbias')[0]

    with tf.Session() as sess:
        new_saver.restore(sess, check_point)
        log_density_prediction = sess.run(log_density, {
            input_tensor: image_data,
            centerbias_tensor: centerbias_data,
        })

    return log_density_prediction


def store_prediction(log_density_prediction, filename):
    fig = plt.figure(figsize=(6, 6))
    ax = fig.gca()
    ax.imshow(img, alpha=0.2)
    m = ax.matshow(
        (log_density_prediction[0, :, :, 0]),
        alpha=0.5,
        cmap=plt.cm.RdBu)
    fig.colorbar(m)
    ax.set_title('log density prediction')
    ax.axis('off')
    fig.tight_layout(pad=1)
    fig.savefig(filename)


def store_density(log_density_prediction, filename):
    fig = plt.figure(figsize=(6, 6))
    ax = fig.gca()
    ax.imshow(img, alpha=0.2)
    m = ax.matshow(
        np.exp(log_density_prediction[0, :, :, 0]),
        alpha=0.5,
        cmap=plt.cm.RdBu)
    fig.colorbar(m)
    ax.set_title('density prediction')
    ax.axis('off')
    fig.tight_layout(pad=1)
    fig.savefig(filename)


if __name__ == "__main__":

    CENTERBIAS_PATH = 'centerbias.npy'
    MODEL_PATH = 'checkpoints/DeepGazeII.ckpt'
    #MODEL_PATH = 'checkpoints/ICF.ckpt'

    sns.set_style('white')
    tf.disable_v2_behavior()

    imagelist = glob.glob('test_imgs/*.jpg')

    for path in imagelist:
        img_name = os.path.basename(path).replace(".jpg", "")
        img = image.imread(path)

        centerbias = load_centerbias(CENTERBIAS_PATH)
        log_density_prediction = process_img(img, centerbias, MODEL_PATH)

        out_file = os.path.join('output', img_name)
        store_prediction(log_density_prediction, f'{out_file}_prediction.png')
        store_density(log_density_prediction, f'{out_file}_density.png')
