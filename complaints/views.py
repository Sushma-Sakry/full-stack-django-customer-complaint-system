from django.shortcuts import render

    
# # complaints/views.py
from django.shortcuts import render, redirect
from .models import Complaint

def complaint_list(request):
    complaints = Complaint.objects.all()  # Fetch all complaints from the database
    return render(request, 'complaints/list.html', {'complaints': complaints})

def home(request):
    return render(request, 'complaints/home.html')  # Create a home.html template if needed

# complaints/views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import ComplaintForm

def submit_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()  # Save the complaint to the database
            return redirect(reverse_lazy('success'))  # Redirect to the success page
    else:
        form = ComplaintForm()
    return render(request, 'complaints/submit_complaint.html', {'form': form})

def success(request):
    return render(request, 'complaints/success.html')  # Render the success template