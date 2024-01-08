# AI-Project-Heart-Disease

## Key Features
### Superior Performance of MLP with "tanh" Activation: 
Based on experiment outcomes, the MLP model with the "tanh" activation function outperformed both linear and non-linear SVM models, achieving the highest accuracy of 0.885. This indicates that the MLP model is a better fit for this dataset and its ability to simulate non-linear correlations contributes to capturing complex data patterns effectively.
   
### Model Advantages: 
SVMs excel in handling high-dimensional and non-linearly separable data through kernel functions, offering insights into the decision-making process. On the other hand, MLPs provide greater flexibility, mastering complex mappings. Careful hyperparameter selection is essential to avoid overfitting in MLP, while the symmetric "tanh" activation function aids in better data pattern understanding.
   
## What I Will Be Using
### MLP:
- Activation Functions -
  1. ReLU (Rectified Linear Unit): Non-linear activation function, outputting input for positive values, zero otherwise.
  2. Tanh (Hyperbolic Tangent): Outputs values in the range [-1, 1], capturing non-linear relationships.
 
- Optimizers -
  1. Stochastic Gradient Descent (SGD): Iterative algorithm to minimize the model's error by adjusting parameters. Effective for large datasets.
  2. Adam Optimizer: Adaptive learning rate algorithm for training neural networks, effective in handling noisy data.
     
- Learning Rates-
  1. [0.01, 0.001]: How big the steps are when the model learns. Higher learning rates can speed up training but might cause the model to surpass the optimal values. Lower rates ensures stability but may slow down training.

### SVM:
- Kernels -
  1. Linear Kernel: A simple kernel that creates linear decision boundaries, works well for linearly separable data.
  2. RBF (Radial Basis Function) Kernel: A versatile kernel that can handle non-linear decision boundaries, suitable for a wide range of data distributions.
  3. Sigmoid Kernel: Non-linear kernel function that is particularly useful for binary classification tasks.

## Download Dataset
You can download the dataset (processed.cleveland.data) from the UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/Heart+Disease
