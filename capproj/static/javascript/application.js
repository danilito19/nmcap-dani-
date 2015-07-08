$(document).on('ready', function(){
  $('.filterSelections ul').hide();

  var filters = ["yearFilter","countyFilter","amountFilter"]

  var showFilters = function(filterHandle){
    var filterId = this.id
    $('.filterSelections ul').hide();
    $('#' + filterId + 'Selections').show();
  }

  filters.forEach(function(d){
    $('#' + d).on('click', showFilters);
  })
});
