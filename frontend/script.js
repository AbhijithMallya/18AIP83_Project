
// function previewImage(event) {
//   var fileInput = event.target;
//   var file = fileInput.files[0];
//   var imagePreview = document.getElementById('imagePreview');

//   if (file) {
//     var reader = new FileReader();
//     reader.onload = function(e) {
//       imagePreview.src = e.target.result;
//     };
//     reader.readAsDataURL(file);
//   } else {
//     imagePreview.src = "#";
//   }
// }

// function uploadImage() {
//   var formData = new FormData();
//   var fileInput = document.getElementById('imageInput');
//   formData.append('file', fileInput.files[0]);

//   var xhr = new XMLHttpRequest();
//   xhr.open('POST', 'http://localhost:8000/generateCaption/', true);
//   xhr.setRequestHeader('Accept', 'application/json');
//   xhr.onreadystatechange = function() {
//     if (xhr.readyState === 4 && xhr.status === 200) {
//       var response = JSON.parse(xhr.responseText);
//       document.getElementById('response').innerHTML = JSON.stringify(response, null, 2);
//     }
//   };
//   xhr.send(formData);
// }
// // Function to read out the text generated from the image
// function convertToAudio() {
//   const captionDisplay = document.getElementById('captionDisplay');
//   const text = captionDisplay.textContent.trim(); // Get the text content from captionDisplay

//   // Create an instance of SpeechSynthesisUtterance
//   const utterance = new SpeechSynthesisUtterance();
//   utterance.text = text;

//   // Speak the text
//   speechSynthesis.speak(utterance);

//   // Set the audio source (optional, depends on your requirements)
//   const audioPlayer = document.getElementById('audioPlayer');
//   audioPlayer.src = `data:audio/wav;base64,${btoa(text)}`;
// }

function previewImage(event) {
  var fileInput = event.target;
  var file = fileInput.files[0];
  var imagePreview = document.getElementById('imagePreview');

  if (file) {
    var reader = new FileReader();
    reader.onload = function(e) {
      imagePreview.src = e.target.result;
    };
    reader.readAsDataURL(file);
  } else {
    imagePreview.src = "#";
  }
}

 async function uploadImage() {
  var formData = new FormData();
  var fileInput = document.getElementById('imageInput');
  formData.append('file', fileInput.files[0]);

  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'http://localhost:8000/generateCaption/', true);
  xhr.setRequestHeader('Accept', 'application/json');
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var response = JSON.parse(xhr.responseText);
      document.getElementById('response').innerHTML = JSON.stringify(response, null, 2);
    }
  };
  xhr.send(formData);

// Function to read out the text generated from the image
  const captionDisplay = await document.getElementById('response');
  const text = captionDisplay.textContent.trim(); // Get the text content from captionDisplay
console.log("**********text**************\n",text)
console.log("**********CaptionDisplay**************\n",captionDisplay)
  // Create an instance of SpeechSynthesisUtterance
  const utterance = new SpeechSynthesisUtterance();
  utterance.text = text;

  // Speak the text
  speechSynthesis.speak(utterance);

  // Set the audio source (optional, depends on your requirements)
  // const audioPlayer = document.getElementById('audioPlayer');
  // audioPlayer.src = `data:audio/wav;base64,${btoa(text)}`;
}


