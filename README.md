# x-ray-abnormality-detection

[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/ilias-ant/x-ray-abnormality-detection/tree/main) [![tensorflow](https://shields.io/badge/tensorflow-2.8-simple?logo=tensorflow&style=flat)](https://www.tensorflow.org/) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 

An attempt at the Bone X-Ray Deep Learning Competition (Stanford ML Group).

<img src="static/mura-cam3.svg" width="100%">

## Installation

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
