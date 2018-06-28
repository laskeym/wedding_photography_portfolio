// Isotope - Masonry Gallery
$(window).on("load", function() {
  $(".grid").isotope({
    itemSelector: ".grid-item",
    masonry: {}
  });
});

// Magnific Popup Gallery
$(".image-link").magnificPopup({
  type: "image",
  verticalFit: true,
  gallery: {
    enabled: true,
    navigateByImgClick: true
  }
});
