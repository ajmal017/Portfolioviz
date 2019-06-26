from . forms import SymbolForm

def symbol_form(request):
    symbol_form = SymbolForm()
    context = {'symbol_form': symbol_form,}
    return context