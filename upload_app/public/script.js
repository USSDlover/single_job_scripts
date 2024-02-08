/**
 * Demo script to capture the user input environment
 */

const captureButton = document.getElementById('capture-button');
const fileInput = document.querySelector('input[type="file"]');

captureButton.addEventListener('click', () => {
    navigator.mediaDevices.getUserMedia({video: true})
        .then(stream => {
            // Create a video element to display the camera preview (optional)
            const video = document.createElement('video');
            video.srcObject = stream;
            video.play();

            // Create a temporary file to store the captured image
            const tempFile = new File([stream], 'photo.jpg', {type: 'image/jpeg'});

            // Trigger the file input to submit the captured image
            fileInput.files = [tempFile];
            fileInput.form.submit();
        })
        .catch(error => {
            console.error('Error accessing camera:', error);
        });
});
