from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, NotesForm
from .models import Record

# Create your views here.
def home(request):
    search_query = request.GET.get('search', '')  # Get search query from GET request
    records = Record.objects.all()

    if search_query:
        records = records.filter(
            first_name__icontains=search_query
        ) | records.filter(
            last_name__icontains=search_query
        ) | records.filter(
            email__icontains=search_query
        ) | records.filter(
            city__icontains=search_query
        ) | records.filter(
            phone__icontains=search_query
        )  # for adding more filters


    if request.method == 'POST':
        # Handle login form Submission
        if 'username' in request.POST and 'password' in request.POST:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')

            # Authenticate user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in!")
                return redirect('home')
            else:
                messages.warning(request, "Invalid username or password.")
        
        # Handle Registration Form submission
        elif 'password1' in request.POST and 'password2' in request.POST:
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Registration successful! You can now log in.")
                return redirect('home')
            else:
                messages.error(request, "Please correct the errors below.")
        
        # Handle Unknown form Submission
        else:
            messages.error(request, "Unrecognized form submission.")
    
    return render(request, 'home.html', {
        'records':records, 
        'search_query':search_query
        })


#def login_user(request):

def logout_user(request):
    logout(request)
    messages.warning(request, "You Have Been Logged Out...")
    return redirect('home') 

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and Login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
    
    return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        customer_record = Record.objects.get(id=pk)
        # Convert the created_at field to local time
        local_created_at = timezone.localtime(customer_record.created_at)

        #Form submission for notes
        if request.method == 'POST':
            # Check if the form submission is for saving notes
            if 'save_notes' in request.POST:
                notes_form = NotesForm(request.POST, instance=customer_record)
                if notes_form.is_valid():
                    notes_form.save()
                    messages.success(request, "Notes Updated Successfully!")
            else:
                # For separating the function of saving the notes and the other fields
                form = AddRecordForm(request.POST, instance=customer_record)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Record Updated Successfully!")

            return redirect('record', pk=pk)

        else:
            form = AddRecordForm(instance=customer_record)
            notes_form = NotesForm(instance=customer_record)

        return render(request, 'record.html', {
            'customer_record': customer_record,
            'form': form,
            'notes_form': notes_form,
        })
    else:
        messages.error(request, "You Must Be Logged In To View That Page...")
        return redirect('home')
    

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.error(request, "Customer Record Has Been Deleted Successfully!")
        return redirect('home')
    else:
        messages.error(request, "You Must Be Logged In To View That Page...")
        return redirect('home')
    

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added Successfully!")
                return redirect('home')
        return render(request, 'add_record.html', {'form' : form})
    else:
        messages.error(request, "You Must Be Logged In To View That Page...")
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance = current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated Successfully!")
            return redirect('record', pk=current_record.id)
        return render(request, 'update_record.html', {'form' : form, 'current_record':current_record})
    else:
        messages.error(request, "You Must Be Logged In To Do That...")
        return redirect('home')
