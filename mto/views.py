import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
# from django.views.generic.base import View
#
# from jobs.models import MALRequirement, MicroTask, MTOJobCategory
from django.views.generic.base import View

from jobs.models import MTOJob, MTOJobCategory
from .forms import SignUpForm, MTOUpdateProfileForm
from .models import MTO


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'mto/register.html'

    def get_form_kwargs(self):
        kwargs = super(SignUpView, self).get_form_kwargs()
        return kwargs

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=200)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        messages.success(self.request, f"Hi {user.full_name}, your account was created successfully.")
        context = {'redirect': '/mto/login'}
        return JsonResponse(context, status=200)


# class SignUpView(View):
#     template_name = 'mto/register.html'
#
#     def get(self, *args, **kwargs):
#         form = SignUpForm
#         context = {'form': form}
#         return render(self.request, self.template_name, context)
#
#     def post(self, *args, **kwargs):
#         # check if there's need to handle race condition when creating users
#         form = SignUpForm(self.request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect(reverse('account_login'))


def dummy_home_view(request):
    mtos = MTO.objects.all()
    jobs_applied = MTOJob.objects.all()
    for job in jobs_applied:  # testing mto foreignkey
        print(job.mto.full_name)
    context = {'mtos': mtos}
    return render(request, 'mto/index.html', context)

# def microtask(request):
#     if request.method == 'POST':
#         form = MicroTaskForm(request.POST, request.FILES)
#         if form.is_valid():
#
#             job_name = form.cleaned_data['job_name']
#
#             form.save()
#             messages.success(request, f'Account created for {job_name}! You have to login')
#             return redirect('/')
#     else:
#         form = MicroTaskForm()
#
#     return render(request, 'microtask.html', {'form': form})
#
#
# def index(request):
#     microtask = MicroTask.objects.all()
#     # category = MAL_Requirements.objects.get(microtask.Category_of_the_microtask)
#
#     context = {'microtask':microtask,
#
#                 }
#     return render(request, 'MalForm.html', context)
#
# def handleSubmit(request):
#     if request.method == 'POST':
#         MAL_Job_Identification_Number = request.POST['malno']
#         Assembly_line_ID = request.POST['asi']
#         Name_of_the_Assembly_line = request.POST['nameassembly']
#         Name_of_the_person_incharge_of_the_MAL = request.POST['personname']
#         Link_of_the_output_folder = request.POST['link1']
#         Name_of_the_micro_task = request.POST['microtask']
#         Category_of_the_Microtask = request.POST['category']
#         Target_date = request.POST['td']
#         Total_budget_allocated_for_the_job = request.POST['budget']
#         Job_description = request.POST['jd']
#         Upload_job_sample = request.POST['jobsample']
#         Upload_Job_instructions = request.POST['instruction']
#         Quantity_of_the_Job = request.POST['quantity']
#         Link_of_the_Input_folder = request.POST['link2']
#
#         job = MicroTask.objects.get(id=Name_of_the_micro_task)
#         cat = MTOJobCategory.objects.get(id=Category_of_the_Microtask)
#
#         data = MALRequirement(MAL_Job_Identification_Number=MAL_Job_Identification_Number, Assembly_line_ID=Assembly_line_ID,
#                                 Name_of_the_Assembly_line=Name_of_the_Assembly_line, Name_of_the_person_incharge_of_the_MAL=Name_of_the_person_incharge_of_the_MAL, Link_of_the_output_folder=Link_of_the_output_folder,
#                                 microtask=job, microtask_category=cat, Target_date=Target_date, Total_budget_allocated_for_the_job=Total_budget_allocated_for_the_job,Job_description=Job_description,
#                                 Uploadjob_sample=Upload_job_sample, UploadJob_instructions=Upload_Job_instructions, Quantity_of_the_Job=Quantity_of_the_Job, Link_of_the_Input_folder=Link_of_the_Input_folder)
#         data.save()
#     return redirect('index')
#
# def posting_page(request,pk=None):
#     #if request.user.is_active:
#     if pk is not None:
#         try:
#             data = MicroTask.objects.get(id=pk)
#         except:
#             data = "NA"
#         return render(request,'JobPosting_Page.html', {'datas': data})
#     return render(request,'JobPosting_Page.html')


@method_decorator(login_required, name='dispatch')
class MTOProfileView(View):
    template_name = 'profile.html'
    context_object_name = 'mto'
    form = MTOUpdateProfileForm

    def get(self, *args, **kwargs):
        mto = MTO.objects.get(id=self.request.user.id)
        self.form = MTOUpdateProfileForm(instance=mto)

        # we get the items from string type to list type and get the users job categories
        jsonDec = json.decoder.JSONDecoder()
        mto_preferred_categories = jsonDec.decode(mto.job_category)
        job_categories = [MTOJobCategory.objects.get(id=job_id) for job_id in mto_preferred_categories]

        context = {self.context_object_name: mto, 'form': self.form, 'job_categories': job_categories}
        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        form = self.form(self.request.POST)
        if form.is_valid():
            phone = form.cleaned_data['contact_number']
            location = form.cleaned_data['location']
            paypal = form.cleaned_data['paypal_id']

            # convert the job categories to a list then save them as a JSON string in the database.
            job_categories = form.cleaned_data['job_category']
            job_categories_ids = json.dumps([job.id for job in job_categories])

            # update our fields in the database
            MTO.objects.filter(id=self.request.user.id).update(contact_number=phone, location=location,
                                                               job_category=job_categories_ids, paypal_id=paypal)
            messages.success(self.request, 'Changes saved successfully')
        return redirect(reverse('mto:profile'))
