$(document).ready(function () {
    const dropdown = $("div.link-cont")

   $("svg.dropd").on('click', function() {
    dropdown.stop().slideToggle(200);
    $("#werk-m-link").removeClass("werk");
  });
});