from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
#from django.shortcuts import render, render_to_response, RequestContext
from django.template import loader
#from django.template import loader, RequestContext
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm
# Create your views here.

def home(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        #obj = NoteForm.objects.create(**form.cleaned_data) 
        #form =NoteForm()
        obj = form.save(commit=False)
        obj.user = request.user
        form.save()
        form =NoteForm()
    qs = Note.objects.all()
    form =NoteForm()
    template_name = 'notes.html'
    context = {'form':form, 'object_list': qs}
    return render(request, template_name, context )



'''

def home(request):
    #template = loader.get_template('note.html')
    #form = NoteForm(request.POST or None)
    
    qs = Note.objects.all()
    print(qs)
    template_name = 'notes.html'
    context = {'object_list': qs}
    return render(request, template_name, context)
    #return render_to_response("notes.html", notes)




def home(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        object.text=form.cleaned_data.get("text")
        obj.save()
        template_name='notes.html'
        
        #save_it = form.save(commit=False)
        #save_it.save()

        context = {'notes': notes, 'form': form}
        return render(request, 'notes.html', context)
        #return render_to_response("note.html", notes)
'''


