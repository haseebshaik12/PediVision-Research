# PediVision AI — Deep Learning MRI Pipeline

## 1. Purpose

This document defines the planned deep-learning pipeline for the MRI component of PediVision AI.

The MRI model will be developed after the approved dataset has been verified.

---

## 2. MRI Input

The model will receive MRI data from the approved dataset.

Before model training, the following will be verified:

- MRI file format
- Available MRI sequences
- Image dimensions
- Voxel spacing
- Orientation
- Number of available subjects
- Number of images per subject

The final input representation will depend on the verified dataset.

---

## 3. MRI Preprocessing

The planned preprocessing pipeline consists of:

```text
Raw MRI
   ↓
File Validation
   ↓
Load MRI
   ↓
Numerical Validity Check
   ↓
Intensity Normalization
   ↓
Spatial Preparation
   ↓
Model Input