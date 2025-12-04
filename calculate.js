const exepress = require("express")  //const ทำให้เราไม่สามารถใช้ express ไปแทนเป็นอย่างอื่นได้ เช่น exp = 10 จะเออเร่อ
const cors = require('cors')

const app = exepress()

app.use(exepress.json())
app.use(cors())

app.get("/plus", (req, res) => {
    //get = รับค่า
    const a = Number(req.query.a)
    const b = Number(req.query.b)

    const result = a + b

    res.json({
            result: result
    })
})

app.get("/minus", (req, res) => {
    //get = รับค่า
    const a = Number(req.query.a)
    const b = Number(req.query.b)

    result = a - b

    res.json({
            result: result,
    })
})

app.get("/multiply", (req, res) => {
    //get = รับค่า
    const a = Number(req.query.a)
    const b = Number(req.query.b)

    result = a * b

    res.json({
            result: result,
    })
})

app.get("/divide", (req, res) => {
    //get = รับค่า
    const a = Number(req.query.a)
    const b = Number(req.query.b)

    result = a / b

    res.json({
            result: result,
    })
})


app.listen(3000, () => {
    console.log("sever start succfully")
})  