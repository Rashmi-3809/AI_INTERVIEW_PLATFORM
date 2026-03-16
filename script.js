let timer
let timeLeft = 30
let score = 0
let currentQuestion = 0
let questions = []

async function startQuiz(){

let response = await fetch("http://127.0.0.1:5000/ai_questions")

questions = await response.json()

showQuestion()

}

function showQuestion(){

clearInterval(timer)

timeLeft = 30

let quizDiv = document.getElementById("quiz")

let q = questions[currentQuestion]

quizDiv.innerHTML = `
<h3>${q.question}</h3>

<p>Time Left: <span id="time">${timeLeft}</span> seconds</p>

${q.options.map(option => 
`<button onclick="checkAnswer('${option}')">${option}</button>`
).join("<br><br>")}
`

timer = setInterval(() => {

timeLeft--

document.getElementById("time").innerText = timeLeft

if(timeLeft === 0){

clearInterval(timer)

currentQuestion++

if(currentQuestion < questions.length){
showQuestion()
}
else{
showResult()
}

}

},1000)

}
function checkAnswer(selected){

let correct = questions[currentQuestion].answer

if(selected === correct){
score++
}

currentQuestion++

if(currentQuestion < questions.length){
showQuestion()
}
else{
showResult()
}

}

function showResult(){

let quizDiv = document.getElementById("quiz")

quizDiv.innerHTML = `
<h2>Your Score: ${score}/${questions.length}</h2>
`

saveScore(username, score)   // ✅ correct place

}

async function saveScore(username, score){

let response = await fetch("http://127.0.0.1:5000/save_score",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({username,score})
})

let data = await response.json()

console.log(data.message)

}