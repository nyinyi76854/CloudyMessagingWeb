// Initialize Firebase
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

const database = firebase.database();
const auth = firebase.auth();

// Function to send notification
function sendNotification(receiverEmail, message) {
    // Retrieve FCM token for the receiverEmail
    database.ref('users').orderByChild('email').equalTo(receiverEmail).once('value')
        .then(snapshot => {
            const user = snapshot.val();
            if (user) {
                const fcmToken = Object.values(user)[0].fcmToken;
                if (fcmToken) {
                    fetch('https://fcm.googleapis.com/fcm/send', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Authorization': 'key=AAAAf9Mi-vg:APA91bG78wl9hvVgAbAxpCp-9bVv6IynCwjukaoZa4CNeWxfvcGRmtDS6U1t8oOXMt8MWcgSwMT0o8gXPd8F3snCO0FSYVZAR9WezPVWOaqdteNt3ikj9ug3qOrfPtZPfsyDZpOEOwUd'
                        },
                        body: JSON.stringify({
                            to: fcmToken,
                            notification: {
                                title: 'New Message',
                                body: message,
                                sound: 'default'
                            }
                        })
                    }).then(response => response.json())
                      .then(data => console.log('Notification sent:', data))
                      .catch(error => console.error('Error sending notification:', error));
                }
            }
        })
        .catch(error => console.error('Error retrieving FCM token:', error));
}

// Function to display messages
function displayMessages() {
    const messagesRef = database.ref('messages');
    messagesRef.on('value', (snapshot) => {
        const messages = snapshot.val();
        const messageList = document.getElementById('messageList');
        messageList.innerHTML = '';

        for (const key in messages) {
            if (messages.hasOwnProperty(key)) {
                const message = messages[key];
                const messageItem = document.createElement('li');
                messageItem.textContent = `From: ${message.senderEmail}, To: ${message.receiverEmail}, Message: ${message.text}, Sent at: ${new Date(message.sentTime).toLocaleString()}`;
                messageList.appendChild(messageItem);
            }
        }
    });
}

// Call displayMessages on page load
window.onload = displayMessages;
