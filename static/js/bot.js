const toggleChatboxBtn = document.querySelector(".js-chatbox-toggle");
const chatbox = document.querySelector(".js-chatbox");
const chatboxMsgDisplay = document.querySelector(".js-chatbox-display");
const chatboxForm = document.querySelector(".js-chatbox-form");

// Use to create chat bubble when user submits text
// Appends to display
const createChatBubble = input => {
  const chatSection = document.createElement("p");
  chatSection.textContent = input;
  chatSection.classList.add("chatbox__display-chat");
  chatSection.classList.add("request");

  chatboxMsgDisplay.appendChild(chatSection);
};

const createChatBubble1 = input => {
    const chatSection = document.createElement("p");
    chatSection.textContent = input;
    chatSection.classList.add("chatbox__display-chat");
    chatSection.classList.add("response");
  
    chatboxMsgDisplay.appendChild(chatSection);
  };

// Toggle the visibility of the chatbox element when clicked
// And change the icon depending on visibility
toggleChatboxBtn.addEventListener("click", () => {
  chatbox.classList.toggle("chatbox--is-visible");

  if (chatbox.classList.contains("chatbox--is-visible")) {
    toggleChatboxBtn.innerHTML = '<i class="fa fa-chevron-down"></i>';
  } else {
    toggleChatboxBtn.innerHTML = '<i class="fa fa-chevron-up"></i>';
  }
});

// Form input using method createChatBubble
// To append any user message to display
chatboxForm.addEventListener("submit", e => {
    var chatInput = document.querySelector(".js-chatbox-input").value;
    createChatBubble(chatInput);
    var base_url = window.location.origin;
    action = base_url + '/api/chat/';
    var str = {
        "text": chatInput
    }
    $.ajax({
        type: "POST",
        url: action,
        data: str,
        success: function(msg) {
          if (msg.text) {
            chatInput = msg.text
            createChatBubble1(chatInput);
          }
        }
      });
  e.preventDefault();
  chatboxForm.reset();
});
