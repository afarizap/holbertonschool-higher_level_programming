$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  for (i of data.results) {
    $('UL#list_movies').append("<li>" + i.title + "</li>");
  }
});
