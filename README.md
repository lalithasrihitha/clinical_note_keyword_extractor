# clinical_note_keyword_extractor
A Natural Language Processing system that automatically extracts medications and diseases from clinical notes using AI-powered Named Entity Recognition.
# Clinical Keyword Extractor Using Named Entity Recognition

## Project Overview

This project addresses a critical challenge in medical informatics: extracting structured information from unstructured clinical text. Healthcare systems generate vast amounts of clinical notes daily, but the valuable information within these notes remains locked in free-text format. This system uses Named Entity Recognition to automatically identify and extract medications and diseases from clinical narratives, transforming unstructured medical text into structured, analyzable data.

The system processes real clinical notes from the MTSamples dataset, which contains approximately 5,000 medical transcriptions across 40 medical specialties. Using a pre-trained medical NER model trained on millions of biomedical documents, the system achieves high accuracy in identifying medical entities without requiring manually curated keyword lists or rule-based approaches.

## Why This Project Matters

Healthcare data analysis faces a fundamental challenge: approximately 80 percent of medical information exists in unstructured formats like clinical notes, radiology reports, and discharge summaries. While this data is rich with insights about patient conditions, treatment patterns, and outcomes, traditional data analysis methods struggle to process free-text narratives. Manual extraction is time-consuming, expensive, and impractical at scale. Rule-based systems require extensive domain expertise and constant maintenance as medical terminology evolves.

Named Entity Recognition represents a transformative approach to this problem. By leveraging deep learning models trained on extensive medical literature, NER systems can automatically identify medical concepts with accuracy approaching human performance. This capability enables numerous downstream applications including clinical decision support, adverse event detection, pharmacovigilance, population health analytics, and medical research acceleration. The ability to automatically extract medications and diseases from clinical notes at scale fundamentally changes how healthcare organizations can leverage their textual data assets.

This project demonstrates the practical application of NER technology to real clinical data. Rather than theoretical exploration, it processes actual medical transcriptions and produces actionable insights about medication usage patterns and disease prevalence across medical specialties. The system handles the inherent messiness of real clinical text including abbreviations, misspellings, varied terminology, and complex medical jargon. The false positive filtering mechanism addresses a critical real-world challenge where NER models may incorrectly classify laboratory values or other medical measurements as medications.

## Project Highlights

- Analyzed 4,999 clinical notes from 40+ medical specialties
- Extracted 18,345 medication mentions comprising 1,795 unique medications
- Identified 60,529 disease mentions comprising 5,627 unique diseases
- Achieved approximately 90 percent accuracy with false-positive filtering
- Generated professional visualizations for data insights
- Processing time of approximately 10 minutes for the complete dataset
- Implemented robust NER pipeline using pre-trained medical models

## Key Results

### Summary Statistics

| Metric | Count |
|--------|-------|
| Clinical Notes Analyzed | 4,999 |
| Total Medication Mentions | 18,345 |
| Unique Medications | 1,795 |
| Total Disease Mentions | 60,529 |
| Unique Diseases | 5,627 |
| Processing Time | ~10 minutes |

### Distribution

Medications represent 23.3 percent of total entities while diseases represent 76.7 percent of total entities, reflecting the diagnostic focus of clinical documentation where physicians extensively document symptoms, conditions, and differential diagnoses.

### Top 5 Medications Discovered

1. Lidocaine with 509 mentions serves as a local anesthetic
2. Marcaine with 506 mentions also known as bupivacaine
3. Epinephrine with 255 mentions used as an emergency medication
4. Xylocaine with 231 mentions representing a lidocaine variant
5. Aspirin with 230 mentions functioning as a blood thinner

### Top 5 Diseases and Symptoms Discovered

1. Pain with 3,437 mentions represents the most common complaint
2. Bleeding with 1,287 mentions
3. Fracture with 773 mentions
4. Infection with 757 mentions
5. Tumor with 755 mentions

## Features

### Core Functionality

The system employs AI-powered NER using pre-trained medical models specifically the en_ner_bc5cdr_md model. Automatic entity extraction eliminates the need for manual keyword lists. False positive filtering removes lab values and non-medications from results. Statistical analysis provides frequency distribution and counting. Data visualizations generate professional charts and graphs. Batch processing efficiently handles over 5,000 documents.

### Technical Features

The implementation features clean modular code architecture with comprehensive error handling. Progress tracking monitors long-running processes. Formatted console output presents statistics clearly. PNG image generation creates publication-quality charts.

## Technologies Used

### Core Libraries

| Technology | Version | Purpose |
|-----------|---------|---------|
| Python | 3.11+ | Programming language |
| spaCy | 3.4.4 | NLP framework |
| scispacy | 0.5.1 | Medical NLP extension |
| matplotlib | 3.7+ | Data visualization |
| pandas | 2.0+ | Data processing (optional) |

### NER Model

The en_ner_bc5cdr_md model weighs 120 MB and recognizes CHEMICAL entities representing medications and DISEASE entities representing diagnoses. Training data comes from the BioCreative V CDR task corpus. The model achieves 85 to 95 percent accuracy on medical text.

## Installation

### Prerequisites

The system requires Python 3.11 or higher, pip package manager, minimum 4 GB RAM, and internet connection for model download.

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/clinical-keyword-extractor.git
cd clinical-keyword-extractor
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate on Mac or Linux
source .venv/bin/activate

# Activate on Windows
.venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
# Install core libraries
pip install spacy scispacy matplotlib

# Install medical NER model
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.1/en_ner_bc5cdr_md-0.5.1.tar.gz
```

### Step 4: Download Dataset

Visit MTSamples on Kaggle at https://www.kaggle.com/datasets/tboyle10/medicaltranscriptions to download the mtsamples.csv file. Place the file in the DATA directory within your project root.

### Verify Installation
```bash
python -c "import spacy; nlp = spacy.load('en_ner_bc5cdr_md'); print('Installation successful')"
```

## Usage Guide

The system provides three main scripts for different purposes, each demonstrating different aspects of NER functionality. Understanding when and how to use each script helps maximize the value extracted from the system.

The simple_extractor.py script demonstrates basic text preprocessing functionality. This script is primarily educational, showing how to clean and normalize clinical text before NER processing. Run it using python simple_extractor.py to see examples of text cleaning including case normalization, whitespace handling, and format standardization.

The NER_medication_finder.py script demonstrates entity extraction on individual clinical notes. This script is ideal for testing the NER model on specific text samples and understanding how entity recognition works at a granular level. Run the script using python NER_medication_finder.py which processes several pre-defined sample clinical notes and displays extracted entities with their labels.

The analyze_dataset.py script represents the main analysis pipeline processing the entire MTSamples dataset. This is the primary script for production analysis and generates comprehensive statistics and visualizations. Run it using python analyze_dataset.py which initiates processing of all 4,999 clinical notes in the dataset. The script displays progress updates every 100 notes, allowing you to monitor the analysis as it proceeds.

## Project Structure
```
clinical-keyword-extractor/
│
├── analyze_dataset.py              # Main analysis script
├── NER_medication_finder.py        # NER demo and testing
├── simple_extractor.py             # Text preprocessing utilities
│
├── DATA/
│   └── mtsamples.csv              # Clinical notes dataset
│
├── results_and_visualizations/
│   ├── clinical_keywords_visualization.png
│   └── medications_vs_diseases_pie.png
│
├── .venv/                          # Virtual environment
├── README.md                       # This file
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore rules
└── LICENSE                         # MIT License
```

## Implementation Details

The implementation leverages modern NLP libraries and follows software engineering best practices for readability, maintainability, and performance. The code structure balances simplicity for educational purposes with robustness for real data processing.

The find_medications function encapsulates the core entity extraction logic. It accepts a text string containing a clinical note and returns two lists containing extracted medications and diseases respectively. The function begins by processing the text through the NER model using nlp(text) which returns a Doc object containing the analyzed text with identified entities. It initializes empty lists for collecting medications and diseases and defines the false_positives set containing terms to filter from medication results.

The entity extraction loop iterates over doc.ents, the collection of identified entities. For each entity, the code checks its label using entity.label_ which returns a string indicating the entity type. If the label equals CHEMICAL, the entity potentially represents a medication. The code then applies the false positive filter checking if entity.text.lower() appears in the false_positives set. Only entities passing this filter are appended to the medications list. If the label equals DISEASE, the entity is appended to the diseases list without additional filtering.

## Data Analysis and Findings

The analysis revealed several interesting patterns in clinical documentation that align with known medical practices while also surfacing some unexpected findings worth deeper investigation.

Medication frequency analysis showed a strong skew toward anesthetic agents with lidocaine and Marcaine dominating the results. This pattern suggests the MTSamples dataset contains a significant proportion of procedural notes where local anesthesia administration is routinely documented. The prevalence of epinephrine, often used in combination with local anesthetics to prolong their effect and reduce bleeding, supports this interpretation.

Disease mention patterns reflected the symptomatic focus of clinical documentation. Pain dominating with 3,437 mentions makes clinical sense as pain is the presenting complaint across numerous conditions and medical specialties. The frequency of bleeding and fracture indicates substantial representation of emergency and trauma cases in the dataset.

The 3.3 to 1 ratio of disease to medication mentions reflects fundamental aspects of clinical documentation. Notes extensively cover patient history, review of systems, physical examination findings, assessment, and differential diagnosis, all rich in disease terminology. Medication documentation, while critical, typically concentrates in specific note sections.

## Challenges and Solutions

Several technical and domain-specific challenges emerged during development, each requiring careful consideration and iterative refinement of the approach.

The false positive problem represented the most significant accuracy challenge. Initial results included numerous laboratory values and test results incorrectly classified as medications. Terms like creatinine, glucose, and potassium appear frequently in clinical notes but typically represent measured values rather than administered substances. The solution involved creating a curated false positive list based on manual inspection of results.

Case sensitivity in entity extraction created minor data quality issues where the same medication appeared multiple times with different capitalizations. The NER model preserves original text case which is appropriate for maintaining the fidelity of clinical language. However, for frequency analysis, variations should ideally count as the same medication.

Performance optimization required balancing processing speed with code clarity. Initial implementations loaded the NER model repeatedly for each note dramatically slowing processing. Moving model loading outside the processing loop reduced runtime from over an hour to approximately 10 minutes.

## Learnings and Insights

This project provided substantial learning opportunities spanning technical skills, domain knowledge, and practical data science experience.

The power of pre-trained models became immediately apparent. Rather than training a custom NER model requiring massive labeled datasets and computational resources, leveraging the en_ner_bc5cdr_md model provided excellent results out of the box. This model encodes years of research and training on millions of medical documents.

Understanding domain-specific NLP challenges deepened appreciation for medical informatics complexity. Medical language differs fundamentally from general text with extensive use of abbreviations, acronyms, technical terminology, and domain-specific syntax.

The importance of data quality and curation emerged as a recurring theme. While the MTSamples dataset provides valuable real-world data, its limitations around specialty distribution, note types, and documentation completeness affect result interpretation.

## Future Development

Several enhancement directions could extend the system's capabilities and improve its utility for medical informatics applications.

Relationship extraction represents a natural next step beyond entity identification. While the current system identifies medications and diseases independently, clinical value often lies in understanding their relationships. Which medications are prescribed for which conditions? What adverse events are associated with specific medications?

Temporal information extraction would add critical context to identified entities. When was a medication started or stopped? How long has a condition been present? Did symptoms appear before or after medication changes?

Entity normalization and linking to medical ontologies would improve data interoperability and analysis. Mapping extracted medications to RxNorm codes and diseases to SNOMED CT or ICD codes creates structured data compatible with other healthcare systems.

## Dataset Information

The MTSamples dataset serves as the foundation for this analysis providing real-world clinical text for entity extraction. Understanding the dataset's characteristics, limitations, and origins is essential for interpreting results appropriately.

MTSamples originated as a collection of medical transcription samples compiled from the MTSamples.com website. The dataset contains approximately 5,000 medical transcriptions spanning over 40 medical specialties. The notes represent various report types including history and physical examinations, consultation notes, operative reports, discharge summaries, and progress notes.

The data underwent de-identification to remove patient names, physician names, dates, and other identifying information before public release. The dataset carries a CC0 Public Domain license allowing unrestricted use for research and educational purposes.

## Performance Metrics

Quantifying system performance provides objective measures of effectiveness and identifies areas for improvement. Several metrics characterize different aspects of system performance.

Processing throughput measured in notes per minute indicates computational efficiency. The system processes approximately 500 notes per minute on a typical development laptop with processing time dominated by NER inference rather than I/O or data handling.

Entity extraction precision measuring how many extracted entities are correct suggests approximately 85 to 90 percent accuracy for the final filtered results based on manual inspection. False positives primarily arise from ambiguous terms that could be medications or test results depending on context.

## Dependencies

The project relies on several external libraries each serving specific purposes in the processing pipeline.

Python 3.11 or higher provides the core programming environment. spaCy version 3.4.4 serves as the foundational NLP framework. scispacy version 0.5.1 extends spaCy with biomedical and clinical text processing capabilities. The en_ner_bc5cdr_md model represents the pre-trained medical NER model. matplotlib version 3.7 or higher provides data visualization capabilities.

## License

This project is released under the MIT License, a permissive open source license allowing free use, modification, and distribution with minimal restrictions. The license requires only that the original copyright notice and license text be included in copies or substantial portions of the software.

## Acknowledgments

This project builds upon substantial work by the medical NLP research community and open source software developers whose contributions make projects like this possible.

The developers of spaCy created a high-quality NLP framework that balances performance with usability. The creators of scispacy from the Allen Institute for AI extended spaCy to biomedical and clinical domains. The authors and annotators of the BioCreative V Chemical Disease Relation corpus provided the training data for the NER model. The creators of the MTSamples dataset provided the real-world clinical text making this analysis possible.
