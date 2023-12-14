let map;

async function initMap() {
  const { Map } = await google.maps.importLibrary("maps");

  console.log('await over');
  map = new Map(document.getElementById("map"), {
    center: { lat: 52.397, lng: -9.5 },
    zoom: 12,
  });
}

initMap();

// https://developers.google.com/maps/documentation/javascript/examples/map-simple