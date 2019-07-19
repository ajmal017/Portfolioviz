$(document).ready(function() { 
    var period = $('#financialsPeriod').children("option:selected").val(); 
    

    // Financials DataTables ----------------------------------------------------------------------------
        // Financials YEARLY ----------------------------------------------------------------------------
        $('#balanceSheetYearlyTable, #incomeStatementYearlyTable, #cashFlowYearlyTable').DataTable({
            "paging": false,
            "scrollX": true,
            "searching": false,
            "ordering": false,
            "bInfo": false,
            "bAutoWidth": true
        });
        
        // Financials QUARTERLY ----------------------------------------------------------------------------
        $('#balanceSheetQuarterlyTable, #incomeStatementQuarterlyTable, #cashFlowQuarterlyTable').DataTable({
            "paging": false,
            "scrollX": true,
            "searching": false,
            "ordering": false,
            "bInfo": false,
            "bAutoWidth": true,
            "fixedColumns": true,
            "autoWidth": false
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
            $('#incomeStatementYearlyWrapper').show()
            $('#incomeStatementYearlyTable').DataTable().columns.adjust();


            $('#descriptionCard').hide()
            $('a#navFinancialsCard').toggleClass("active")
            $('a#navDescriptionCard').toggleClass("active")
        });
              
            // Financial Statement Buttons ----------------------------------------------------------------
            $('#btnBalanceSheet').click(function(){
                
                $( '#btnBalanceSheet' ).removeClass( "btn-outline-info" )
                $( '#btnBalanceSheet' ).addClass( "btn-info" );
                $( '#btnIncomeStatement, #btnCashFlowStatement' ).removeClass("btn-info")
                $( '#btnIncomeStatement, #btnCashFlowStatement' ).addClass("btn-outline-info"); 

                if(period == "yearly"){  
                    $('#balanceSheetYearlyWrapper').show()
                    $('#balanceSheetYearlyTable').DataTable().columns.adjust();

                    $('#incomeStatementYearlyWrapper, #incomeStatementQuarterlyWrapper').hide()
                    $('#cashFlowYearlyWrapper, #cashFlowQuarterlyWrapper').hide()
                    $('#balanceSheetQuarterlyWrapper').hide()
                }

                if(period == "quarterly"){
                    $('#balanceSheetQuarterlyWrapper').show()
                    $('#balanceSheetQuarterlyTable').DataTable().columns.adjust();
                     
                    $('#incomeStatementYearlyWrapper, #incomeStatementQuarterlyWrapper').hide()
                    $('#cashFlowYearlyWrapper, #cashFlowQuarterlyWrapper').hide()
                    $('#balanceSheetYearlyWrapper').hide()

                }
            });

            $('#btnIncomeStatement').click(function(){
                
                $( '#btnIncomeStatement' ).removeClass( "btn-outline-info" )
                $( '#btnIncomeStatement' ).addClass( "btn-info" );
                $( '#btnBalanceSheet, #btnCashFlowStatement' ).removeClass( "btn-info" )
                $( '#btnBalanceSheet, #btnCashFlowStatement' ).addClass( "btn-outline-info" );

                if(period == "yearly"){
                    $('#incomeStatementYearlyWrapper').show()
                    $('#incomeStatementYearlyTable').DataTable().columns.adjust();
                    
                    $('#incomeStatementQuarterlyWrapper').hide()     
                    $('#cashFlowYearlyWrapper, #cashFlowQuarterlyWrapper').hide()
                    $('#balanceSheetYearlyWrapper, #balanceSheetQuarterlyWrapper').hide()
                }
                
                if(period == "quarterly"){
                    $('#incomeStatementQuarterlyWrapper').show()
                    $('#incomeStatementQuarterlyTable').DataTable().columns.adjust();
                    
                    $('#incomeStatementYearlyWrapper').hide()
                    $('#cashFlowYearlyWrapper, #cashFlowQuarterlyWrapper').hide()
                    $('#balanceSheetYearlyWrapper, #balanceSheetQuarterlyWrapper').hide()
                }

            });

            $('#btnCashFlowStatement').click(function(){
                $( '#btnCashFlowStatement' ).removeClass( "btn-outline-info" )
                $( '#btnCashFlowStatement' ).addClass( "btn-info" );
                $( '#btnIncomeStatement, #btnBalanceSheet' ).removeClass( "btn-info" )
                $( '#btnIncomeStatement, #btnBalanceSheet' ).addClass( "btn-outline-info" );

                if(period == "yearly"){  
                    $('#cashFlowYearlyWrapper').show()
                    $('#cashFlowYearlyTable').DataTable().columns.adjust();
                    
                    $('#incomeStatementYearlyWrapper, #incomeStatementQuarterlyWrapper').hide()
                    $('#cashFlowQuarterlyWrapper').hide()
                    $('#balanceSheetYearlyWrapper, #balanceSheetQuarterlyWrapper').hide()
                    
                }

                if(period == "quarterly"){
                    $('#cashFlowQuarterlyWrapper').show()
                    $('#cashFlowQuarterlyTable').DataTable().columns.adjust();
                    
                    $('#incomeStatementYearlyWrapper, #incomeStatementQuarterlyWrapper').hide()
                    $('#cashFlowYearlyWrapper').hide()
                    $('#balanceSheetYearlyWrapper, #balanceSheetQuarterlyWrapper').hide()
                }

            });
        
            // Financial Statement Period Change ----------------------------------------------------------------
            $( "#financialsPeriod" ).change(function() { 
                period = $(this).children("option:selected").val();
                
                if(period == "yearly"){
                    // BALANCE SHEET ---------------------------------------------------------
                    if($('#btnBalanceSheet').hasClass( "btn-info" )){
                        $('#balanceSheetYearlyWrapper').show()
                        $('#balanceSheetYearlyTable').DataTable().columns.adjust();

                        $('#incomeStatementYearlyWrapper, #incomeStatementQuarterlyWrapper').hide()
                        $('#cashFlowYearlyWrapper, #cashFlowQuarterlyWrapper').hide()
                        $('#balanceSheetQuarterlyWrapper').hide()
                    }

                    // INCOME STATEMENT ---------------------------------------------------------
                    if($('#btnIncomeStatement').hasClass( "btn-info" )){
                        $('#incomeStatementYearlyWrapper').show()
                        $('#incomeStatementYearlyTable').DataTable().columns.adjust();
                        
                        $('#incomeStatementQuarterlyWrapper').hide()     
                        $('#cashFlowYearlyWrapper, #cashFlowQuarterlyWrapper').hide()
                        $('#balanceSheetYearlyWrapper, #balanceSheetQuarterlyWrapper').hide()
                    }

                    // CASH FLOW STATEMENT ---------------------------------------------------------
                    if($('#btnCashFlowStatement').hasClass( "btn-info" )){
                        $('#cashFlowYearlyWrapper').show()
                        $('#cashFlowYearlyTable').DataTable().columns.adjust();
                        
                        $('#incomeStatementYearlyWrapper, #incomeStatementQuarterlyWrapper').hide()
                        $('#cashFlowQuarterlyWrapper').hide()
                        $('#balanceSheetYearlyWrapper, #balanceSheetQuarterlyWrapper').hide()
                    }
                }

                if(period == "quarterly"){
                    // BALANCE SHEET ---------------------------------------------------------
                    if($( "#btnBalanceSheet" ).hasClass('btn-info')){
                        $('#balanceSheetQuarterlyWrapper').show()
                        $('#balanceSheetQuarterlyTable').DataTable().columns.adjust();
                         
                        $('#incomeStatementYearlyWrapper, #incomeStatementQuarterlyWrapper').hide()
                        $('#cashFlowYearlyWrapper, #cashFlowQuarterlyWrapper').hide()
                        $('#balanceSheetYearlyWrapper').hide()
                    }

                    // INCOME STATEMENT ---------------------------------------------------------
                    if($('#btnIncomeStatement').hasClass('btn-info')){
                        $('#incomeStatementQuarterlyWrapper').show()
                        $('#incomeStatementQuarterlyTable').DataTable().columns.adjust();
                        
                        $('#incomeStatementYearlyWrapper').hide()
                        $('#cashFlowYearlyWrapper, #cashFlowQuarterlyWrapper').hide()
                        $('#balanceSheetYearlyWrapper, #balanceSheetQuarterlyWrapper').hide()
                    }

                    // CASH FLOW STATEMENT ---------------------------------------------------------
                    if($('#btnCashFlowStatement').hasClass('btn-info')){
                        $('#cashFlowQuarterlyWrapper').show()
                        $('#cashFlowQuarterlyTable').DataTable().columns.adjust();
                        
                        $('#incomeStatementYearlyWrapper, #incomeStatementQuarterlyWrapper').hide()
                        $('#cashFlowYearlyWrapper').hide()
                        $('#balanceSheetYearlyWrapper, #balanceSheetQuarterlyWrapper').hide()
                    }
                }
            });
            
    
    
 }); // document.ready()