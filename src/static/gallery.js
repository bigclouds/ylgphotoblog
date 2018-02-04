$('#modal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var modal = $(this);
  var slide = modal.find(button.data('slide'));
  var title = slide.data('title');
  var description = slide.data('description');
  var tags = slide.data('tags');
  var date = slide.data('date');
  var pk = slide.data('pk');
  ($('.photo-title')).text(title);
  ($('.photo-description')).text(description);
  ($('.photo-tags')).text(tags);
  ($('.photo-date')).text(date);
  ($('.edit-link')).attr('href', '/admin/blog/photo/' + pk + '/change/')
  slide.addClass('active');
})

$('#modal').on('hide.bs.modal', function (event) {
  var modal = $(this);
  modal.find('.carousel-item').each(function() {
  	$(this).removeClass('active');
  });
})

$('#carouselControls').on('slide.bs.carousel', function (event) {
  var carousel = $(this);
  var relatedTarget = $(event.relatedTarget);
  var title = relatedTarget.data('title');
  var description = relatedTarget.data('description');
  var tags = relatedTarget.data('tags');
  var date = relatedTarget.data('date');
  var pk = relatedTarget.data('pk');
  ($('.photo-title')).text(title);
  ($('.photo-description')).text(description);
  ($('.photo-tags')).text(tags);
  ($('.photo-date')).text(date);
  ($('.edit-link')).attr('href', '/admin/blog/photo/' + pk + '/change/')
})
