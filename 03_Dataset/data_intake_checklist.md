# PediVision AI — Dataset Intake Checklist

## Purpose

This checklist will be used when the approved research dataset becomes available.

The purpose is to verify the dataset before any model training is performed.

---

## 1. Access Verification

- [ ] Confirm dataset was obtained through the approved access process.
- [ ] Confirm applicable Data Use Agreement requirements.
- [ ] Confirm permitted research use.
- [ ] Confirm whether redistribution is prohibited.
- [ ] Confirm that no identifiable patient information is stored in the repository.

---

## 2. Dataset Structure

- [ ] Record the dataset directory structure.
- [ ] Identify available data files.
- [ ] Identify MRI image files.
- [ ] Identify clinical-data files.
- [ ] Identify metadata files.
- [ ] Identify documentation provided with the dataset.

---

## 3. MRI Verification

Record the actual information provided by the dataset documentation.

- [ ] MRI file format
- [ ] Number of MRI records
- [ ] Number of unique subjects
- [ ] Available MRI sequences
- [ ] Image dimensions
- [ ] Voxel spacing
- [ ] Orientation information
- [ ] Missing MRI records
- [ ] Corrupted/unreadable files

Do not assume MRI sequences before verification.

---

## 4. Clinical Data Verification

- [ ] Identify the clinical-data file.
- [ ] Record the available variables.
- [ ] Record variable data types.
- [ ] Identify missing values.
- [ ] Identify categorical variables.
- [ ] Identify numerical variables.
- [ ] Identify subject/study identifiers.
- [ ] Identify variables relevant to the research question.

Do not assume that variables such as age, sex, diagnosis, treatment, or other clinical information are available until verified.

---

## 5. Target Label Verification

- [ ] Identify the official target-label variable.
- [ ] Document the label definition.
- [ ] Record the number of unique classes.
- [ ] Record class frequencies.
- [ ] Identify missing labels.
- [ ] Determine whether labels are appropriate for the research question.

No target labels will be invented or inferred without supporting dataset documentation.

---

## 6. MRI–Clinical Matching

- [ ] Identify the approved subject/study identifier.
- [ ] Determine how MRI records map to clinical records.
- [ ] Count successfully matched records.
- [ ] Identify unmatched MRI records.
- [ ] Identify unmatched clinical records.
- [ ] Investigate duplicate identifiers.
- [ ] Document the final matching procedure.

---

## 7. Cohort Definition

Before modeling, document:

- [ ] Inclusion criteria
- [ ] Exclusion criteria
- [ ] Number of eligible subjects
- [ ] Number of eligible MRI records
- [ ] Number of records with clinical information
- [ ] Number of records with target labels

All cohort decisions must be documented before final evaluation.

---

## 8. Data Leakage Check

- [ ] Confirm patient-level splitting.
- [ ] Confirm that the same patient does not occur across train/validation/test partitions.
- [ ] Confirm that test data is not used for model selection.
- [ ] Confirm that preprocessing parameters are learned only from training data where applicable.

---

## 9. Data Quality

- [ ] Check missing values.
- [ ] Check duplicate records.
- [ ] Check invalid numerical values.
- [ ] Check unreadable MRI files.
- [ ] Check unexpected image dimensions.
- [ ] Check inconsistent identifiers.
- [ ] Check unexpected label values.

---

## 10. Reproducibility

Record:

- Dataset version/date
- Access date
- Software environment
- Python version
- Package versions
- Random seeds
- Dataset split configuration
- Preprocessing configuration

---

## 11. Final Verification Before Training

Do not begin final model training until the following are confirmed:

- [ ] Dataset access is authorized.
- [ ] Dataset documentation has been reviewed.
- [ ] MRI structure is understood.
- [ ] Clinical variables are verified.
- [ ] Target labels are verified.
- [ ] MRI–clinical matching is verified.
- [ ] Cohort definition is documented.
- [ ] Patient-level split is established.
- [ ] No obvious data leakage is present.

---

## Important Research Rule

The actual dataset determines the final preprocessing and modeling decisions.

This checklist is a verification framework and does not assume that specific MRI sequences, clinical variables, cohort sizes, or target labels are available.