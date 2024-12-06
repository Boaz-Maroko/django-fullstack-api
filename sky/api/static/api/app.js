// define a function to get the tokens

const form = document.getElementById('myForm');

async function fetchAccessToken() {

    const tokenUrl = 'http://127.0.0.1:8000/api/token/';
    const userCredentials = {
        username: "yourusername",
        password: "yourpassword",
    };

    try {
        const response = await fetch(tokenUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(userCredentials),
        });
    
        if (!response.ok) {
            throw new Error(`Error: ${response.status} ${response.statusText}`);
        }
        const data = await response.json();
    
        localStorage.setItem('access_token', data.access);
        localStorage.setItem('refresh_token', data.refresh);
    
    } catch (error) { 
        console.error("Failed to fetch access token:", error.message);
    }
}

async function sendData() {

    const access_token = localStorage.getItem('access_token');
    const studentUrl = 'http://127.0.0.1:8000/api/students/';

    const formData = new FormData(form);

    try {
        const response = await fetch(studentUrl, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${access_token}`,
            },
            body: formData,
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const result = await response.json();
        console.log('Success:', result);
        alert('Form submitted successfully!');
    } catch (error) {
        console.error('Error submitting form:', error);
        alert('Failed to submit the form.');
    }
}

window.onload = async function() {
    await fetchAccessToken();
}

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    await sendData(event)
});