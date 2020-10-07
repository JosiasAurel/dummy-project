const gurl = 'https://covid19.mathdro.id/api'

// global data
let gdeaths = document.getElementById('gd')

let gcured = document.getElementById('gr')

let gcases = document.getElementById('gc')

// cameroon specific data

let deaths = document.getElementById('d')

let cured = document.getElementById('r')

let cases = document.getElementById('c')

// providing global data

fetch(gurl)
.then(response => {
  return response.json()
})
.then(data => {
  gcases.innerHTML = data.confirmed.value

  gdeaths.innerHTML = data.deaths.value
  
  gcured.innerHTML = data.recovered.value
  
})

// cameroon data endpoint

const curl = 'https://covid19.mathdro.id/api/countries/cameroon'

fetch(curl)
.then(response => {
  return response.json()
})
.then(data => {
  cases.innerHTML = data.confirmed.value
  
  deaths.innerHTML = data.deaths.value
  
  cured.innerHTML = data.recovered.value
})
