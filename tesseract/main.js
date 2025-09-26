const tesseract = require("node-tesseract-ocr")

const config = {
  lang: "eng",
  oem: 1,
  psm: 3,
}

tesseract
  .recognize("C:\\Users\\Acer\\OneDrive\\Desktop\\OCRs\\public\\sample.jpg", config)
  .then(text => {
    console.log("Result:", text)
  })
  .catch(err => {
    console.error(err)
  })

