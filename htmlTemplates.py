# Custom CSS for styling chat messages
css = '''
<style>
.chat-message {
    padding: 1.5rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
    transition: transform 0.3s ease-in-out;
    position: relative;
    overflow: hidden;
}

.chat-message.user {
    background-color: #2b313e;
}

.chat-message.bot {
    background-color: #475063;
}

.chat-message .avatar {
    width: 20%;
    transform: rotate(3deg);
}

.chat-message .avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
    transition: transform 0.3s ease-in-out;
}

.chat-message.user .avatar img {
    transform: rotate(-3deg);
}

.chat-message .message {
    width: 80%;
    padding: 0 1.5rem;
    color: #fff;
    font-family: 'Comic Sans MS', cursive;
    font-size: 1.2rem;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    transition: transform 0.3s ease-in-out;
}

.chat-message.user .message {
    text-align: right;
}

.chat-message:hover {
    transform: scale(1.02);
}

.chat-message:hover .avatar img {
    transform: rotate(0);
}

.chat-message:hover .message {
    transform: rotate(-2deg);
}

.chat-message .offering {
    position: absolute;
    top: 0;
    right: -100%;
    width: 100%;
    height: 100%;
    background-color: rgba(255, 255, 255, 0.2);
    transition: right 0.5s cubic-bezier(0.68, -0.55, 0.27, 1.55);
    display: flex;
    align-items: center;
    justify-content: center;
    pointer-events: none;
}

.chat-message:hover .offering {
    right: 0;
    pointer-events: all;
}
</style>
'''

# Templates for user and bot messages
bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://t4.ftcdn.net/jpg/02/29/75/83/360_F_229758328_7x8jwCwjtBMmC6rgFzLFhZoEpLobB6L8.jpg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://static.vecteezy.com/system/resources/previews/004/996/790/non_2x/robot-chatbot-icon-sign-free-vector.jpg">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''