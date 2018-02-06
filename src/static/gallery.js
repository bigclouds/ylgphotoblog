$('#modal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var modal = $(this);
  var slide = modal.find(button.data('slide'));
  var title = slide.data('title');
  var description = slide.data('description');
  var imageUrl = slide.data('image');
  var tags = slide.data('tags');
  var date = slide.data('date');
  var pk = slide.data('pk');
  ($('.photo-title')).text(title);
  ($('.photo-description')).text(description);
  ($('.photo-tags')).text(tags);
  ($('.photo-date')).text(date);
  ($('.edit-link')).attr('href', '/admin/blog/photo/' + pk + '/change/')
  slide.addClass('active');
  slide.find('.carousel-image').attr('src', imageUrl);
  slide.find('.carousel-image').attr('alt', title);
});

$('#modal').on('hide.bs.modal', function (event) {
  var modal = $(this);
  modal.find('.carousel-item').each(function() {
  	$(this).removeClass('active');
  });
});

$('#carouselControls').on('slide.bs.carousel', function (event) {
  var carousel = $(this);
  var relatedTarget = $(event.relatedTarget);
  var title = relatedTarget.data('title');
  var description = relatedTarget.data('description');
  var imageUrl = relatedTarget.data('image');
  var tags = relatedTarget.data('tags');
  var date = relatedTarget.data('date');
  var pk = relatedTarget.data('pk');
  ($('.photo-title')).text(title);
  ($('.photo-description')).text(description);
  ($('.photo-tags')).text(tags);
  ($('.photo-date')).text(date);
  ($('.edit-link')).attr('href', '/admin/blog/photo/' + pk + '/change/');
  var carouselImage = relatedTarget.find('.carousel-image');
  carouselImage.attr('src', imageUrl);
  carouselImage.attr('alt', title);
});

