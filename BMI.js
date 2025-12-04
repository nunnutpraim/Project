const exepress = require("express")  //const ทำให้เราไม่สามารถใช้ express ไปแทนเป็นอย่างอื่นได้ เช่น exp = 10 จะเออเร่อ
const cors = require('cors')

const app = exepress()

app.use(exepress.json())
app.use(cors())

app.get("/BMI", (req, res) => {
    //get = รับค่า
    const hight = req.query.hight
    const weight = req.query.weight


    x = weight / (hight/100)**2

    if (x <= 18.4) {
        result = "ผอม" // Underweight
    } else if (x > 18.5 || x < 22.9) {
        result = "สมส่วน" // Normal/Ideal
    } else if (x > 23 || x < 24.9) {
        result = "ท้วม" // Overweight (Mild)
    } else {
        result = "อ้วน" // Obese
    }

    res.json({
            result: result,
    })
})


app.listen(3000, () => {
    console.log("sever start succfully")
})  