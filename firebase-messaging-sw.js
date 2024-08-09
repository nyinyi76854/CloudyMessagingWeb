importScripts('https://www.gstatic.com/firebasejs/8.10.1/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.10.1/firebase-messaging.js');

// Your web app's Firebase configuration
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

firebase.initializeApp(firebaseConfig);

const messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function(payload) {
    const title = 'Background Message Title';
    const options = {
        body: 'Background message body.',
        icon: '/firebase-logo.png'
    };

    return self.registration.showNotification(title, options);
});
