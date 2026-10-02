# PediVision AI — Research Methodology

## 1. Overview

PediVision AI investigates multimodal deep learning for pediatric brain tumor classification using MRI imaging and relevant clinical information.

The methodology is organized into the following stages:

1. Dataset access
2. Dataset verification
3. MRI preprocessing
4. Clinical data processing
5. Patient-level dataset splitting
6. MRI-only modeling
7. Clinical-only modeling
8. Multimodal modeling
9. Model evaluation
10. Comparative analysis

## 2. Dataset Access

The study intends to use an approved pediatric brain tumor dataset obtained through the appropriate data-access process.

The current project is pursuing access to Children's Brain Tumor Network (CBTN) resources.

The actual dataset characteristics will be documented only after access and verification.

## 3. Dataset Verification

After receiving access, the dataset will be examined to determine:

- Number of eligible subjects
- Available MRI sequences
- MRI file formats
- Available clinical variables
- Target classification labels
- Missing data
- Class distribution
- Number of records per subject

No assumptions will be made about variables that are not confirmed by the official dataset documentation.

## 4. MRI Processing

MRI files will undergo appropriate preprocessing before model development.

The current software pipeline supports:

- NIfTI file loading
- MRI dimension inspection
- Voxel-spacing inspection
- Numerical-value validation
- Intensity normalization
- MRI visualization
- MRI feature extraction

Additional preprocessing will be selected based on the verified dataset structure.

## 5. Clinical Data Processing

Clinical information will be inspected and prepared according to the actual variables available in the approved dataset.

Potential processing steps include:

- Missing-value assessment
- Numerical-variable processing
- Categorical-variable encoding
- Feature normalization
- Feature selection where justified

The final clinical feature set will be determined after dataset verification.

## 6. Patient-Level Data Splitting

Dataset partitioning will be performed at the patient/subject level where applicable.

The purpose is to prevent records from the same patient from appearing in multiple partitions.

The initial software framework uses:

- 70% training
- 15% validation
- 15% testing

The final partitioning strategy will be documented according to the approved dataset and experimental requirements.

## 7. MRI-Only Model

An MRI-only baseline will use information derived from MRI images.

The project will investigate established deep-learning approaches such as:

- ResNet-based architectures
- Vision Transformer-based architectures

The final architecture will be selected based on the verified dataset, computational requirements, and experimental design.

## 8. Clinical-Only Model

A clinical-only baseline will use the relevant verified clinical variables.

A conventional machine-learning model will initially provide a baseline for comparison.

## 9. Multimodal Model

The multimodal approach combines MRI-derived information with clinical information.

The general workflow is:

```text
MRI
 ↓
MRI Encoder
 ↓
MRI Representation
          \
           → Feature Fusion → Classifier → Prediction
          /
Clinical Data
 ↓
Clinical Encoder
 ↓
Clinical Representation