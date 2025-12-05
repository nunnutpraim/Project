const express = require("express")
const cors = require("cors")
const app = express()

app.use(cors())
app.use(express.json())

app.get("/me", (req, res) => {
    res.json({
        Name : "My name is Praim",
        Age :  "I am 17 years old",
        Sport : "I like to play sport such as Badminton and Football",
        Food : "I like to eat fried chicken, salmon sashimi and mashed potato",
        Hobbie : "I like to play games such as Valorent, Rov and Delta force",
        National : "I lived in Thailand"
    })
})

app.listen(3000, () => {
    console.log("Srever start successfully")
})