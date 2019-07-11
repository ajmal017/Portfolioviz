$(document).ready(function() { 
    $('#descriptionCard').hide()
    $('#incomeStatementYearlyWrapper').hide()

    
   
    // $('#').DataTable(); ----------------------------------------------------------------------------
    $('#incomeStatementYearlyTable').DataTable({
        "paging": false,
        "scrollX": true,
        "searching": false,
        "ordering": false,
        "bInfo": false,
        "bAutoWidth": true
      });
    
    $('#balanceSheetYearlyTable').DataTable({
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

        // Financial Statement Buttons ----------------------------------------------------------------
        $('#btnBalanceSheet').click(function(){
            $('#incomeStatementYearlyWrapper').hide();
            $('#blanceSheetYearlyWrapper').show();
            $( '#balanceSheetYearlyTable' ).DataTable().columns.adjust();
            $( '#btnBalanceSheet' ).removeClass( "btn-outline-info" )
            $( '#btnBalanceSheet' ).addClass( "btn-info" );
            $( '#btnIncomeStatement, #btnCashFlowStatement' ).removeClass( "btn-info" )
            $( '#btnIncomeStatement, #btnCashFlowStatement' ).addClass( "btn-outline-info" );
        });

        $('#btnIncomeStatement').click(function(){
            $('#blanceSheetYearlyWrapper').hide()
            $('#incomeStatementYearlyWrapper').show()
            $( '#incomeStatementYearlyTable' ).DataTable().columns.adjust();
            $( '#btnIncomeStatement' ).removeClass( "btn-outline-info" )
            $( '#btnIncomeStatement' ).addClass( "btn-info" );
            $( '#btnBalanceSheet, #btnCashFlowStatement' ).removeClass( "btn-info" )
            $( '#btnBalanceSheet, #btnCashFlowStatement' ).addClass( "btn-outline-info" );
        });

        $('#btnCashFlowStatement').click(function(){
            $( '#btnCashFlowStatement' ).removeClass( "btn-outline-info" )
            $( '#btnCashFlowStatement' ).addClass( "btn-info" );
            $( '#btnIncomeStatement, #btnBalanceSheet' ).removeClass( "btn-info" )
            $( '#btnIncomeStatement, #btnBalanceSheet' ).addClass( "btn-outline-info" );
        });

    

    
    


 }); // document.ready()