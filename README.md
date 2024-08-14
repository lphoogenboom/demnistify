# Demnistify

***<p align="center">(The "n" is silent)</p>***

### Interpretable Post-Hoc Machine Learning on the MNIST DATA set.
This project aims provide a set of interpretability methods for deep neural nets. All these methods will be **post-hoc**. This means that we will not used methods that change the model fundamnetally, but instead work with an already trained model that was not designed with interpretability in mind.

#### MNIST DATA
The MNIST data set is a collection of hand-drawn numbers ranging 0 to 9. Each image is black-and-white and has the number centered. The file size is very small, yet extensive enough to do good training. This means that training algorithms execute quickly and there is enough dept in the data to differentiate between well trained models and poorly trained models.

![Example of MNIST images](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.researchgate.net%2Fpublication%2F359449733%2Ffigure%2Ffig2%2FAS%3A11431281087562446%401664675721372%2FExample-Images-of-the-MNIST-Handwritten-Digit-Classification-dataset.png&f=1&nofb=1&ipt=acd19b0464996a0fddfc4fcc9a42cbbeaea4839e2e7dfa0b5bf809ae93452763&ipo=images)<p>Examples of images in MNIST data set</p>

#### Reported Performances of models (2019)
**Table:** *Side-by-side comparison of different models trained on MNIST data without augmentation. Source: [A Survey of Handwritten Character Recognition with
MNIST and EMNIST](https://www.mdpi.com/2076-3417/9/15/3169?type=check_update)*
| Technique                                                     | Test Error Rate |
| :---                                                          | :---: |
|HOPE+DNN with unsupervised learning features                   |0.40%|
|Deep convex net                                                |0.83%|
|CDBN                                                           |0.82%|
|S-SC + linear SVM                                              |0.84%|
|2-layer MP-DBM                                                 |0.88%|
|DNet-kNN                                                       |0.94%|
|2-layer Boltzmann machine                                      |0.95%|
|Batch-normalized maxout network-in-network                     |0.24%|
|Committees of evolved CNNs (CEA-CNN)                           |0.24%|
|Genetically evolved committee of CNNs                          |0.25%|
|Committees of 7 neuroevolved CNNs                              |0.28%|
|CNN with gated pooling function                                |0.29%|
|Inception-Recurrent CNN + LSUV + EVE                           |0.29%|
|Recurrent CNN                                                  |0.31%|
|CNN with norm. layers and piecewise linear activation units    |0.31%|
|[CNN (5 conv, 3 dense) with full training](https://ieeexplore.ieee.org/abstract/document/7280683)                       |0.32%|
|MetaQNN (ensemble)                                             |0.32%|
|Fractional max-pooling CNN with random overlapping             |0.32%|
|CNN with competitive multi-scale conv. filters                 |0.33%|
|CNN neuroevolved with GE                                       |0.37%|
|Fast-learning shallow CNN                                      |0.37%|
|CNN FitNet with LSUV initialization and SVM                    |0.38%|
|Deeply supervised CNN                                          |0.39%|
|Convolutional kernel networks                                  |0.39%|
|CNN with Multi-loss regularization                             |0.42%|
|MetaQNN                                                        |0.44%|
|CNN (3 conv maxout, 1 dense) with dropout                      |0.45%|
|Convolutional highway networks                                 |0.45%|
|CNN (5 conv, 3 dense) with retraining                          |0.46%|
|Network-in-network                                             |0.47%|
|CNN (3 conv, 1 dense), stochastic pooling                      |0.49%|
|CNN (2 conv, 1 dense, relu) with dropout                       |0.52%|
|CNN, unsup pretraining                                         |0.53%|
|CNN (2 conv, 1 dense, relu) with DropConnect                   |0.57%|
|SparseNet + SVM                                                |0.59%|
|CNN (2 conv, 1 dense), unsup pretraining                       |0.60%|
|DEvol                                                          |0.60%|
|CNN (2 conv, 2 dense)                                          |0.62%|
|Boosted Gabor CNN                                              |0.68%|
|CNN (2 conv, 1 dense) with L-BFGS                              |0.69%|
|Fastfood 1024/2048 CNN                                         |0.71%|
|Feature Extractor + SVM                                        |0.83%|
|Dual-hidden Layer Feedforward Network                          |0.87%|
|CNN LeNet-5                                                    |0.95%|