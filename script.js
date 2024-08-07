
const firebaseConfig = {
    apiKey: "AIzaSyBcTEVvxXmv5N8dJav4xNDRy5hXZRjVeM4",
    authDomain: "chatflow-59776.firebaseapp.com",
    databaseURL: "https://chatflow-59776-default-rtdb.firebaseio.com",
    projectId: "chatflow-59776",
    storageBucket: "chatflow-59776.appspot.com",
    messagingSenderId: "549003131640",
    appId: "1:549003131640:web:3f4a7b8cef4c0d8a2b990d",
    measurementId: "G-V2180PR5CR"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const database = firebase.database();

// Elements
const nameInput = document.getElementById('nameInput');
const submitButton = document.getElementById('submitButton');
const nameList = document.getElementById('nameList');

// Authentication state
auth.onAuthStateChanged(user => {
    if (user) {
        // User is signed in
        fetchDataFromFirebase();
    } else {
        // Redirect to login or handle user not signed in
        window.location.href = 'login.html';
    }
});

// Text input listener
nameInput.addEventListener('input', () => {
    submitButton.style.display = nameInput.value.trim() ? 'inline-block' : 'none';
});

// Submit button listener
submitButton.addEventListener('click', () => {
    const name = nameInput.value.trim();
    if (name) {
        const userEmail = auth.currentUser.email;
        const timestamp = Date.now();
        saveNameToFirebase(userEmail, name, timestamp);
    }
});

// Save name to Firebase
function saveNameToFirebase(email, name, timestamp) {
    const databaseRef = database.ref('names');
    const nameData = {
        email: email,
        name: name,
        timestamp: timestamp
    };

    databaseRef.push(nameData)
        .then(() => {
            alert('Name saved successfully');
            nameInput.value = '';
            fetchDataFromFirebase();
        })
        .catch(error => {
            alert('Failed to save name: ' + error.message);
        });
}

// Fetch data from Firebase
function fetchDataFromFirebase() {
    const userEmail = auth.currentUser.email;
    const databaseRef = database.ref('names');
    const query = databaseRef.orderByChild('email').equalTo(userEmail);

    query.on('value', snapshot => {
        nameList.innerHTML = '';
        snapshot.forEach(childSnapshot => {
            const nameEntry = childSnapshot.val();
            const nameElement = document.createElement('div');
            nameElement.className = 'name-entry';
            nameElement.innerHTML = `
                <span>${nameEntry.name}</span>
                <span class="timestamp">${new Date(nameEntry.timestamp).toLocaleString()}</span>
            `;
            nameList.appendChild(nameElement);
        });
    });
}
