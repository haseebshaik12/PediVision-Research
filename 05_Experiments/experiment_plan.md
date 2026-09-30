# PediVision AI — Experiment Plan

## 1. Research Objective

The objective of this experimental study is to investigate whether combining pediatric brain MRI data with clinically available patient information improves classification performance compared with MRI-only and clinical-only approaches.

The experiments will also investigate performance under incomplete input conditions and examine model predictions using explainability methods where appropriate.

**Important:** All experiments are planned. No results have been generated yet.

---

## 2. Dataset Requirements

The dataset must provide:

* Pediatric brain MRI scans appropriate for the selected classification task.
* Reliable patient identifiers for patient-level data splitting.
* Target labels suitable for classification.
* Relevant clinical variables, if available.
* Appropriate permissions for research use.

The Children's Brain Tumor Network (CBTN) is being investigated as a potential dataset.

The final dataset and classification task will be selected after reviewing the available data and access conditions.

---

## 3. Experimental Setup

### Data Partitioning

The dataset will be divided into:

* Training set
* Validation set
* Test set

The split will be performed at the patient level to prevent data leakage.

The same patient must not appear in more than one partition.

The exact split proportions will be finalized after dataset assessment.

### Preprocessing

MRI preprocessing may include:

* Image loading and integrity checks.
* Intensity normalization.
* Image resizing or resampling where appropriate.
* Sequence selection and alignment where necessary.

Clinical preprocessing may include:

* Missing-value analysis.
* Numerical feature scaling.
* Categorical-variable encoding.
* Appropriate missing-value handling.

Any preprocessing parameters learned from data will be fitted using training data only.

---

## 4. Experiment EXP-01 — Dataset Analysis

### Objective

Understand the dataset structure, quality, and suitability for the research task.

### Tasks

1. Identify the number of eligible patients.
2. Inspect available MRI sequences.
3. Identify available clinical variables.
4. Check target labels and class distribution.
5. Analyze missing values.
6. Review data quality and access restrictions.
7. Finalize the classification task.

### Expected Output

* Dataset summary.
* Class-distribution table.
* Missing-value summary.
* Data dictionary.
* Finalized task specification.

### Status

Not started.

---

## 5. Experiment EXP-02 — Clinical-Only Baseline

### Objective

Establish a baseline using clinical variables without MRI data.

### Input

Selected clinical variables available for the chosen task.

### Proposed Model

A multilayer perceptron (MLP) or another appropriate tabular baseline.

### Evaluation

The model will be evaluated using the selected classification metrics on the held-out test set.

### Expected Output

* Clinical-only model.
* Evaluation metrics.
* Confusion matrix, where appropriate.

### Status

Not started.

---

## 6. Experiment EXP-03 — MRI-Only Baseline

### Objective

Establish a baseline using MRI data without clinical variables.

### Input

MRI images from the selected sequence or sequences.

### Proposed Model

A convolutional neural network (CNN), such as ResNet, will be considered as the image encoder.

### Evaluation

The MRI-only model will be evaluated using the same patient-level data partitions and appropriate metrics.

### Expected Output

* MRI-only model.
* Evaluation metrics.
* Confusion matrix, where appropriate.

### Status

Not started.

---

## 7. Experiment EXP-04 — Multi-Sequence MRI

### Objective

Investigate whether combining multiple MRI sequences improves classification performance compared with using a single sequence.

### Input

Available MRI sequences suitable for the selected task.

### Proposed Approach

Compare individual-sequence models with a multi-sequence approach, if the dataset supports this comparison.

### Evaluation

Use consistent data partitions and evaluation metrics.

### Expected Output

* Single-sequence comparison.
* Multi-sequence comparison.
* Performance summary.

### Status

Not started.

---

## 8. Experiment EXP-05 — Multimodal MRI + Clinical Model

### Objective

Investigate whether integrating MRI-derived features with clinical information improves classification performance.

### Model Components

**MRI branch:** A CNN-based image encoder.

**Clinical branch:** An MLP or another suitable tabular encoder.

**Fusion:** Combine the image and clinical feature representations.

**Classifier:** Predict the selected target label.

### Comparison

Compare:

1. Clinical-only model.
2. MRI-only model.
3. Multimodal MRI-clinical model.

### Expected Output

* Multimodal model.
* Model comparison table.
* Evaluation metrics.

### Status

Not started.

---

## 9. Experiment EXP-06 — Missing MRI Modalities

### Objective

Investigate how classification performance changes when one or more MRI sequences are unavailable.

### Proposed Approach

Evaluate the model under selected missing-sequence conditions and compare its performance with the complete-input condition.

The missing-modality strategy will be chosen based on the dataset and model architecture.

### Expected Output

* Missing-sequence evaluation.
* Performance comparison.
* Analysis of robustness limitations.

### Status

Not started.

---

## 10. Experiment EXP-07 — Missing Clinical Information

### Objective

Investigate how incomplete clinical information affects multimodal classification.

### Proposed Approach

Evaluate selected conditions in which clinical variables are unavailable.

Missingness patterns and handling strategies will be documented.

### Expected Output

* Missing-clinical-information evaluation.
* Performance comparison.
* Analysis of robustness limitations.

### Status

Not started.

---

## 11. Experiment EXP-08 — Explainability

### Objective

Examine which image regions and clinical variables contribute to model predictions.

### Potential Methods

* Grad-CAM for image-based models.
* SHAP or another appropriate feature-attribution method for clinical variables.

### Analysis

The visualizations and feature attributions will be interpreted cautiously.

They will not be treated as proof of causal relationships or clinical validity.

### Expected Output

* Selected visualization examples.
* Feature-attribution analysis.
* Discussion of interpretability limitations.

### Status

Not started.

---

## 12. Evaluation Metrics

Depending on the task and class distribution, the following metrics may be used:

* Accuracy.
* Precision.
* Recall.
* Macro-F1 score.
* Matthews correlation coefficient (MCC).
* ROC-AUC, where appropriate.
* Confusion matrix.

Additional metrics may be included if justified by the task.

Macro-F1 and class-specific performance will be considered to avoid relying solely on accuracy.

---

## 13. Reproducibility

The following information will be recorded for each experiment:

* Experiment identifier.
* Dataset version or approved data reference.
* Patient-level split strategy.
* Preprocessing configuration.
* Model architecture.
* Hyperparameters.
* Random seed.
* Training configuration.
* Evaluation metrics.
* Software environment.
* Limitations and observations.

Restricted patient data will not be uploaded to the public repository.

---

## 14. Results Tracking

| Experiment                           | Status      | Results |
| ------------------------------------ | ----------- | ------- |
| EXP-01: Dataset Analysis             | Not started | Pending |
| EXP-02: Clinical-Only Baseline       | Not started | Pending |
| EXP-03: MRI-Only Baseline            | Not started | Pending |
| EXP-04: Multi-Sequence MRI           | Not started | Pending |
| EXP-05: Multimodal Model             | Not started | Pending |
| EXP-06: Missing MRI Modalities       | Not started | Pending |
| EXP-07: Missing Clinical Information | Not started | Pending |
| EXP-08: Explainability               | Not started | Pending |

---

## 15. Completion Criteria

The study will be considered experimentally complete when:

1. The dataset and classification task are documented.
2. The data partitions and preprocessing are established.
3. The planned baseline models have been evaluated.
4. The multimodal model has been evaluated, if feasible.
5. The planned missing-modality experiments have been conducted, if feasible.
6. Results are documented with appropriate metrics.
7. Limitations and reproducibility information are recorded.
8. The findings are ready for interpretation and manuscript preparation.

## Multi-Class Classification Strategy

### Objective

Classify pediatric brain tumors into the available subtypes using MRI data, clinical information, and a combination of both.

### Planned Experiments

1. **MRI-only model:** Use MRI images to classify tumor subtypes.
2. **Clinical-only model:** Use available clinical features to classify tumor subtypes.
3. **Multimodal model:** Combine MRI-derived features and clinical information.
4. **Missing-modality experiment:** Evaluate model performance when MRI or clinical information is unavailable.

### Evaluation

Evaluate models using accuracy, precision, recall, macro-F1 score, Matthews correlation coefficient (MCC), and confusion matrices.

The final class labels and dataset-specific experimental settings will be determined after dataset verification.

