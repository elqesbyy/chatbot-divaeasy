const API_URL = "http://127.0.0.1:8000/chat";

async function sendMessage(){

    const input = document.getElementById("message");

    const message = input.value.trim();

    if(message === "")
        return;

    const chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += `
        <div class="user-message">
            ${message}
        </div>
    `;

    input.value = "";

    chatBox.scrollTop = chatBox.scrollHeight;

    try{

        const response = await fetch(API_URL,{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({

                message:message

            })

        });

        const data = await response.json();

        chatBox.innerHTML += `
            <div class="bot-message">
                ${data.answer}
            </div>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;

    }

    catch(error){

        chatBox.innerHTML += `
            <div class="bot-message">
                Impossible de contacter le serveur.
            </div>
        `;

    }

}