window.onload = function() {
    isAllowedFileType = function(fileType) {
        const allowedFileTypes = ['audio/wav', 'audio/x-wav', 'audio/aiff', 'audio/x-aiff', 'audio/flac'];
        return allowedFileTypes.includes(fileType);
    }
    
    const dropZone = document.querySelector('#drop-zone');
    const fileInput = document.querySelector('#id_file');
    
    fileInput.addEventListener('change', (e) => {
        const file = e.target.files[0];
        if (!isAllowedFileType(file.type)) {
            alert('Please upload a WAV, AIFF, or FLAC file');
            fileInput.value = ''; // Reset the file input
            return;
        }
    });
    
    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
    })
    
    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
    
        if (e.dataTransfer.files.length > 1) {
            alert('Please submit only one file');
            return;
        }
    
        if (!isAllowedFileType(e.dataTransfer.files.item(0).type)) {
            alert('Please upload a WAV, AIFF, or FLAC file');
            return;
        }
    
        console.log(e.dataTransfer.files);
        fileInput.files = e.dataTransfer.files;
        var files = e.dataTransfer.files;
        file = files.item(0);
        console.log(file.type);
    })
}
