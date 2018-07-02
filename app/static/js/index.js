// Carousel
$(".carousel").carousel({
  interval: 4000,
  pause: false
});

var scrollLink = $("#scroll");

// Smooth scrolling
scrollLink.click(function(e) {
  e.preventDefault();
  $("body,html").animate(
    {
      scrollTop: $(this.hash).offset().top
    },
    1000
  );
});
