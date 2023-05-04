
document.addEventListener('DOMContentLoaded', function() {
    var textForm = document.querySelector('#text-form-div');
    var textArea = document.querySelector('[name="text"]');
    var charCountDisplay = document.getElementById('char-count-display');

    var updateCharCount = function() {
        var maxLength = parseInt(textArea.getAttribute('maxlength'));
        var currentLength = textArea.value.length;
        var remaining = maxLength - currentLength;
        charCountDisplay.textContent = remaining + ' characters remaining';
    };

    var validateForm = function() {
        var minLength = 10;
        var maxLength = 1024;
        var text = textArea.value.trim();
        if (text.length < minLength) {
            alert('Text must be at least ' + minLength + ' characters long.');
            return false;
        }
        if (text.length > maxLength) {
            alert('Text must not exceed ' + maxLength + ' characters.');
            return false;
        }
        return true;
    };

    textArea.addEventListener('input', updateCharCount);
    updateCharCount();
    textForm.addEventListener('submit', validateForm);
});

document.addEventListener('DOMContentLoaded', function() {
    var audioBtn = document.getElementById('audio-btn');
    var textBtn = document.getElementById('text-btn');
    var audioForm = document.getElementById('audio-form-div');
    var textForm = document.getElementById('text-form-div');

    audioBtn.addEventListener('click', function() {
        audioForm.style.display = 'block';
        textForm.style.display = 'none';
    });

    textBtn.addEventListener('click', function() {
        audioForm.style.display = 'none';
        textForm.style.display = 'block';
    });
});


