import streamlit as st

st.set_page_config(page_title="Cheesecake 💖", layout="centered")

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>

/* 🌈 Background animation */
body {
    margin: 0;
    overflow: hidden;
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fbc2eb, #a6c1ee);
    background-size: 400% 400%;
    animation: gradientFlow 12s ease infinite;
    color: white;
    text-align: center;
}

@keyframes gradientFlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ✨ Particles */
.particle {
    position: fixed;
    font-size: 20px;
    animation: floatUp linear infinite;
    opacity: 0.7;
}

@keyframes floatUp {
    from { transform: translateY(100vh); }
    to { transform: translateY(-10vh); }
}

/* Container */
.container {
    margin-top: 40px;
    animation: fadeIn 1.5s ease;
}

@keyframes fadeIn {
    from {opacity: 0; transform: scale(0.95);}
    to {opacity: 1; transform: scale(1);}
}

/* Bunny */
.bunny {
    width: 220px;
    animation: floatBunny 3s ease-in-out infinite;
}

@keyframes floatBunny {
    0%,100% {transform: translateY(0);}
    50% {transform: translateY(-12px);}
}

/* Title */
h1 {
    font-size: 40px;
}

/* Buttons */
.button {
    height: 70px;
    width: 170px;
    font-size: 20px;
    border-radius: 25px;
    border: none;
    cursor: pointer;
    margin: 15px;
    backdrop-filter: blur(10px);
    transition: 0.3s;
}

.yes {
    background: rgba(40,167,69,0.85);
    box-shadow: 0 0 15px rgba(40,167,69,0.6);
}

.no {
    background: rgba(255,77,77,0.85);
    box-shadow: 0 0 15px rgba(255,77,77,0.6);
}

.button:hover {
    transform: scale(1.1);
}

/* Message */
.message {
    font-size: 24px;
    min-height: 50px;
    margin-top: 20px;
}

/* Typewriter */
.typewriter {
    border-right: 2px solid white;
    white-space: nowrap;
    overflow: hidden;
    display: inline-block;
    animation: typing 2s steps(30), blink 0.5s step-end infinite alternate;
}

@keyframes typing {
    from { width: 0 }
    to { width: 100% }
}

@keyframes blink {
    50% { border-color: transparent }
}

</style>
</head>

<body>

<div id="particles"></div>

<div class="container">
    <img class="bunny" src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif">
    <h1>Will you be my cheesecake? 🍰</h1>

    <button id="yesBtn" class="button yes" onclick="accept()">Yes 💚</button>
    <button id="noBtn" class="button no" onclick="noClick()">No ❤️</button>

    <div id="msg" class="message"></div>
</div>

<script>

/* ✨ particles */
const emojis = ["✨","💖","⭐","💫"];
for(let i=0;i<30;i++){
    let p = document.createElement("div");
    p.className = "particle";
    p.innerText = emojis[Math.floor(Math.random()*emojis.length)];
    p.style.left = Math.random()*100 + "vw";
    p.style.animationDuration = (5 + Math.random()*5) + "s";
    p.style.fontSize = (15 + Math.random()*20) + "px";
    document.body.appendChild(p);
}

/* Messages */
let noCount = 0;

const messages = [
"ദയവായി ആകാമല്ലോ 🥺",
"ഒന്ന് ചിന്തിച്ചു നോക്കൂ ❤️",
"ഇല്ല എന്ന് പറയരുതേ 😢",
"ദയവായി സമ്മതിക്കൂ 💕",
"നിനക്ക് ഇഷ്ടമാകും 🥹",
"ഞാൻ സീരിയസാണ് 😭",
"പ്ലീസ് ഇനി ഇല്ല പറയല്ലേ 🥺",
"നീ സമ്മതിച്ചാൽ ഞാൻ വളരെ ഹാപ്പിയാകും 💖",
"ഇത് എന്റെ ഹൃദയം ആണ് 😢",
"നീ അല്ലെങ്കിൽ ആരും വേണ്ട 😭",
"ഇനി ഞാൻ കരയാൻ പോകുന്നു 😭💔",
"ഒന്നു YES അമർത്തി നോക്കൂ 😌",
"നീ YES അമർത്തിയാൽ magic ഉണ്ടാകും ✨",
"ഇനി request mode ON 😤",
"100% ഉറപ്പ് നിനക്ക് ഇഷ്ടമാകും 💕",
"ഇത് destiny ആണ് 😎",
"ഇനി NO അമർത്തുന്നത് illegal ആണ് 🚫😂"
];

function typeText(text) {
    let msg = document.getElementById("msg");
    msg.innerHTML = "<span class='typewriter'>" + text + "</span>";
}

/* ❌ NO click */
function noClick() {

    let yesBtn = document.getElementById("yesBtn");
    let noBtn = document.getElementById("noBtn");

    typeText(messages[noCount % messages.length]);

    noCount++;

    // YES grows
    let scale = 1 + noCount * 0.04;
    yesBtn.style.transform = `scale(${scale})`;
    yesBtn.style.boxShadow = `0 0 ${10 + noCount*2}px rgba(40,167,69,0.9)`;

    // NO fades
    noBtn.style.opacity = Math.max(0.4, 1 - noCount*0.03);

    if(noCount > 25){
        typeText("😏 ഇനി YES മാത്രം ശരിയായ option ആണ്...");
    }

    if(noCount > 50){
        typeText("💖 ഞാൻ കാത്തിരിക്കും... നീ YES അമർത്തും വരെ 🥹");
    }
}

/* ✅ YES click (FULL ANIMATION) */
function accept() {

    document.body.innerHTML = `
    <style>

    body {
        margin:0;
        overflow:hidden;
        background: radial-gradient(circle, #ff9a9e, #fad0c4);
        display:flex;
        justify-content:center;
        align-items:center;
        height:100vh;
        flex-direction:column;
        font-family: 'Segoe UI';
        color:white;
        animation: fadeIn 1s ease;
    }

    @keyframes fadeIn {
        from {opacity:0;}
        to {opacity:1;}
    }

    .text {
        font-size: 42px;
        animation: pop 1s ease infinite alternate;
    }

    @keyframes pop {
        from {transform: scale(1);}
        to {transform: scale(1.1);}
    }

    .sub {
        font-size: 26px;
        margin-top: 10px;
    }

    .bunny {
        width: 220px;
        margin: 20px;
        animation: float 2s ease-in-out infinite;
    }

    @keyframes float {
        0%,100% {transform: translateY(0);}
        50% {transform: translateY(-15px);}
    }

    .heart {
        position: fixed;
        font-size: 24px;
        animation: floatUp linear infinite;
    }

    @keyframes floatUp {
        from {transform: translateY(100vh);}
        to {transform: translateY(-10vh);}
    }

    .confetti {
        position: fixed;
        width: 10px;
        height: 10px;
        animation: fall linear infinite;
    }

    @keyframes fall {
        from {transform: translateY(-10vh) rotate(0deg);}
        to {transform: translateY(100vh) rotate(360deg);}
    }

    </style>

    <div class="text">💖 യേയ്! 💖</div>
    <div class="sub">ഇനി നീ എന്റെ ചീസ്‌കേക്ക് ആണ് 🥰🍰</div>

    <img class="bunny" src="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif">
    `;

    // Confetti
    for(let i=0;i<80;i++){
        let c = document.createElement("div");
        c.className = "confetti";
        c.style.left = Math.random()*100 + "vw";
        c.style.background = ["#ff4d6d","#ffd166","#06d6a0","#118ab2"][Math.floor(Math.random()*4)];
        c.style.animationDuration = (2 + Math.random()*3) + "s";
        document.body.appendChild(c);
    }

    // Hearts
    for(let i=0;i<40;i++){
        let h = document.createElement("div");
        h.className = "heart";
        h.innerText = "💖";
        h.style.left = Math.random()*100 + "vw";
        h.style.animationDuration = (4 + Math.random()*4) + "s";
        document.body.appendChild(h);
    }
}

</script>

</body>
</html>
"""

st.components.v1.html(html_code, height=820)