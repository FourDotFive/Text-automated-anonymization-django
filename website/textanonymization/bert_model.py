from transformers import pipeline
from transformers import AutoModelForTokenClassification, BertTokenizerFast
from django.conf import settings


def combine_entities(results):
    processed_results = []

    for result in results:
        word = result["word"]
        entity = result["entity"].replace("I-", "").replace("B-", "")

        if word == '\'':
            word = '&#x2018;'

        if word.startswith("##"):
            # Combine words with '##' with the previous word
            prev_result = processed_results[-1]
            prev_result["word"] = prev_result["word"] + word[2:]
            prev_result["end"] = result["end"]
        else:
            # Add a new result to the list
            processed_results.append(
                {
                    "entity": entity,
                    "word": word,
                    "start": result["start"],
                    "end": result["end"],
                }
            )

    return processed_results


def anonymize_text(text: str, allowed_entity_labels=None):
    tokenizer = BertTokenizerFast.from_pretrained(str(settings.BASE_DIR) + "\\textanonymization\\model\\tokenizer\\")
    model_fine_tuned = AutoModelForTokenClassification.from_pretrained(str(settings.BASE_DIR) + "\\textanonymization\\model\\ner_model\\")
    nlp = pipeline("ner", model=model_fine_tuned, tokenizer=tokenizer)

    ner_results = nlp(text)

    combined_tokens = combine_entities(ner_results)

    return combined_tokens

