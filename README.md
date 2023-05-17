# Anonymizer: Text and Audio Anonymization using BERT NER Model and Django

Anonymizer is a web application that enables users to anonymize text and audio files containing human speech using a BERT-based Named Entity Recognition (NER) model. Built with the Django framework, this application provides a user-friendly interface to remove or replace sensitive information in both text and transcribed audio files.

## Features

- Secure user registration and login system
- Text submission and anonymization
- Audio file submission, transcription, and anonymization
- Real-time replacement of NER tokens with generic placeholders (e.g., `<PER>`, `<LOC>`)
- View, copy, and save anonymized text to personal account records
- Results Management: Provides the ability to view, copy, and save the anonymized text to personal account records. Users can also manage their records, including viewing and deleting specific entries.

## Model

The core of the Anonymizer application is a BERT-based Named Entity Recognition (NER) model that detects and classifies named entities in the submitted text or transcribed audio. The model is trained to recognize various entities such as person names, locations, and organizations. Upon identification, the model replaces these entities with generic placeholders to protect sensitive information.

## Usage

1. Begin by registering a new user account or logging into an existing one.
2. Submit text or an audio file containing human speech for anonymization.
3. View the anonymized text with replaced NER tokens in real-time.
4. Copy or save the anonymized text to your personal account records.
5. Access and manage your account records, including viewing and deleting specific records.