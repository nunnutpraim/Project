const exepress = require("express")  //const ทำให้เราไม่สามารถใช้ express ไปแทนเป็นอย่างอื่นได้ เช่น exp = 10 จะเออเร่อ
const cors = require('cors')

const app = exepress()

app.use(exepress.json())
app.use(cors())

app.get("/", (req, res) => {
    //get = รับค่า
    const name = req.query.name
    res.json({
        name: "Hello " + name
    })
})

app.post("/user", (req, res) => {
    //post = create new user,game,product
    const name = req.body.name
    
    res.json({
        message: "Hello " + name
    })
})

app.listen(3000, () => {
    console.log("sever start succfully")
})  