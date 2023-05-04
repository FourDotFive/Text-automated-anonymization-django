function redactText(text, entities, tagsToRedact) {
    let diff = 0;
    entities.forEach(function(entity) {
        let tag;
        if (tagsToRedact.includes(entity.entity)) {
            switch (entity.entity) {
                case 'PER':
                    tag = '&ltPER&gt';
                    break;
                case 'LOC':
                    tag = '&ltLOC&gt';
                    break;
                case 'ORG':
                    tag = '&ltORG&gt';
                    break;
                case 'MISC':
                    tag = '&ltMISC&gt';
                    break;
                default:
                    tag = entity.word;
                    break;
            }
        } else {
            switch (entity.entity) {
                case 'PER':
                    tag = '<span style="background-color:rgb(255, 230, 230);padding: .0em;">' + entity.word + '</span>';
                    break;
                case 'LOC':
                    tag = '<span style="background-color:rgb(230, 255, 230);padding: .0em;">' + entity.word + '</span>';
                    break;
                case 'ORG':
                    tag = '<span style="background-color:rgb(230, 230, 255);padding: .0em;">' + entity.word + '</span>';
                    break;
                case 'MISC':
                    tag = '<span style="background-color:rgb(255, 255, 230);padding: .2em;">' + entity.word + '</span>';
                    break;
                default:
                    tag = entity.word;
                    break;
            }
        }

        text = text.slice(0, entity.start + diff) + tag + text.slice(entity.end + diff);
        diff += tag.length - (entity.end - entity.start);
    });
    return text;
}

function updateRedactedText() {
    // Get the checked tags
    let tagsToRedact = [];
    let checkboxes = document.querySelectorAll('.form-check-input');
    checkboxes.forEach(function(checkbox) {
        if (checkbox.checked) {
            tagsToRedact.push(checkbox.value);
        }
    });

    // Redact the text using the checked tags
    let redactedText = redactText(originalText, entities, tagsToRedact);

    // Update the redacted text on the page
    document.getElementById("redactedText").innerHTML = redactedText;
}

async function copyText() {
    var text = document.getElementById("redactedText");
    try {
        await navigator.clipboard.writeText(text.innerText);
        console.log('Text copied to clipboard');
    } catch (err) {
        console.error('Failed to copy text: ', err);
    }
}