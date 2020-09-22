var pass = document.getElementById('ps')

var gen = document.getElementById('make')

var copy = document.getElementById('copy')


const chars = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","@","£","_","#","?"]


//console.log(finalPass)

// Password generator
const generatePassword = () => {
  var passw = []

for (let i=0; i<8;i++) {
  passw.push(chars[Math.floor(Math.random()*chars.length)])
}

const finalPass = passw.join('')

  pass.innerText = finalPass.toString()
}

gen.addEventListener("click", generatePassword)

//Clipboard copy

const copyToClipboard = () => {
  text = pass.innerText
  
  navigator.clipboard.writeText(text).then(
    alert(`You copied ${text} successfully `)
    )
}

copy.addEventListener('click', copyToClipboard)



