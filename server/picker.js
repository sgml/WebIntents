var decodeNameTransport = function(str) {
  return JSON.parse(window.atob(str.replace(/_/g, "=")));
};

attachEventListener(window, "load", function() {
  var intent = decodeNameTransport(window.name);   

  data = {};
  data.request = "startActivity";
  data.origin = window.name;
  data.intent = intent;

  // Send a message to itself, mainly for webkit. 
  window.postMessage(JSON.stringify(data), "*");

  window.resizeTo(300,300);
}, false);
