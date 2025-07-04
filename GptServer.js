const fs =require('fs');
const express = require('express');
const https =require('https');
const cors = require('cors');
const axios = require('axios');

const app = express();
const port = 5000;
const apiKey = "1";


app.use(cors());
app.use(express.json())

app.get('/',(req,res)=>{
    res.send("돌아가는 중");
})

app.post('/chat',async(req,res)=>{
    const message = req.body.message;
    console.log(`인지한 데이터: ${message}`)
    try {
        const response = await axios.post(
            'https://api.openai.com/v1/chat/completions',
            {
                model: 'gpt-4o',
                messages: [
                    { role: 'system', content: '너는 주변 환경을 인지하고 행동하는 NPC야.' },
                    { role: 'user', content: `주변에서 이런 걸 들었어: "${perception}". 어떤 생각이 들어?` }
                ]
            },
            {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${OPENAI_API_KEY}`
                }
            }
        );

        const gptReply = response.data.choices[0].message.content;
        console.log(`[Perceive] GPT 응답: ${gptReply}`);

        res.json({ reply: gptReply });
    } catch (error) {
        console.error('GPT 에러:', error.response ? error.response.data : error.message);
        res.status(500).json({ error: 'GPT 호출 실패' });
    }
});

https.createServer({
    key:fs.readFileSync(`./key.pem`),
    cert: fs.readFileSync(`./cert.pem`)
},app).listen(port,()=>{
    console.log('Https 작동중')
})