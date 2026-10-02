# PediVision AI — Experiment Protocol

## Research Title

Multimodal Deep Learning for Pediatric Brain Tumor Classification Using MRI and Clinical Information

## 1. Research Objective

The primary objective is to investigate whether combining MRI-derived information with relevant clinical information improves pediatric brain tumor classification compared with using MRI information alone or clinical information alone.

## 2. Experimental Groups

Three experimental settings will be evaluated where the approved dataset supports them:

### Experiment A — MRI-Only

Input:

- MRI-derived information

Output:

- Target classification label

Purpose:

Establish the performance of an imaging-only baseline.

### Experiment B — Clinical-Only

Input:

- Relevant clinical variables available in the approved dataset

Output:

- Target classification label

Purpose:

Establish the performance of a clinical-information-only baseline.

### Experiment C — Multimodal

Input:

- MRI-derived information
- Relevant clinical information

Output:

- Target classification label

Purpose:

Determine whether combining the two modalities provides additional predictive information.

## 3. Dataset Verification

Before model training, the approved dataset will be inspected to verify:

- Available MRI sequences
- MRI file format
- Available clinical variables
- Target label
- Missing values
- Number of eligible subjects
- Number of records per subject
- Class distribution
- Data-access restrictions

No dataset variables will be assumed before verification.

## 4. Data Splitting

Data will be divided into:

- Training set
- Validation set
- Test set

Splitting will occur at the patient/subject level where applicable.

Records belonging to the same patient must not be distributed across different dataset partitions.

This is intended to reduce patient-level data leakage.

## 5. MRI Processing

The MRI pipeline will include appropriate preprocessing based on the verified dataset structure.

Initial processing components include:

- MRI file inspection
- Numerical validity checks
- Intensity normalization
- MRI visualization
- Feature extraction or learned representation generation

Additional preprocessing will be determined after dataset verification.

## 6. Clinical Data Processing

Clinical variables will be processed according to their actual data types and availability.

Potential processing steps may include:

- Missing-value handling
- Numerical feature normalization
- Categorical-variable encoding
- Feature selection where justified

Only variables permitted by the approved dataset and relevant to the research question will be used.

## 7. MRI Model

A baseline MRI-only model will first be established.

Potential deep-learning architectures include established image-based architectures such as:

- ResNet-based models
- Vision Transformer-based models

The final architecture will be selected after considering dataset size, image representation, computational requirements, and experimental suitability.

## 8. Clinical Model

A clinical-only baseline will be developed using the verified clinical variables.

The baseline may use a conventional machine-learning classifier before more complex approaches are considered.

## 9. Multimodal Model

The multimodal model will combine MRI-derived representations with clinical representations.

A general fusion workflow is:

MRI → MRI representation
Clinical data → Clinical representation
MRI representation + Clinical representation → Fusion
Fusion → Classification head

The exact fusion strategy will be determined during model development.

## 10. Evaluation

The experiments will use a common evaluation protocol.

Planned evaluation metrics include:

- Accuracy
- Precision
- Recall
- F1-score
- Matthews correlation coefficient (MCC)
- Confusion matrix

Additional metrics may be included if appropriate for the verified class distribution.

## 11. Experimental Comparison

The primary comparison will be:

MRI-only vs Clinical-only vs Multimodal

The experiments will be evaluated using the same appropriate test population and evaluation protocol.

The study will determine whether multimodal integration provides measurable improvement rather than assuming that it will.

## 12. Reproducibility

Experiments will use:

- Fixed random seeds where appropriate
- Version-controlled code
- Documented preprocessing
- Documented model configurations
- Documented evaluation procedures

Experiment configurations and results will be recorded systematically.

## 13. Data Leakage Prevention

Patient-level separation will be maintained throughout the experimental workflow.

Information from the test set must not be used to train or tune the model.

Any preprocessing step that learns parameters from the data must be fitted using the training data and then applied to validation/test data.

## 14. Research Integrity

No results will be fabricated or inferred before experiments are conducted on the approved dataset.

Synthetic data may be used to test software functionality, but synthetic-test performance will not be reported as research findings.

Actual dataset characteristics, labels, cohort sizes, and experimental results will be documented only after verification and analysis of the approved dataset.

## 15. Current Status

The software pipeline and experimental framework have been prepared and tested using synthetic data.

The actual CBTN dataset has not yet been incorporated into the experimental pipeline.

The next stage is dataset-access completion and verification of the approved dataset structure.