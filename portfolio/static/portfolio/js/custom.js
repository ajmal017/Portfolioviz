$(document).ready(function() { 
    $('#descriptionCard').hide()
    $('#blanceSheetYearlyTableWrapper').hide()

    
   
    // $('#').DataTable();
    $('#incomeStatementYearlyTable').DataTable({
        "paging": false,
        "scrollX": true,
        "searching": false,
        "ordering": false,
        "bInfo": false,
        "bAutoWidth": true
        
      });


    // CARDS ---------------------------------------------------------------------------
    // Description Card ----------------------------------------------------------------
    $('#navDescriptionCard').click(function(){
        $('#financialsCard').hide()
        $('#descriptionCard').show()
        $('a#navFinancialsCard').toggleClass("active")
        $('a#navDescriptionCard').toggleClass("active")
    });

    // Financials Card ----------------------------------------------------------------
    $('#navFinancialsCard').click(function(){
        $('#financialsCard').show()
        $('#descriptionCard').hide()
        $('a#navFinancialsCard').toggleClass("active")
        $('a#navDescriptionCard').toggleClass("active")
    });
    
    




 }); // document.ready()