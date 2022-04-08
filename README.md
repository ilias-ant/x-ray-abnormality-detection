# x-ray-abnormality-detection

[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/ilias-ant/x-ray-abnormality-detection/tree/main) [![tensorflow](https://shields.io/badge/tensorflow-2.8-simple?logo=tensorflow&style=flat)](https://www.tensorflow.org/) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 

An attempt at the Bone X-Ray Deep Learning Competition (Stanford ML Group).

From the paper (see Citation below):

> The MURA abnormality detection task is a binary classification task, where the input is an upper exremity radiograph study — with each study containing one or more views (images) — and the expected output is a binary label y ∈ {0, 1} indicating whether the study is normal or abnormal,
respectively.

<img src="static/mura-sample-images.png" width="99%" text="https://www.researchgate.net/figure/Sample-images-from-MURA-dataset_fig2_348282230">

## Results

We have used the MURA v1.1 dataset. 

We report our findings on the Cohen’s kappa statistic, which expresses the agreement of the model with the gold standard. This is the metric used in the competition as well.

| model | Overall | Shoulder | Elbow | Humerus | Hand | Wrist | Forearm | Finger |
| --- | --- | --- | --- | --- | --- | --- | --- |--- |
|CNN (sc) |0.386 | 0.17 | 0.50 | 0.44 | 0.18 | 0.51 | 0.44 | 0.37|
| ens: CNN + wrist-CNN (sc) |0.400 | 0.17 | 0.50 | 0.44 | 0.18 | 0.58 | 0.44 | 0.37|
|DenseNet-169 (pt) | 0.629 | 0.54 | **0.72** | 0.72 | 0.43 | 0.71 | 0.65 | 0.59|
|VGG-19 (pt) |0.598 | 0.51 | 0.67 | 0.7 | 0.42 | 0.67 | 0.62 | 0.56|
| ResNet50 (pt) | 0.618 | 0.47 | 0.63 | **0.75** | **0.47** | **0.72** | 0.66 | 0.6 |
| ens: DenseNet-169 + VGG-19| 0.629 | 0.57 | 0.7 | 0.73 | 0.45 | 0.7 | 0.63 | 0.58|
| ens: DenseNet-169 + ResNet50 | **0.645** | **0.62** | 0.69 | 0.69 | 0.45 | 0.71 | **0.68** | **0.62** |


*(pt): pre-trained | (sc): trained from scratch.

## Installation

You will at the very least need a local copy of the [MURA dataset](https://stanfordmlgroup.github.io/competitions/mura/): download the dataset version (e.g. `v1.1`) you want to use and place it in the `data` folder (e.g. `data/MURA-v1.1/`).

To enable reproducibility, [Poetry](https://python-poetry.org/) has been used as a dependency manager.

```shell
python3 -m pip install poetry
```

and then:

```shell
python3 -m poetry install
```

To serve the Jupyter notebooks, run:

```shell
python3 -m poetry run jupyter notebook
```

## Contributors

- [Ilias Antonopoulos](https://github.com/ilias-ant)
- [Silva Ndoja](https://github.com/sndoja)

## Citation

```bibtex
@article{Rajpurkar2017MURALD,
  title={MURA: Large Dataset for Abnormality Detection in Musculoskeletal Radiographs.},
  author={Pranav Rajpurkar and Jeremy A. Irvin and Aarti Bagul and Daisy Yi Ding and Tony Duan and Hershel Mehta and Brandon Yang and Kaylie Zhu and Dillon Laird and Robyn L. Ball and C. Langlotz and Katie S. Shpanskaya and Matthew P. Lungren and A. Ng},
  journal={arXiv: Medical Physics},
  year={2017}
}
```
