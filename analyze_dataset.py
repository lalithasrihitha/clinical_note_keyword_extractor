import csv
import spacy
from collections import Counter
import matplotlib.pyplot as plt

#loading the NER Model
print("loading NER model")
nlp=spacy.load("en_ner_bc5cdr_md")
print("Model loaded \n")


def find_medications(text):
    """ Find medications & diseases In text using NER"""
    doc = nlp(text)
    medications = []
    diseases = []

    # Filter out non-medications
    false_positives = {'creatinine', 'glucose', 'potassium', 'calcium',
                       'co2', 'cc', 'smoke', 'p.o', 'alcohol', 'oxygen'}

    for entity in doc.ents:
        if entity.label_ == "CHEMICAL":
            # Check if NOT in false positives
            if entity.text.lower() not in false_positives:  # ← This line!
                medications.append(entity.text)
        elif entity.label_ == "DISEASE":
            diseases.append(entity.text)

    return medications, diseases

#Opening the CSV File
print("Opening mtsamples.csv")

with open('DATA/mtsamples.csv', 'r' , encoding ='utf-8') as file:
     reader = csv.DictReader(file)

     #storing all medications & diseases found
     all_medications =[]
     all_diseases=[]

     #counter for progress
     note_count=0
     #processing each row(each clinical note)
     for row in reader:
         note_count +=1
         #showing progress every 100 notes
         if note_count % 100 == 0:
             print(f"Processed {note_count} notes")

         #getting the clinical note text
         clinical_note = row['transcription']

         #finding medications & diseases in this note
         medications,diseases =find_medications(clinical_note)

         #adding to collection
         all_medications.extend(medications)
         all_diseases.extend(diseases)

     print(f"\n finished! Processed {note_count} clinical notes")


# Counting frequencies
print("\n" + "="*50)
print("MEDICATION STATISTICS")
print("="*50)

medication_counts = Counter(all_medications)

print(f"\nTotal medications found: {len(all_medications)}")
print(f"Unique medications: {len(medication_counts)}")

print(f"\n Top 20 Most Common Medications:")
print("-" * 50)

for medication, count in medication_counts.most_common(20):
    print(f"{medication:30} → {count:4} times")

# NOW ADD DISEASE STATISTICS
print("\n" + "="*50)
print("DISEASE STATISTICS")
print("="*50)

disease_counts = Counter(all_diseases)

print(f"\nTotal diseases found: {len(all_diseases)}")
print(f"Unique diseases: {len(disease_counts)}")

print(f"\n Top 20 Most Common Diseases:")
print("-" * 50)

for disease, count in disease_counts.most_common(20):
    print(f"{disease:30} → {count:4} times")

# Save to file
with open('results_and_visualizations/results.txt', 'w') as f:
    f.write("MEDICATION STATISTICS\n")
    f.write(f"Top 20: {medication_counts.most_common(20)}\n")
    f.write("\nDISEASE STATISTICS\n")
    f.write(f"Top 20: {disease_counts.most_common(20)}\n")


# VISUALIZATIONS


print("\n" + "="*50)
print("CREATING VISUALIZATIONS...")
print("="*50)

# Visualization 1: Top 10 Medications Bar Chart
plt.figure(figsize=(12, 6))
top_10_meds = medication_counts.most_common(10)
meds_names = [item[0] for item in top_10_meds]
meds_counts = [item[1] for item in top_10_meds]

plt.subplot(1, 2, 1)  # 1 row, 2 columns, first plot
plt.barh(meds_names, meds_counts, color='skyblue')
plt.xlabel('Frequency')
plt.title('Top 10 Most Common Medications')
plt.gca().invert_yaxis()  # Highest at top

# Visualization 2: Top 10 Diseases Bar Chart
top_10_diseases = disease_counts.most_common(10)
disease_names = [item[0] for item in top_10_diseases]
disease_counts_list = [item[1] for item in top_10_diseases]

plt.subplot(1, 2, 2)  # 1 row, 2 columns, second plot
plt.barh(disease_names, disease_counts_list, color='lightcoral')
plt.xlabel('Frequency')
plt.title('Top 10 Most Common Diseases')
plt.gca().invert_yaxis()

plt.tight_layout()
plt.savefig('clinical_keywords_visualization.png')
print(" Saved: clinical_keywords_visualization.png")
plt.show()

# Visualization 3: Pie Chart - Medications vs Diseases
plt.figure(figsize=(8, 8))
labels = ['Medications', 'Diseases']
sizes = [len(all_medications), len(all_diseases)]
colors = ['skyblue', 'lightcoral']
explode = (0.1, 0)  # explode 1st slice

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Medications vs Diseases Distribution')
plt.savefig('medications_vs_diseases_pie.png')
print(" Saved: medications_vs_diseases_pie.png")
plt.show()
print("\n All visualizations created!")





