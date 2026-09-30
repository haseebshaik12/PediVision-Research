
# PediVision Research Gap

## 1. Background
Pediatric brain tumor classification using MRI is an active area of medical AI research. Existing studies have explored deep learning for tumor classification, detection, and segmentation. Some studies have also investigated the use of patient age alongside MRI features.

## 2. Preliminary Literature Comparison

### Paper 01
Focus: Pediatric brain tumor classification using MRI and age fusion.

Relevance: Investigates whether patient age can be combined with MRI-derived features for classification.

### Paper 02
Focus: Pediatric brain tumor detection and subtype prediction using deep learning.

Relevance: Provides related work on MRI-based tumor analysis.

### Paper 03
Focus: Description of a pediatric brain tumor MRI dataset from CBTN.

Relevance: May help identify suitable imaging and clinical data for research.

Note: The exact bibliographic details, methods, and findings of all three papers must be verified against their original publications before finalizing this comparison.

## 3. Preliminary Research Gap
A potential research direction is to investigate whether combining MRI-derived features with structured clinical information improves pediatric brain tumor classification compared with MRI-only and clinical-only models.

The availability of appropriate clinical variables, patient-level linkage, and sufficient labeled cases must be confirmed before this direction can be finalized.

## 4. Research Question
Does integrating MRI-derived features with structured clinical information improve pediatric brain tumor classification compared with MRI-only and clinical-only models?

## 5. Proposed Experiments
1. Establish an MRI-only classification baseline.
2. Establish a clinical-only classification baseline, if suitable variables are available.
3. Develop a multimodal model combining MRI and clinical features.
4. Compare the models using consistent patient-level data splits and evaluation metrics.
5. Investigate performance when one modality is unavailable, if the dataset supports this analysis.

## 6. Important Considerations
- Verify dataset access permissions and terms of use.
- Confirm the availability and meaning of clinical variables.
- Prevent patient-level data leakage between training and testing.
- Report class imbalance and missing data.
- Avoid making clinical claims without appropriate validation.

## 7. Research Gap Status

Existing studies have explored deep learning for pediatric brain tumor classification using MRI data and, in some cases, clinical information. However, the extent to which combining MRI-derived features with clinical information improves multi-class classification of pediatric brain tumor subtypes requires further investigation.

This study will compare MRI-only, clinical-only, and multimodal models under a consistent experimental framework. It will also examine the impact of missing modalities and explore model explainability.

The final tumor classes and clinical variables will depend on the verified availability of data in the selected dataset.
