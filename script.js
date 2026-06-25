function sendMessage() {
    let input = document.getElementById("user-input").value;
    let chatWindow = document.getElementById("chat-window");

    // Add user message to UI
    chatWindow.innerHTML += `<p>You: ${input}</p>`;

    // Simple Rule-Based Logic
    let response = "I'm not sure how to answer that.";
    let lowerInput = input.toLowerCase();

    if (lowerInput.includes("hello")) {
        response = "Hello! How can I help you today?";
    } else if (lowerInput.includes("name")) {
        response = "I am your Coffee-themed Chatbot.";
    }

    // Add bot response to UI
    chatWindow.innerHTML += `<p>Bot: ${response}</p>`;
    document.getElementById("user-input").value = "";
}
function sendMessage() {
    let inputField = document.getElementById("user-input");
    let input = inputField.value.trim(); // .trim() removes accidental spaces
    if (input === "") return; // Don't process empty clicks

    let chatWindow = document.getElementById("chat-window");

    // Add user message
    chatWindow.innerHTML += `<p><b>You:</b> ${input}</p>`;

    // Define rules clearly
    let lowerInput = input.toLowerCase();
    let response = "";

    // Exact word matching for better accuracy
    if (lowerInput.match(/\b(hello|hi|hey)\b/)) {
        response = "Hello! How can I help you today?";
    } else if (lowerInput.includes("name")) {
        response = "I am a  chatbot, nice to meet you!";
    } else {
        response = "That's an interesting point! I'm still learning, could you tell me more about that?";
    }

    // Add bot response
    chatWindow.innerHTML += `<p><b>Bot:</b> ${response}</p>`;
    
    // Clear input and scroll to bottom
    inputField.value = "";
    chatWindow.scrollTop = chatWindow.scrollHeight;
}