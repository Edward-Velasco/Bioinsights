document.getElementById('load-data').addEventListener('click', function() {
    const formData= {
      id: 379
    };
    fetch('/api/submit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
      console.log('Form submit response:', data);
    })
    .catch(error => {
    console.error('Error submitting form:', error);
    });
});
