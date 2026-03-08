function startChat() {

    document.getElementById("landing").style.display = "none";
    document.getElementById("chatPage").style.display = "block";

    const chatBox = document.getElementById("chatBox");

    chatBox.innerHTML += `
        <div class="bot">
        Hey hi, please tell me which quotes you want for today
        (Inspirational / Motivational / Success / Love / Funny)
        </div>
    `;

}


function sendMessage() {

    const input = document.getElementById("message");
    const message = input.value.trim();

    if (message === "") return;

    const chatBox = document.getElementById("chatBox");

    /* USER MESSAGE */

    chatBox.innerHTML += `
        <div class="user">${message}</div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;

    input.value = "";

    /* SEND MESSAGE TO RASA */

    fetch("http://localhost:5005/webhooks/rest/webhook", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            sender: "user",
            message: message
        })
    })

    .then(response => response.json())

    .then(data => {

        if (data.length === 0) {
            chatBox.innerHTML += `
                <div class="bot">Sorry, I didn't understand.</div>
            `;
        }

        data.forEach(function(msg) {

            chatBox.innerHTML += `
                <div class="bot">${msg.text}</div>
            `;

        });

        chatBox.scrollTop = chatBox.scrollHeight;

    })

    .catch(error => {

        chatBox.innerHTML += `
            <div class="bot">Server error. Please try again.</div>
        `;

    });

}


/* ENTER KEY SEND MESSAGE */

document.addEventListener("DOMContentLoaded", function () {

    const input = document.getElementById("message");

    input.addEventListener("keypress", function(event) {

        if (event.key === "Enter") {
            sendMessage();
        }

    });

});