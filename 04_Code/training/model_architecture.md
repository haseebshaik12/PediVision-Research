# PediVision AI — Model Architecture Specification

## 1. Objective

The deep-learning component of PediVision AI will investigate pediatric brain tumor
classification from MRI data and compare MRI-only, clinical-only, and multimodal
approaches.

The final architecture and configuration will be finalized after the approved
dataset has been obtained and its MRI modalities, labels, cohort size, and clinical
variables have been verified.

---

## 2. MRI-Only Model

The MRI-only experiment will use a convolutional neural network or transformer-based
architecture to learn discriminative representations from MRI data.

Candidate architectures include:

- ResNet-based architecture
- Vision Transformer (ViT)

The final architecture will be selected based on:

- MRI dimensionality and format
- Available MRI sequences
- Dataset size
- Computational resources
- Class distribution
- Training stability

No final architecture will be claimed before dataset verification.

---

## 3. MRI Preprocessing

MRI preprocessing will be performed consistently across the dataset.

Planned steps include:

1. MRI file validation
2. Loading of the imaging volume
3. Handling of invalid or non-finite values
4. Intensity normalization
5. Spatial preprocessing/resampling where required
6. Conversion to the input representation required by the selected model
7. Training-only augmentation where appropriate

The exact preprocessing parameters will be determined from the characteristics of
the approved dataset.

---

## 4. Clinical-Only Model

The clinical-only experiment will use verified clinical variables available in the
approved dataset.

Potential preprocessing steps include:

- Missing-value handling
- Numerical feature normalization
- Categorical feature encoding
- Feature validation
- Removal of variables that could introduce target leakage

Only variables confirmed by the official dataset documentation will be used.

---

## 5. Multimodal Model

The multimodal experiment will combine MRI-derived representations with clinical
representations.

Planned architecture:

MRI
|
v
MRI Encoder
|
v
MRI Feature Vector
|
+----------------------+
                       |
Clinical Information -> Clinical Encoder
                       |
                       v
              Clinical Feature Vector
                       |
                       v
                 Feature Fusion
                       |
                       v
              Classification Head
                       |
                       v
              Predicted Tumor Class

The fusion strategy will be finalized after the available clinical variables and
MRI representation have been verified.

Possible fusion approaches include:

- Feature-level concatenation
- Learned projection followed by fusion
- Joint neural representation

---

## 6. Classification Head

The classification head will map the learned representation to the verified tumor
classification categories.

The number of output classes will be determined from the actual approved dataset.

A suitable classification loss, such as cross-entropy loss for a multiclass
classification task, may be used if appropriate for the verified target structure.

---

## 7. Training Strategy

Training will use patient-level dataset partitions.

The planned structure is:

- Training set
- Validation set
- Held-out test set

No patient should appear across multiple partitions.

The validation set will be used for model selection and hyperparameter decisions.
The test set will remain isolated until final evaluation.

---

## 8. Class Imbalance

The class distribution will be inspected after dataset acquisition.

If substantial class imbalance is present, appropriate approaches may include:

- Class-weighted loss
- Stratified sampling where appropriate
- Training-set augmentation
- Other justified imbalance-handling methods

The selected method will be documented before final evaluation.

---

## 9. Evaluation

The models will be evaluated using metrics appropriate for multiclass
classification.

Planned metrics include:

- Accuracy
- Precision
- Recall
- F1-score
- Matthews correlation coefficient (MCC)
- Confusion matrix

Results will be calculated on the same held-out test set when comparing the
different experimental groups.

---

## 10. Explainability

Model explainability will be considered to help examine which image regions
contribute to model predictions.

For convolutional architectures, Grad-CAM or a related attribution method may be
used where technically appropriate.

Explainability results will be treated as interpretability evidence rather than
clinical proof.

---

## 11. Reproducibility

The implementation will record:

- Random seeds
- Dataset split information
- Model architecture
- Preprocessing configuration
- Training configuration
- Hyperparameters
- Evaluation metrics
- Software dependencies

The final experiments will be reproducible from the project repository without
including restricted patient-level data.

---

## 12. Research Integrity

No model performance values will be reported until experiments have been performed
using the approved dataset.

Synthetic data used during software development and pipeline testing will not be
reported as research results.

Dataset-specific assumptions will not be treated as confirmed facts until verified
against the official dataset documentation.