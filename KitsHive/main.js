var bat = document.getElementById('c');
var charg = document.getElementById('p');
var latitude = document.getElementById('lat');
var longitude = document.getElementById('lon')
var host = document.getElementById('dom');
var map = document.getElementById('map')

hostName = window.location.hostname

host.innerText = hostName

navigator.geolocation.getCurrentPosition((pos) => {
  const lat = pos.coords.latitude;
  const lon = pos.coords.longitude;
  longitude.innerHTML = lon;
  latitude.innerHTML = lat;
  
  var platform = new H.service.Platform({
  'apikey': 'WMNVfAVCMtDfpO3P35xMFAOBbFv9irz7GV2JccMWDPA'
});

var defaultLayers = platform.createDefaultLayers();

// Instantiate (and display) a map object:
var map = new H.Map(
    document.getElementById('map'),
    defaultLayers.vector.normal.map,
    {
      zoom: 10,
      center: { lat: lat, lng: lon }
    });
 
  let battery = 'getBattery' in navigator;
  if (!battery) {
    alert("Your browser doesn't suppoet battery API");
  };
  
  let batteryObj = navigator.getBattery();
  batteryObj.then((data) => {
    bat.innerHTML = data.charging;
    charg.innerHTML = (data.level*100);
    console.log(data.level)
  })
});
