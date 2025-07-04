const fs =require('fs');
const express = require('express');
const https =require('https');
const cors = require('cors');

const app = express();
const port = 5000;

app.use(cors());
app.use(express.json())

app.get('/',(req,res)=>{
    res.send("돌아가는 중");
})

app.post('/chat',(req,res)=>{
    console.log(`받은 메세지: ${JSON.stringify(req.body)}`)
    res.json({reply:'응답 테스트 완료'})
})

https.createServer({
    key:fs.readFileSync(`./key.pem`),
    cert: fs.readFileSync(`./cert.pem`)
},app).listen(port,()=>{
    console.log('Https 작동중')
})