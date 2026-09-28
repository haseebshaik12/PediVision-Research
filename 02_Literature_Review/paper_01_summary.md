## Detailed Methodology Notes

### Dataset Selection

* Initial downloaded dataset: 326 subjects.
* Subjects with tumor-type information: 273.
* Final analyzed cohort: 178 subjects.
* Final tumor categories: low-grade astrocytoma, ependymoma, and medulloblastoma.
* Image quality and tumor visibility were assessed before inclusion.

### MRI Preprocessing

* Brain extraction.
* Per-sequence intensity normalization and harmonization.
* Resampling to 1 mm isotropic resolution.
* Extraction of 2D transverse slices from the tumor region.
* Final image size: 224 × 224 pixels.
* ADC maps were derived from diffusion-weighted MRI data.

### Model Architecture

* ResNet50 image encoder.
* Vision Transformer (ViT) image encoder.
* Separate neural network for age information.
* Joint fusion of MRI and age feature vectors.
* Final classifier predicts one of three tumor types.

### Pretraining

The Methods section describes three pretraining strategies:

1. Supervised pretraining on ImageNet.
2. Self-supervised pretraining on BraTS.
3. Self-supervised pretraining on CBTN.

The exact relationship between these strategies and the abstract's description of two pretraining paradigms should be checked against the complete experimental results.

### Evaluation

* Repeated 5-fold stratified cross-validation, repeated 10 times.
* Subject-wise splitting into training, validation, and testing sets.
* Metrics: MCC, accuracy, AUC, precision, recall, and F1-score.
* Statistical comparisons using Wilcoxon tests with Bonferroni correction for multiple comparisons.

### Explainability

* Grad-CAM applied to ResNet50 and ViT models.
* PCA used to visualize learned feature representations.
* Explainability was used to investigate model attention, not to establish clinical reasoning.

### Implications for PediVision

The paper supports evaluating MRI-only and MRI-plus-clinical-information models under patient-level data splitting.

Potential extensions include testing additional verified clinical variables, evaluating missing modalities, and investigating generalization. These directions require further literature review and dataset feasibility checks.

### Remaining Questions

* [ ] Verify the exact paper title, author list, and publication year.
* [ ] Review the full supplementary materials.
* [ ] Confirm the precise training, validation, and test split procedure.
* [ ] Review the limitations reported by the authors.
* [ ] Investigate whether additional clinical variables are available in the intended dataset.
