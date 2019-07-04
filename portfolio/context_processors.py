from . forms import SymbolForm, AddPositionForm

def symbol_form(request):
    symbol_form = SymbolForm()
    context = {'symbol_form': symbol_form,}
    return context

def addPosition_form(request):
    addPositionForm = AddPositionForm()
    context = {'addPositionForm': addPositionForm,}
    return context

