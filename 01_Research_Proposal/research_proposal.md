# Research Proposal

## 1. Research Title

**Multimodal Deep Learning for Pediatric Brain Tumor Classification Using MRI and Clinical Information**

*Working title — subject to refinement after the literature review and dataset assessment.*

## 2. Research Domain

**Primary Domain:** Healthcare Artificial Intelligence

**Specific Area:** Medical Imaging AI

**Research Focus:**

* Pediatric Neuroimaging
* Deep Learning
* Multimodal Artificial Intelligence
* Medical Image Analysis
* Explainable AI
* Robust Machine Learning
* AI-Assisted Clinical Decision Support

## 3. Abstract

This proposed research investigates the use of multimodal deep learning for pediatric brain tumor classification by integrating magnetic resonance imaging (MRI) data with clinically available patient information. The study aims to compare MRI-only, clinical-only, and multimodal classification approaches under a consistent experimental framework. It will also investigate model performance when some MRI sequences or clinical variables are unavailable. Explainability methods may be used to examine image regions and clinical variables associated with model predictions. The research will focus on appropriate data preprocessing, patient-level data partitioning, evaluation metrics, and reproducibility. The availability of suitable datasets, clinical variables, and target labels will be assessed before implementation. The findings are intended to contribute to the understanding of multimodal learning for pediatric brain MRI analysis. No clinical validity is assumed.

## 4. Introduction and Background

Artificial intelligence and deep learning have become important research areas in medical image analysis. Deep learning models can learn image representations from MRI scans and may support the investigation of classification tasks involving brain tumors.

Pediatric brain tumors present distinct research challenges because of differences in tumor types, patient characteristics, imaging protocols, and the availability of labeled data.

MRI provides structural and tissue-related information, while clinical information may provide additional context about a patient's characteristics and medical history. Integrating these sources may offer complementary information for classification.

However, multimodal learning introduces challenges, including missing data, differences in data quality, limited sample sizes, class imbalance, and the risk of data leakage.

This research proposes a systematic investigation of MRI-only, clinical-only, and multimodal models for a clearly defined pediatric brain tumor classification task.

## 5. Problem Statement

MRI-based deep learning models can learn patterns from medical images, but image-only approaches do not directly incorporate potentially useful clinical information.

Clinical-only models, on the other hand, may not capture the imaging patterns available in MRI scans.

A multimodal model may combine these information sources, but its benefit must be established through controlled experiments.

The central problem is to determine whether integrating MRI-derived features with appropriate clinical variables improves pediatric brain tumor classification and how model performance changes when some input information is unavailable.

## 6. Preliminary Research Gap

Existing research has investigated deep learning for pediatric brain MRI analysis and has also explored the use of clinical variables in prediction tasks.

A systematic comparison of MRI-only, clinical-only, and multimodal approaches under consistent experimental conditions, including missing-modality evaluation, is the proposed focus of this study.

This is a **preliminary research gap**. It must be verified through a detailed literature review before being presented as an established gap or a novel contribution.

## 7. Research Questions

## Primary Research Question

Does integrating MRI-derived features with clinically available patient information improve multi-class classification of available pediatric brain tumor subtypes compared with MRI-only and clinical-only models?

## Secondary Research Questions

1. How does the performance of MRI-only, clinical-only, and multimodal models compare?
2. Does using multiple MRI sequences improve classification performance compared with a single sequence?
3. How does model performance change when MRI or clinical information is missing?
4. Which MRI regions and clinical features contribute to the model's predictions?

The final tumor classes and clinical variables will be determined after dataset verification.


## 8. Research Hypotheses

* **H1:** A multimodal MRI-clinical model may achieve better classification performance than MRI-only and clinical-only models.
* **H2:** Combining multiple MRI sequences may improve classification performance compared with a single sequence.
* **H3:** Missing-modality training or evaluation strategies may help identify approaches that are more robust to incomplete data.
* **H4:** Explainability methods may identify image regions and clinical variables associated with model predictions.

These hypotheses will be evaluated experimentally and may not be supported by the findings.

## 9. Research Objectives

1. Identify a suitable pediatric brain MRI dataset with appropriate clinical information and target labels.
2. Analyze dataset characteristics, data quality, missing values, and class distribution.
3. Develop an MRI-only classification baseline.
4. Develop a clinical-only classification baseline.
5. Develop a multimodal MRI-clinical classification model.
6. Compare the approaches using appropriate evaluation metrics.
7. Investigate performance under missing-modality conditions.
8. Examine model predictions using suitable explainability methods.
9. Document limitations, reproducibility considerations, and potential research implications.

## 10. Dataset and Data Sources

### Potential Dataset

The Children's Brain Tumor Network (CBTN) is being investigated as a potential source of pediatric brain tumor imaging and associated clinical information.

### Dataset Selection Criteria

The selected dataset should provide:

* Pediatric brain MRI scans suitable for the selected task.
* Clearly defined target labels.
* Relevant clinical variables, if available.
* Sufficient eligible subjects for a defensible experimental design.
* Appropriate access permissions and data-use conditions.

### Dataset Status

* Dataset access: To be confirmed.
* Eligible patient count: Not yet established.
* Available MRI sequences: To be confirmed.
* Clinical variables: To be confirmed.
* Target classification labels: To be finalized.
* Institutional and ethical requirements: To be reviewed.

No dataset characteristics will be assumed until the actual data documentation has been examined.

## 11. Proposed Methodology

### 11.1 Dataset Assessment

The dataset will be examined to determine the number of eligible subjects, available MRI sequences, target labels, clinical variables, missing values, and class distribution.

The classification task and inclusion/exclusion criteria will be finalized based on the available data.

### 11.2 MRI Preprocessing

Depending on the dataset and selected task, MRI preprocessing may include:

* MRI file loading and integrity checks.
* Image orientation and dimensionality checks.
* Intensity normalization.
* Image resizing or resampling when appropriate.
* Sequence selection and alignment where required.

Preprocessing will be documented and applied consistently. Any transformations that learn parameters from data will be fitted using training data only.

### 11.3 Clinical Data Preprocessing

Clinical variables will be selected based on availability, relevance, completeness, and permitted use.

Potential preprocessing steps include:

* Missing-value analysis.
* Appropriate numerical feature scaling.
* Categorical-variable encoding.
* Missing-value handling.
* Exclusion of variables that could cause target leakage.

Clinical preprocessing parameters will be fitted on training data only.

### 11.4 Data Partitioning

Data will be divided into training, validation, and test sets at the patient level.

The same patient must not appear in multiple partitions. This is essential to reduce data leakage and obtain a more reliable estimate of model performance.

The exact split proportions will be finalized after dataset assessment.

### 11.5 MRI-Only Model

A convolutional neural network (CNN), such as ResNet, will be investigated as an image encoder.

The MRI-only model will serve as an imaging baseline.

### 11.6 Clinical-Only Model

A multilayer perceptron (MLP) or another suitable tabular baseline will be investigated using selected clinical variables.

This model will provide a clinical-data baseline.

### 11.7 Multimodal MRI-Clinical Model

The MRI encoder will generate image features, while a separate clinical-data branch will generate clinical features.

The two feature representations will be combined using a feature-level fusion approach and passed to a classification head.

The architecture will be selected according to dataset size, data availability, and computational resources.

### 11.8 Missing-Modality Experiments

The study will investigate performance when one or more MRI sequences or selected clinical variables are unavailable.

The missing-modality strategy will be chosen according to the dataset and experimental design.

Results will be compared with the corresponding complete-input condition.

## 12. Experimental Design

The planned experiments are:

| Experiment | Description                                             |
| ---------- | ------------------------------------------------------- |
| EXP-01     | Dataset analysis and data-quality assessment            |
| EXP-02     | Clinical-only baseline                                  |
| EXP-03     | MRI-only baseline                                       |
| EXP-04     | Multi-sequence MRI experiment, if supported by the data |
| EXP-05     | Multimodal MRI-clinical fusion                          |
| EXP-06     | Missing MRI modality evaluation                         |
| EXP-07     | Missing clinical information evaluation                 |
| EXP-08     | Explainability analysis                                 |

The final experiment list will be adjusted after the dataset and research task are confirmed.

## 13. Evaluation Metrics

The study may use the following metrics, depending on the classification task and class distribution:

* Accuracy
* Precision
* Recall
* Macro-F1 score
* Matthews correlation coefficient (MCC)
* ROC-AUC, where appropriate
* Confusion matrix

Additional analyses may include calibration metrics and confidence intervals where appropriate.

Macro-F1 and class-specific performance will be considered to avoid relying solely on accuracy in an imbalanced dataset.

## 14. Explainability

Explainability methods may be used to investigate model behavior.

Potential methods include:

* **Grad-CAM:** To visualize image regions associated with CNN predictions.
* **SHAP or other suitable feature-attribution methods:** To examine the contribution of clinical variables.

These methods will be interpreted cautiously. An explanation map does not establish that a model has identified a clinically meaningful biomarker or causal relationship.

## 15. Expected Contribution

The intended contribution is a controlled comparison of MRI-only, clinical-only, and multimodal MRI-clinical approaches for a defined pediatric brain tumor classification task, together with missing-modality and explainability analyses where feasible.

The contribution and novelty will be reassessed after the literature review and experiments.

## 16. Ethical Considerations

The study will follow applicable dataset access conditions, institutional requirements, and ethical guidelines.

* Use only data that the research team is authorized to access.
* Protect patient privacy and confidentiality.
* Avoid publishing identifiable patient information.
* Keep restricted medical data out of public GitHub repositories.
* Document relevant data-use permissions and ethics approvals, where required.
* Avoid presenting the model as a clinically validated diagnostic system.

## 17. Limitations

Potential limitations include:

* Limited dataset size.
* Class imbalance.
* Missing clinical variables.
* Incomplete MRI sequences.
* Differences in MRI acquisition protocols.
* Limited generalizability across institutions.
* Computational constraints.
* Lack of external validation, if no independent dataset is available.

These limitations will be updated based on the actual study.

## 18. Expected Outcomes

The expected outputs are:

1. A documented dataset assessment.
2. Reproducible preprocessing and model code.
3. Experimental comparisons of the selected approaches.
4. Missing-modality and explainability analyses, where feasible.
5. Tables and figures based on actual experimental results.
6. A research manuscript documenting the methods, results, and limitations.

No performance improvement is assumed in advance.

## 19. Technology Stack

The proposed tools include:

* Python
* PyTorch or TensorFlow
* NumPy
* pandas
* scikit-learn
* Matplotlib
* SimpleITK or other appropriate medical-imaging tools
* Git and GitHub
* Jupyter Notebook or VS Code

The final stack will depend on the selected dataset and model.

## 20. Research Status

**Current stage:** Research planning and literature review.

**Dataset access:** Under investigation.

**Implementation:** Not started.

**Experimental results:** Not available.

**Manuscript:** Proposal stage.

**Publication status:** Not submitted.

## 21. References

References will be added after the literature review is completed and the cited sources have been verified.
