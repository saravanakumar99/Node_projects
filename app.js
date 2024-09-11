const http = require('http')

const server =  http.createServer((req,res)=>{
    if(req.url == "/"){
        res.end("this is the home page")
    }
    if(req.url == "/about"){
        res.end("this is about me")
    }
    res.end(`<h1>oops</h1>`)
})

server.listen(5000)

