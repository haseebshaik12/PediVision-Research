# Multimodal Deep Learning for Pediatric Brain Tumor Classification Using MRI and Clinical Information

## PediVision AI

**Research Manuscript**

**Author:** Haseeb Pasha  
**Program:** Bachelor of Technology in Computer Science and Engineering — Artificial Intelligence and Machine Learning 
**Institution:** Garden City University

---

## Abstract

Pediatric brain tumors represent a challenging area of clinical research, where magnetic resonance imaging (MRI) provides important information for tumor characterization while clinical information may provide complementary patient-level context. This study proposes PediVision AI, a multimodal deep-learning framework for pediatric brain tumor classification using MRI and associated clinical information.

The primary objective is to investigate whether combining MRI-derived representations with relevant clinical information improves classification performance compared with MRI-only and clinical-information-only approaches. The proposed framework consists of three experimental settings: an MRI-only model, a clinical-only model, and a multimodal model that integrates representations from both modalities.

The study will use an appropriately authorized and deidentified pediatric brain tumor dataset. The Children's Brain Tumor Network (CBTN) is being pursued as the primary research resource. Dataset-specific characteristics, including the final cohort size, MRI sequences, clinical variables, diagnostic categories, and class distribution, will be verified after authorized access and will not be assumed in advance.

The methodology incorporates patient-level dataset partitioning to reduce information leakage, standardized MRI and clinical preprocessing, deep-learning-based representation learning, multimodal feature fusion, and evaluation using accuracy, precision, recall, F1-score, Matthews correlation coefficient, and confusion matrices. Explainability methods such as Grad-CAM may additionally be used to investigate model behavior.

The study is designed to determine whether multimodal integration provides measurable predictive value beyond individual modalities. The findings will contribute to the evaluation of multimodal artificial intelligence approaches for pediatric brain tumor classification and may provide a reproducible framework for future pediatric neuro-oncology research.

**Keywords:** Pediatric brain tumor, magnetic resonance imaging, MRI, deep learning, multimodal learning, medical image analysis, clinical information, Vision Transformer, ResNet, artificial intelligence.


# 1. Introduction

Pediatric brain tumors represent an important and challenging area of pediatric
neuro-oncology. Accurate characterization of these tumors can support research
into diagnosis, prognosis, treatment planning, and patient management. Magnetic
resonance imaging (MRI) is particularly important because it provides detailed
information about brain anatomy and tumor appearance across different imaging
sequences.

The increasing availability of medical imaging datasets has enabled the
development of artificial intelligence (AI) methods for automated medical image
analysis. In particular, deep-learning models can learn complex representations
from MRI data and have been investigated for brain tumor detection,
segmentation, classification, and prognosis.

However, pediatric brain tumor research presents several challenges. Pediatric
tumors differ from adult brain tumors in their biological characteristics,
clinical presentation, and distribution. Furthermore, pediatric datasets can
be limited in size and heterogeneous in terms of imaging protocols, tumor
categories, and available clinical information. Consequently, models developed
using adult datasets cannot automatically be assumed to generalize to pediatric
populations.

The Children's Brain Tumor Network (CBTN) provides an important research
resource for addressing some of these challenges by bringing together
pediatric brain tumor imaging and associated clinical research information.
CBTN-based imaging research has demonstrated the feasibility of applying
deep-learning approaches to pediatric brain tumor MRI classification.

A particularly relevant recent study investigated pediatric brain tumor
classification using CBTN MRI data and evaluated both ResNet50 and Vision
Transformer (ViT) architectures across different MRI sequences. The study also
investigated the fusion of MRI-derived information with patient age. Its
findings demonstrated the potential of deep learning for pediatric MRI
classification while also showing that the contribution of age information was
not consistently substantial across experimental configurations.

These findings raise an important research question. If a single clinical
variable such as age does not consistently provide additional predictive
information, it remains unclear whether a broader set of appropriately
verified clinical variables could provide complementary information when
combined with MRI-derived representations.

This motivates the development of PediVision AI, a multimodal deep-learning
framework designed to investigate pediatric brain tumor classification using
MRI and associated clinical information.

The central research question of this study is:

> Does combining MRI-derived features with relevant clinical information
> improve pediatric brain tumor classification compared with MRI-only and
> clinical-information-only approaches?

To investigate this question, PediVision AI will compare three experimental
settings. The first will use MRI information alone, the second will use
clinical information alone, and the third will integrate MRI-derived and
clinical representations through a multimodal fusion architecture.

This controlled comparison is important because multimodal integration should
not automatically be assumed to improve predictive performance. A multimodal
model may provide additional information, provide no meaningful improvement,
or potentially introduce additional complexity without improving
generalization. Therefore, the contribution of this study will be determined
empirically through consistent evaluation of the three experimental settings.

The study will additionally emphasize patient-level data partitioning,
reproducible preprocessing, appropriate evaluation metrics, and model
interpretability. These considerations are particularly important in medical
imaging research because repeated examinations from the same patient can
otherwise result in information leakage and overly optimistic performance
estimates.

The proposed research is intended as an academic research and classification
framework rather than a clinically validated diagnostic system. The final
conclusions will be based exclusively on experiments performed using the
authorized and verified research dataset.

# 2. Related Work

## 2.1 Artificial Intelligence in Pediatric Brain Tumor Imaging

Artificial intelligence has increasingly been investigated for the analysis of
pediatric brain tumor imaging, particularly for tumor detection, segmentation,
classification, and other clinical research tasks. A systematic review of
artificial intelligence applications in pediatric brain tumor imaging
identified substantial growth in this area while also highlighting the need
for further validation of model performance and clinical utility.

One of the major challenges in pediatric neuro-oncology research is the
availability of sufficiently large and well-characterized pediatric imaging
datasets. Pediatric brain tumors differ from adult tumors in their biological
characteristics, anatomical distribution, and clinical presentation.
Consequently, models developed exclusively using adult brain tumor datasets
cannot automatically be assumed to generalize to pediatric populations.

The Children's Brain Tumor Network (CBTN) has contributed to addressing this
challenge by providing a large, multi-institutional pediatric brain tumor
research resource containing imaging and associated clinical information.
The CBTN imaging resource provides an important foundation for developing and
evaluating pediatric-specific artificial intelligence approaches.

## 2.2 Deep Learning for MRI-Based Brain Tumor Analysis

Deep learning has become an important approach for medical image analysis
because neural networks can learn hierarchical representations directly from
imaging data. Convolutional neural networks (CNNs), in particular, have been
widely investigated for brain MRI analysis.

Residual neural networks provide an established architecture for deep image
representation learning. ResNet introduced residual learning through shortcut
connections, enabling the optimization of substantially deeper neural networks.
ResNet-based architectures have subsequently become widely used as feature
extractors in computer vision and medical imaging.

Transformer-based architectures provide an alternative approach to image
representation learning. Vision Transformer (ViT) models formulate image
classification using sequences of image patches and Transformer-based
self-attention. This approach has subsequently been investigated in medical
image analysis and brain MRI applications.

Brain tumor research has also demonstrated the importance of multiple MRI
sequences. Different sequences can provide complementary information about
tumor structure and tissue characteristics. However, MRI-based deep-learning
research continues to face challenges related to limited sample sizes,
heterogeneous imaging protocols, class imbalance, and generalization across
datasets.

These challenges are particularly important in pediatric research, where
available datasets can be smaller and more heterogeneous than large
general-purpose imaging datasets.

## 2.3 CBTN-Based Pediatric Brain Tumor Classification

A particularly relevant study by Tampu et al. investigated pediatric brain
tumor classification using deep learning on MRI data from the Children's Brain
Tumor Network. The study evaluated ResNet50 and Vision Transformer
architectures across multiple preoperative MRI sequences and investigated
different pretraining strategies.

The study also investigated fusion between MRI information and patient age. [1]
The results demonstrated that deep-learning models can learn useful
representations for pediatric brain tumor classification from MRI data.
However, the contribution of age fusion varied across experimental
configurations and did not consistently produce a substantial improvement over
image-only approaches.

This study is directly relevant to PediVision because it establishes an
important CBTN-based precedent for pediatric MRI classification and for
incorporating clinical information into an imaging model.

At the same time, the findings motivate further investigation into whether
clinical information beyond age can provide complementary predictive
information when combined with MRI-derived representations.

## 2.4 Multimodal Medical Artificial Intelligence

Multimodal learning aims to combine complementary information from different
data sources within a predictive model. In healthcare, these sources can
include medical images, structured clinical variables, laboratory measurements,
clinical text, pathology, and molecular information.

Medical imaging and electronic health record data provide an important example
of multimodal learning. Imaging data can contain spatial and structural
information, while structured clinical information can provide patient-level
context that may not be directly represented within the image.
Several studies and reviews have investigated strategies for combining imaging and non-imaging information using deep learning. [2, 3] These approaches include
early fusion, intermediate feature-level fusion, and late fusion of model
outputs.

However, multimodal learning does not inherently guarantee improved
performance. The contribution of an additional modality depends on factors
such as data quality, feature complementarity, missing information, sample
size, and the architecture used for fusion.

Therefore, multimodal integration should be treated as an empirical research
question rather than assuming that additional information will automatically
produce better predictions.

## 2.5 Multimodal Learning in Neuro-Oncology

Multimodal learning is particularly relevant to neuro-oncology because brain
tumor research can involve multiple complementary sources of information.

MRI provides spatial and structural information about the tumor, whereas
clinical variables can provide information about the patient and disease
context. Additional information such as pathology and molecular characteristics
may also be available in some research settings.

Previous research has demonstrated the feasibility of combining imaging with
clinical and other non-imaging information for brain tumor prediction and
prognosis. Although much of this literature focuses on adult glioma and
prognostic tasks rather than pediatric tumor classification, it provides
methodological support for investigating multimodal representation learning.

PediVision applies this broader multimodal concept to pediatric brain tumor
classification while maintaining a controlled comparison against unimodal
baselines.

## 2.6 Explainable Deep Learning

Interpretability is an important consideration when applying deep-learning
methods to medical imaging.

Gradient-weighted Class Activation Mapping (Grad-CAM) provides
class-discriminative localization maps that can be used to investigate image
regions associated with model predictions. For suitable convolutional
architectures, such techniques can provide insight into model behavior and
potential failure modes.

In PediVision, explainability methods may be applied to appropriate MRI models
to examine whether predictions are associated with meaningful image regions.

However, attribution maps will be interpreted as model-interpretability
evidence rather than as evidence of clinical diagnostic validity.

## 2.7 Research Gap

The existing literature establishes several important findings.

First, artificial intelligence has demonstrated potential for pediatric brain
tumor imaging, but validation, generalizability, and clinical utility remain
important challenges.

Second, CBTN provides an important pediatric brain tumor imaging resource that
can support research into deep-learning-based MRI analysis.

Third, established architectures such as ResNet and Vision Transformer provide
multiple approaches for learning representations from medical images.

Fourth, previous CBTN-based work has demonstrated the feasibility of pediatric
brain tumor classification using deep learning and has investigated the fusion
of MRI information with patient age.

However, existing work does not establish that adding clinical information will
consistently improve pediatric brain tumor classification. The limited or
variable benefit observed from age fusion motivates further investigation into
whether a broader set of verified clinical variables can provide complementary
predictive information.

Therefore, PediVision addresses the following research gap:

> Although previous work has demonstrated pediatric brain tumor classification
> using deep learning on CBTN MRI data and has investigated the fusion of MRI
> information with age, there remains a need to systematically evaluate whether
> a broader set of verified clinical information provides complementary
> predictive value when compared with controlled MRI-only and
> clinical-information-only baselines.

## 2.8 Proposed Contribution

PediVision will investigate this research question through three controlled
experimental settings:

1. **MRI-only:** classification using MRI-derived representations.
2. **Clinical-only:** classification using verified clinical variables.
3. **Multimodal:** classification using fused MRI-derived and clinical
   representations.

The primary contribution will be a controlled empirical assessment of whether
multimodal integration provides measurable predictive value beyond individual
modalities.

The study will additionally emphasize:

- Patient-level dataset partitioning
- Reproducible preprocessing
- Consistent evaluation procedures
- Multiple performance metrics
- Model interpretability
- Prevention of information leakage

The study will not assume that the multimodal model will outperform the
MRI-only model. Both positive and negative findings will be considered
scientifically meaningful.

# 3. Materials and Methods

## 3.1 Study Design

This study proposes a multimodal deep-learning framework for pediatric brain
tumor classification using magnetic resonance imaging (MRI) and associated
clinical information.

The primary objective is to determine whether integrating MRI-derived
representations with relevant clinical features provides improved
classification performance compared with models based exclusively on MRI or
clinical information.

Three experimental configurations will be investigated:

1. **MRI-only model:** uses MRI-derived information as the sole input modality.
2. **Clinical-only model:** uses verified clinical variables as the sole input
   modality.
3. **Multimodal model:** combines MRI-derived and clinical representations
   through a feature-fusion architecture.

All three configurations will be evaluated using a consistent experimental
protocol and a held-out test set.

## 3.2 Dataset and Data Access

The study will use an appropriately authorized and deidentified pediatric brain
tumor research dataset. The Children's Brain Tumor Network (CBTN) is being
pursued as the primary data resource because it provides pediatric brain tumor
imaging and associated research information.

CBTN describes its imaging resources as controlled-access resources containing
deidentified MRI and clinical imaging data. Access is subject to the
applicable research-resource request and data-use requirements.

At the time of manuscript preparation, the project is undergoing the
data-access process. Consequently, dataset-specific characteristics,
including the final number of subjects, MRI sequences, clinical variables,
diagnostic categories, and available labels, will be reported only after
authorized access and formal dataset verification.

## 3.3 Dataset Verification and Cohort Definition

Before model development, the received dataset will undergo a structured
verification process.

The following characteristics will be documented:

- Number of available subjects
- Patient identifiers
- Number and type of MRI examinations
- Available MRI sequences
- Imaging formats
- Clinical variables
- Diagnostic labels
- Class distribution
- Missing values
- Availability of matching MRI and clinical records
- Potential duplicate examinations
- Eligibility criteria

The final study cohort will be defined according to the availability and
quality of the required imaging and clinical information.

Records that do not satisfy the predefined inclusion criteria or cannot be
reliably linked across modalities will be excluded according to documented
criteria.

No dataset-specific inclusion or exclusion decisions will be finalized before
inspection of the authorized dataset.

## 3.4 MRI Preprocessing

MRI data will undergo standardized preprocessing before being provided to the
deep-learning models.

The planned preprocessing pipeline consists of:

1. MRI file validation
2. Image loading
3. Identification and handling of invalid or non-finite values
4. Intensity normalization
5. Spatial normalization or resampling where required
6. Conversion to the representation required by the selected architecture
7. Training-time augmentation where appropriate

The precise preprocessing parameters will be determined according to the
characteristics of the available MRI data.

If multiple MRI sequences are available, their suitability for inclusion will
be evaluated during dataset verification. The final sequence selection will be
reported explicitly in the completed manuscript.

Preprocessing operations that learn parameters from the data will be fitted
using the training set only and subsequently applied to validation and test
data to minimize information leakage.

## 3.5 Clinical Data Processing

Clinical variables available in the authorized dataset will be examined for
relevance, completeness, and potential information leakage.

Depending on the verified data types, preprocessing may include:

- Numerical feature normalization
- Categorical-variable encoding
- Missing-value handling
- Removal of redundant variables
- Removal of variables that directly encode the target outcome
- Feature consistency checks

Only clinical variables available before or independently of the target
classification will be considered appropriate model inputs.

The final set of clinical variables will be reported in the completed
manuscript after dataset verification.

## 3.6 Patient-Level Dataset Partitioning

To minimize information leakage, dataset partitioning will be performed at the
**patient level** rather than the individual MRI-examination level.

The dataset will be divided into:

- Training set
- Validation set
- Held-out test set

A patient will be assigned to only one partition.

Consequently, multiple MRI examinations belonging to the same patient will not
be distributed across training and evaluation sets.

The training set will be used for model optimization, the validation set for
model selection and hyperparameter decisions, and the held-out test set for
final performance evaluation.

The exact partition proportions will be documented with the final
experimental results.

## 3.7 MRI-Only Deep-Learning Model

The MRI-only experiment will evaluate deep-learning architectures capable of
learning representations directly from MRI data.

Candidate architectures include:

- ResNet-based convolutional neural networks
- Vision Transformer (ViT)

ResNet architectures provide hierarchical convolutional representations
through residual connections, whereas ViT architectures use self-attention
over image patches.

The final architecture will be selected based on the verified characteristics
of the dataset, including MRI dimensionality, sample size, available
sequences, computational requirements, and training stability.

Where appropriate, transfer learning may be evaluated as an additional
experimental configuration.

## 3.8 Clinical-Only Model

The clinical-only model will use the verified clinical variables as input.

The processed clinical feature vector will be passed through an appropriate
neural-network or machine-learning classification architecture.

This experiment provides an independent baseline for determining the predictive
contribution of clinical information without MRI-derived information.

The same patient-level data partitioning strategy will be used as in the
MRI-only and multimodal experiments.

## 3.9 Multimodal Fusion Model

The multimodal model will integrate representations learned from MRI and
clinical information.

The proposed architecture consists of two processing branches.

**MRI branch**

MRI input → MRI encoder → MRI feature representation

**Clinical branch**

Clinical variables → Clinical encoder → Clinical feature representation

The resulting representations will then be combined using a feature-level
fusion mechanism.

A candidate implementation is feature concatenation followed by one or more
fully connected layers and a classification head:

```text
MRI
 ↓
MRI Encoder
 ↓
MRI Feature Vector
        \
         \
          → Feature Fusion → Classification Head → Prediction
         /
        /
Clinical Features
 ↓
Clinical Encoder
 ↓
Clinical Feature Vector

## 3.10 Classification Objective

The final classification layer will produce predictions corresponding to the
verified target categories in the dataset.

For a multiclass classification problem, categorical cross-entropy may be used
as the primary training objective:

L = -Σ(y_c log(ŷ_c))

where C represents the number of verified target classes, y_c is the
ground-truth indicator for class c, and ŷ_c is the predicted probability for
that class.

The final number of classes will be determined from the actual dataset and
will not be assumed in advance.

## 3.11 Training Strategy

Model training will be performed using the training partition, while the
validation partition will be used for model selection and hyperparameter
optimization.

Potential training considerations include:

- Learning rate
- Batch size
- Number of training epochs
- Optimizer
- Weight regularization
- Early stopping
- Learning-rate scheduling
- Class-weighted loss where appropriate
- Training-set augmentation

Hyperparameters will be selected without using the held-out test set.

If class imbalance is identified, appropriate strategies such as class-weighted
loss or training-set sampling may be investigated.

## 3.12 Evaluation Metrics

The experimental models will be evaluated using multiple complementary
metrics.

### Accuracy

Accuracy measures the proportion of correctly classified samples.

### Precision

Precision measures the proportion of predicted positive instances that are
correct.

### Recall

Recall measures the proportion of relevant instances that are correctly
identified.

### F1-score

The F1-score provides a harmonic mean of precision and recall.

### Matthews Correlation Coefficient

Matthews correlation coefficient (MCC) will be included because it can provide
a useful summary of classification performance, particularly when class
distributions are imbalanced.

### Confusion Matrix

Confusion matrices will be used to examine class-specific prediction patterns
and identify systematic misclassification.

Where appropriate, macro-averaged or class-specific metrics will also be
reported.

## 3.13 Comparative Analysis

The primary comparison will evaluate whether the multimodal model provides
improved performance relative to the MRI-only and clinical-only models.

The comparison will use the same held-out test set and evaluation metrics
across experimental configurations.

The magnitude and consistency of performance differences will be examined
rather than relying solely on overall accuracy.

If sufficient data are available, additional statistical analyses may be
performed to assess uncertainty associated with model performance.

## 3.14 Explainability Analysis

Explainability techniques will be considered to investigate model behavior.

For suitable convolutional architectures, **Gradient-weighted Class
Activation Mapping (Grad-CAM)** may be used to generate class-discriminative
activation maps.

These maps will be examined to determine whether model predictions are
associated with meaningful regions of the MRI.

Explainability analysis will be treated as a mechanism for understanding model
behavior and potential failure modes rather than as evidence of clinical
diagnostic validity.

## 3.15 Reproducibility

To support reproducibility, the study will document:

- Dataset version or access identifier where applicable
- Cohort-selection criteria
- Dataset partitioning
- Random seeds
- MRI preprocessing configuration
- Clinical preprocessing configuration
- Model architecture
- Hyperparameters
- Training configuration
- Evaluation metrics
- Software dependencies

Patient-level research data will not be placed in the public GitHub repository.

The project repository will contain the reproducible analysis and
model-development code required to reproduce the computational workflow using
appropriately authorized data.

## 3.16 Data Leakage Prevention

Several measures will be used to reduce information leakage:

1. Patient-level rather than scan-level partitioning.
2. Isolation of the held-out test set until final evaluation.
3. Fitting preprocessing parameters only on training data where applicable.
4. Performing feature-selection decisions using training/validation data rather
   than the test set.
5. Avoiding clinical variables that directly encode the target.
6. Avoiding duplicate or near-duplicate patient examinations across partitions.

These procedures are particularly important in medical imaging because multiple
examinations from the same patient can otherwise result in overly optimistic
performance estimates.

## 3.17 Ethical and Data-Privacy Considerations

The study will use deidentified research data obtained through an appropriate
data-access process.

All data-use conditions associated with the approved resource will be
followed.

No personally identifiable patient information will be included in the public
research repository or manuscript.

The resulting model will be presented as a research system for automated
classification and not as a clinically validated diagnostic system.

# 4. Experimental Results

## 4.1 Experimental Evaluation Framework

The experimental evaluation is designed to determine whether incorporating clinical information alongside MRI-derived features provides additional predictive value for pediatric brain tumor classification. Three experimental settings will be evaluated under the same patient-level data partitioning strategy:

1. **MRI-only model:** classification using MRI-derived features.
2. **Clinical-information-only model:** classification using verified clinical variables.
3. **Multimodal model:** classification using a fusion of MRI-derived and clinical features.

The three settings will be evaluated using consistent training, validation, and testing procedures to enable a controlled comparison of their predictive performance.

At the current stage of the study, the CBTN dataset access and dataset-specific variable verification are still in progress. Therefore, numerical experimental results are not reported in this manuscript section until the approved dataset has been obtained, processed, and evaluated.

## 4.2 Evaluation Metrics

The performance of each experimental setting will be evaluated using multiple complementary metrics, including:

- Accuracy
- Precision
- Recall
- F1-score
- Matthews correlation coefficient (MCC)
- Confusion matrix

These metrics will be calculated on the held-out test set after patient-level partitioning. The use of multiple evaluation measures is intended to provide a more comprehensive assessment of classification performance, particularly where class distributions may be unequal.

## 4.3 MRI-Only Results

The MRI-only experiment will establish the performance of the deep-learning model using MRI-derived information without clinical variables.

The following results will be reported after completion of the experiments:

| Metric | MRI-Only |
|---|---:|
| Accuracy | To be determined |
| Precision | To be determined |
| Recall | To be determined |
| F1-score | To be determined |
| MCC | To be determined |

The corresponding confusion matrix will also be reported to examine class-specific prediction patterns.

## 4.4 Clinical-Information-Only Results

The clinical-information-only experiment will evaluate the predictive value of the verified clinical variables independently of MRI information.

| Metric | Clinical-Only |
|---|---:|
| Accuracy | To be determined |
| Precision | To be determined |
| Recall | To be determined |
| F1-score | To be determined |
| MCC | To be determined |

The final variables included in this experiment will depend on the clinical information made available through the approved dataset and verified during dataset intake.

## 4.5 Multimodal Results

The multimodal experiment will combine MRI-derived features with the selected and verified clinical information.

| Metric | Multimodal |
|---|---:|
| Accuracy | To be determined |
| Precision | To be determined |
| Recall | To be determined |
| F1-score | To be determined |
| MCC | To be determined |

The multimodal results will be compared directly with the MRI-only and clinical-information-only experiments using the same evaluation protocol.

## 4.6 Comparative Performance Analysis

The primary comparison will examine whether multimodal fusion provides measurable predictive improvement over the individual information sources.

The final comparison will be presented using a consolidated table:

| Experiment | Accuracy | Precision | Recall | F1-score | MCC |
|---|---:|---:|---:|---:|---:|
| MRI-only | To be determined | To be determined | To be determined | To be determined | To be determined |
| Clinical-only | To be determined | To be determined | To be determined | To be determined | To be determined |
| Multimodal | To be determined | To be determined | To be determined | To be determined | To be determined |

The comparison will be interpreted after the experiments are completed. Particular attention will be given to whether the multimodal model demonstrates consistent improvement across multiple evaluation metrics rather than relying on a single performance measure.

## 4.7 Explainability Results

Where supported by the final MRI model architecture, explainability analysis will be performed to examine the image regions contributing to model predictions.

For convolutional models, Grad-CAM or a comparable post-hoc visualization method may be used to generate activation maps. These visualizations will be examined qualitatively to assess whether model attention is concentrated in anatomically or diagnostically meaningful regions.

Explainability findings will be reported only after the corresponding trained models and predictions have been obtained.

## 4.8 Statistical and Reproducibility Considerations

Where appropriate, performance will be reported across repeated evaluation runs or cross-validation folds using mean and standard deviation. The exact reporting strategy will depend on the final dataset size, class distribution, and experimental design after dataset verification.

All reported numerical results will be generated directly from the finalized experimental pipeline and recorded with the corresponding dataset version, preprocessing configuration, model configuration, and random seed.

## 4.9 Current Experimental Status

The software infrastructure and experimental methodology for the PediVision AI study have been prepared and tested using synthetic or placeholder data where necessary for pipeline verification.

The actual CBTN dataset has not yet been incorporated into the experimental pipeline. Consequently, no numerical performance results from the target pediatric brain tumor cohort are claimed at this stage.

Once dataset access is approved and the data are received, the following sequence will be followed:

1. Verify the received dataset against the approved data request and official documentation.
2. Identify the eligible cohort and verified target labels.
3. Construct the patient-level dataset manifest.
4. Perform MRI and clinical preprocessing.
5. Generate patient-level training, validation, and test partitions.
6. Train the MRI-only model.
7. Train the clinical-information-only model.
8. Train the multimodal model.
9. Evaluate all models using the predefined metrics.
10. Generate comparative tables, confusion matrices, and explainability visualizations.
11. Record the final results for analysis in the Discussion section.

# 5. Discussion

## 5.1 Overview of the Study

This study investigates whether combining MRI-derived information with relevant clinical information can improve pediatric brain tumor classification compared with models based on MRI or clinical information alone. The study is designed as a controlled comparison of three experimental settings: MRI-only, clinical-information-only, and multimodal classification.

The primary objective is not to assume that multimodal learning will necessarily outperform single-modality approaches, but to determine whether the addition of verified clinical information provides measurable complementary predictive value within the studied pediatric brain tumor cohort.

## 5.2 Expected Contribution of Multimodal Learning

MRI provides important structural and imaging information for characterizing brain tumors. However, clinical information may provide additional contextual information that is not directly represented in the imaging data.

A multimodal model may therefore benefit from complementary information obtained from different sources. The proposed comparison allows this potential benefit to be evaluated systematically rather than attributing improvement to multimodal fusion without a controlled baseline.

If the multimodal model demonstrates improved performance over both MRI-only and clinical-information-only models, this would provide evidence that combining the two information sources may be beneficial for the studied classification task.

Conversely, if multimodal fusion does not improve performance, this would also constitute a meaningful finding. It could indicate that the available clinical variables provide limited additional predictive information beyond MRI-derived features, or that the selected fusion strategy does not effectively integrate the available modalities.

## 5.3 Relationship to Previous Research

Previous research has demonstrated the potential of deep learning for pediatric brain tumor classification using MRI data. Research has also investigated the incorporation of clinical information such as age into MRI-based classification models.

The present study extends this line of investigation by establishing a structured comparison between MRI-only, clinical-information-only, and multimodal approaches using verified clinical information available within the approved pediatric dataset.

The contribution is therefore positioned as a systematic experimental evaluation rather than a claim that multimodal learning itself is a new concept.

## 5.4 Importance of Patient-Level Evaluation

A major methodological consideration in medical imaging studies is preventing information leakage between training and evaluation data.

In this study, dataset partitioning is performed at the patient level rather than independently at the image level. This ensures that MRI examinations belonging to the same patient are not inadvertently distributed across different partitions.

Patient-level partitioning is particularly important when multiple imaging examinations or sequences are available for an individual patient. Without appropriate grouping, models may encounter highly similar information during training and testing, resulting in overly optimistic estimates of generalization performance.

## 5.5 Clinical Relevance

The intended contribution of PediVision AI is methodological and research-oriented. The system is designed to investigate automated classification using multimodal information and is not intended to replace clinical diagnosis or clinical decision-making.

If successful, the study may contribute to the broader investigation of AI-assisted analysis of pediatric neuro-oncology imaging by examining whether clinical context can complement image-based representations.

Any interpretation of clinical relevance will remain dependent on the characteristics of the final dataset, experimental results, and external validation.

## 5.6 Explainability and Model Interpretation

Model explainability is an important consideration in medical imaging research because predictive performance alone does not establish whether a model is relying on appropriate image information.

The proposed explainability analysis will investigate model activation patterns using an appropriate post-hoc visualization method, such as Grad-CAM for compatible convolutional architectures.

These visualizations will be used to examine the regions contributing to model predictions. They will be interpreted cautiously because activation maps do not independently establish clinical validity or causal reasoning.

## 5.7 Interpretation of Experimental Results

The final interpretation of this study will depend on the experimentally observed performance of the three model settings.

The following outcomes will be considered:

- If the multimodal model consistently outperforms the MRI-only model, this may indicate that the incorporated clinical information provides complementary predictive information.
- If the MRI-only model performs similarly to or better than the multimodal model, the additional clinical variables may provide limited benefit for the studied task.
- If the clinical-only model provides meaningful predictive performance, this may indicate that some verified clinical variables contain information relevant to the classification target.
- If performance varies substantially across evaluation metrics, the results will be interpreted using the complete metric profile rather than accuracy alone.

No conclusion regarding the superiority of multimodal learning will be made until the experiments have been completed on the approved dataset.

## 5.8 Research Integrity

The study follows a data-driven evaluation strategy in which numerical findings will be generated only after the approved dataset has been obtained and processed through the defined experimental pipeline.

Synthetic or placeholder data used during software development are intended only to verify implementation and are not considered evidence for the research hypothesis.

The final manuscript will distinguish clearly between methodological development, experimental observations, and conclusions supported by the actual dataset.

# 6. Limitations

Several limitations should be considered when interpreting the findings of this study.

## 6.1 Dataset Access and Availability

At the current stage of the research, access to the CBTN dataset is still in progress. Consequently, the final cohort size, available MRI sequences, clinical variables, diagnostic categories, and class distribution cannot yet be confirmed.

These characteristics will be reported only after the approved dataset has been received and verified against the relevant dataset documentation.

## 6.2 Dataset-Specific Generalizability

The study focuses on pediatric brain tumor data available through the selected research dataset. Therefore, findings obtained from the final cohort may not necessarily generalize to other institutions, populations, imaging protocols, or adult brain tumor populations.

External validation using an independent cohort would be required to assess broader generalizability.

## 6.3 Clinical Variable Availability

The usefulness of multimodal fusion depends on the clinical variables available in the approved dataset. Some potentially informative clinical characteristics may not be available, may contain missing values, or may not be suitable for inclusion in the final model.

The final clinical feature set will therefore be determined only after dataset verification.

## 6.4 MRI Heterogeneity

Pediatric brain tumor MRI data may contain variations in acquisition protocols, scanners, institutions, image quality, and available sequences. Such heterogeneity can affect model training and generalization.

The preprocessing pipeline is intended to reduce technically relevant variation while preserving diagnostically useful information. However, preprocessing cannot completely eliminate differences originating from heterogeneous data acquisition.

## 6.5 Sample Size and Class Distribution

The effective sample size available for the final classification task will depend on the verified inclusion criteria and availability of target labels.

If substantial class imbalance is present, performance metrics may differ across tumor categories. Appropriate evaluation metrics and patient-level partitioning will therefore be important when interpreting the final results.

## 6.6 Model and Fusion Strategy

The selected model architecture and multimodal fusion strategy may influence experimental performance. Different architectures, feature representations, fusion mechanisms, or hyperparameter configurations could produce different outcomes.

The experiments in this study therefore represent an evaluation of the defined methodology rather than evidence that one particular architecture or fusion strategy is universally optimal.

## 6.7 Lack of Clinical Deployment Validation

The proposed system is a research model and has not been clinically validated or evaluated as a diagnostic system.

Before any potential clinical application, additional validation would be required, including independent external validation, assessment of robustness, clinical evaluation, and appropriate regulatory and ethical review.

## 6.8 Explainability Limitations

Explainability methods such as Grad-CAM can provide useful visual indications of model attention, but they do not independently demonstrate that a model has learned clinically meaningful or causal features.

Interpretation of activation maps will therefore remain exploratory and will not be treated as proof of clinical validity.

## 6.9 Need for Future Validation

Future work should evaluate the methodology using additional independent pediatric cohorts where appropriate. Further research could also investigate alternative multimodal fusion strategies, additional clinical variables, self-supervised representation learning, transformer-based architectures, and more extensive explainability and robustness analyses.

# 7. Conclusion

This study presents the design of PediVision AI, a multimodal deep-learning framework for investigating pediatric brain tumor classification using MRI and clinical information. The research is structured around a controlled comparison of MRI-only, clinical-information-only, and multimodal approaches.

The central objective is to determine whether verified clinical information provides complementary predictive value when combined with MRI-derived representations. Rather than assuming that multimodal fusion will always provide superior performance, the proposed methodology evaluates this question empirically using consistent patient-level data partitioning and predefined evaluation metrics.

The study also incorporates methodological safeguards relevant to medical imaging research, including patient-level dataset partitioning, explicit dataset verification, reproducible preprocessing and training procedures, and careful separation between development-stage synthetic testing and experiments performed using the approved research dataset.

At the current stage, numerical performance conclusions cannot be established because the approved CBTN dataset has not yet been incorporated into the experimental pipeline. Final conclusions will therefore be based only on results obtained after dataset access, cohort verification, model training, and evaluation have been completed.

Future work will focus on completing dataset acquisition and verification, conducting the planned experiments, analyzing multimodal performance, evaluating model explainability, and assessing the generalizability of the resulting models using appropriate independent validation where feasible.

Overall, PediVision AI provides a structured research framework for studying multimodal artificial intelligence in pediatric brain tumor classification while maintaining a clear distinction between methodological development, experimental evidence, and clinically supported conclusions.

# 8. References

1. Tampu IE, Bianchessi T, Blystad I, Lundberg P, Nyman P, Eklund A, Haj-Hosseini N. Pediatric brain tumor classification using deep learning on MR images with age fusion. *Neuro-Oncology Advances*. 2025;7(1):vdae205. doi:10.1093/noajnl/vdae205.

2. Huang SC, Pareek A, Seyyedi S, Banerjee I, Lungren MP. Fusion of medical imaging and electronic health records using deep learning: a systematic review and implementation guidelines. *npj Digital Medicine*. 2020;3:136. doi:10.1038/s41746-020-00341-z.

3. Cui C, Yang H, Wang Y, Zhao S, Asad Z, Coburn LA, Wilson KT, Landman BA, Huo Y. Deep multimodal fusion of image and non-image data in disease diagnosis and prognosis: a review. *Progress in Biomedical Engineering*. 2023;5(2):10. doi:10.1088/2516-1091/acc2fe.

4. He K, Zhang X, Ren S, Sun J. Deep residual learning for image recognition. In: *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*. 2016:770-778. doi:10.1109/CVPR.2016.90.

5. Dosovitskiy A, Beyer L, Kolesnikov A, et al. An image is worth 16x16 words: Transformers for image recognition at scale. In: *International Conference on Learning Representations*. 2021.

6. Selvaraju RR, Cogswell M, Das A, Vedantam R, Parikh D, Batra D. Grad-CAM: Visual explanations from deep networks via gradient-based localization. In: *Proceedings of the IEEE International Conference on Computer Vision (ICCV)*. 2017:618-626. doi:10.1109/ICCV.2017.74.

7. Children's Brain Tumor Network. CBTN Research Resources and Data Access. Children's Brain Tumor Network. Available from: https://cbtn.org/research/platforms/.

8. Children's Brain Tumor Network. FAQs: CBTN Research. Children's Brain Tumor Network. Available from: https://cbtn.org/faqs/.
