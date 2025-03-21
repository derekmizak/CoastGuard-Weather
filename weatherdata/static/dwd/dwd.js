  $(document).ready(function(){

    $("#btn-json-display").click(function(){
      fetch('/dwdcoastwarnings/', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        document.getElementById('json-display').innerHTML = data.html;
      })
      .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        $("#result").text('An error occurred!');  // Update DOM in case of an error
      });
    });
  });