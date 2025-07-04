const express = require('express');
const app = express();
const port = 5000;

app.get('/',(req,res)=>{
    res.send("돌아가는 중");
})

app.listen(port,()=>{
    console.log("듣고 있어요")
})