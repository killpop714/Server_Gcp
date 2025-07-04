const express = require('express');
const app = express();
const port = 5000;

app.get('/',(req,res)=>{
    res.send("돌아가는 중");
})

app.post('/chat',(req,res)=>{
    console.log(`받은 메세지: ${JSON.stringify(req.body)}`)
    res.json({reply:'응답 테스트 완료'})
})

app.listen(port,()=>{
    console.log("듣고 있어요")
})